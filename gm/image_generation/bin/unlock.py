#!/usr/bin/env python3
"""Approve and run ONE paid API call. Run by the USER, never by an agent.

  ! python3 -I bin/unlock.py

The -I matters. Without it Python imports usercustomize.py from the user site
directory on every start, and anything written there can monkeypatch getpass or
subprocess to capture your passphrase without touching this file. -I also ignores
PYTHONPATH, which can shadow stdlib modules. Always use it.

bin/gen.py cannot make a paid call: it holds no key. When one is needed it writes
.api-request and stops. This script shows you that request and the exact command it
would run, asks for the passphrase, decrypts the key in memory, and hands it to
gen.py down a pipe — so the key never touches disk in plaintext and never reaches a
process an agent started on its own.

Set the key up once with  ! python3 -I bin/seal-key.py

What this cannot defend against: an agent that edits THIS FILE, or that plants a
usercustomize.py / PYTHONPATH hijack if you forget the -I. Nothing running as your
user can stop either. Skim this file before typing a passphrase into it, always pass
-I, and if you want certainty keep a copy outside the repo and run that.
"""

from __future__ import annotations

import sys

# A compiled copy of this file in __pycache__ is a copy that does not carry
# later changes — including the paid-call gate. Never leave one behind.
sys.dont_write_bytecode = True

import getpass
import json
import os
import re
import subprocess
import time
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
BIN = Path(__file__).resolve().parent
REQUEST = ROOT / ".api-request"
ENC = ROOT / ".api-key.enc"
ITERATIONS = 600_000


class Fail(SystemExit):
    def __init__(self, msg: str):
        super().__init__(f"FAIL: {msg}")


# Any readable key makes --key-fd meaningless, so look for one the way an attacker
# would find one: anywhere under the vault, not just `*.key` in its root. A key at
# tmp/k.txt or sources/key.pem evaded the first version of this check.
# NOTE: .api-key.enc is the SEALED file and must never match -- it is the thing that
# makes the gate work.
PLAINTEXT_KEY_GLOBS = ("*.key", "*.pem", "*key.txt", "*key.json", "*.secret")
KEY_RE = re.compile(r"\bsk-[A-Za-z0-9_\-]{20,}")
# NOTE: ".enc" is deliberately NOT here. It is the one extension this vault teaches
# agents to use; the real sealed file is exempted by its full path at the vault root
# (never by basename -- tmp/.api-key.enc was a blind spot behind a trusted name), and
# skipping the suffix hid a plaintext key in backup.enc from both passes.
# An allowlist of text suffixes needs updating every time someone invents a config
# format -- it was missing .toml in a Poetry repo. Deny the binaries instead and sniff
# everything else, so a new suffix is covered by default rather than by remembering.
BINARY_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".tif", ".tiff",
                   ".pdf", ".zip", ".gz", ".bz2", ".xz", ".tar", ".pyc", ".pyo",
                   ".so", ".dylib", ".woff", ".woff2", ".ttf", ".otf", ".mp4", ".mov",
                   ".mp3", ".wav", ".psd", ".ai", ".sketch", ".ico", ".icns"}


def find_plaintext_keys(root: Path) -> list[str]:
    """Vault-relative paths of files that may hold a usable key in the clear.

    Two passes, because neither alone is enough: suspicious NAMES catch an empty or
    rotated keyfile, and a CONTENT sniff catches a key saved under a name no pattern
    would guess -- tmp/k.txt defeated a name-only version of this check.

    Walks with os.walk(followlinks=True) rather than rglob: rglob does not descend into
    symlinked directories, so a symlinked subtree hid keys from BOTH passes. Cycles are
    bounded by a resolved-path set.

    The name pass searches EVERYTHING. The content sniff skips binaries, files over
    1 MB, and a few large subtrees, all for speed -- skipping ref_images there once hid
    a literal key.key inside the subtree agents write into most, so the skip list stays
    off the name pass.

    Accepted misses, by design rather than oversight: a key inside a binary (a .png, a
    zip), one appended to a file over 1 MB, one under a skipped subtree with an
    innocuous name, and ~/.codex/auth.json, which is a separate ungated credential
    (rules.md says so). This is a tripwire for the plausible, not a proof.
    """
    hits = set()
    slow = {".git", "__pycache__", "node_modules", ".obsidian"}
    sealed = (root / ".api-key.enc").resolve()
    seen_dirs = set()

    for dirpath, dirnames, filenames in os.walk(root, followlinks=True):
        here = Path(dirpath)
        try:
            real = here.resolve()
        except OSError:
            continue
        if real in seen_dirs:          # symlink cycle
            dirnames[:] = []
            continue
        seen_dirs.add(real)
        for fname in filenames:
            f = here / fname
            try:
                # only the vault root's own sealed file is exempt; a stray
                # tmp/.api-key.enc is a plaintext key hiding behind a trusted name
                if f.resolve() == sealed or not f.is_file():
                    continue
                rel = str(f.relative_to(root))
            except (OSError, ValueError):
                continue

            # case-insensitively: API.KEY and creds.PEM are innocent filenames, and
            # the name pass exists for exactly the keyfiles the sk- sniff cannot see
            lower = PurePosixPath(fname.lower())
            if any(lower.match(pat) for pat in PLAINTEXT_KEY_GLOBS):
                hits.add(rel)
                continue
            if f.suffix.lower() in BINARY_SUFFIXES:
                continue
            if slow & set(Path(rel).parts):
                continue
            try:
                if f.stat().st_size > 1_000_000:
                    continue
                if KEY_RE.search(f.read_text("utf8", "ignore")):
                    hits.add(rel)
            except OSError:
                continue
    return sorted(hits)


def tty_prompt(prompt: str) -> str:
    try:
        with open("/dev/tty", "r+") as tty:
            return getpass.getpass(prompt, stream=tty)
    except OSError:
        raise Fail("no /dev/tty — run this in a terminal. In Claude Code: "
                   "! python3 -I bin/unlock.py")


def decrypt(blob: bytes, passphrase: str) -> str:
    """Decrypt via openssl, passphrase on fd 3 so it never appears in argv."""
    r, w = os.pipe()
    try:
        os.write(w, (passphrase + "\n").encode())
    finally:
        os.close(w)
    try:
        proc = subprocess.run(
            ["openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2",
             "-iter", str(ITERATIONS), "-pass", "fd:3"],
            input=blob, capture_output=True, pass_fds=(r,), timeout=120,
        )
    except FileNotFoundError:
        raise Fail("openssl not found.")
    finally:
        os.close(r)
    if proc.returncode != 0:
        raise Fail("wrong passphrase, or .api-key.enc is damaged. Nothing was spent.")
    return proc.stdout.decode()


def main() -> int:
    if not REQUEST.exists():
        raise Fail(
            "no pending request — nothing is waiting for approval.\n"
            "  gen.py writes .api-request when a paid call needs you. If an agent "
            "asked you to run this without one, ask it what it wants to spend on."
        )

    try:
        req = json.loads(REQUEST.read_text())
        argv, summary = list(req["argv"]), list(req["summary"])
        age = int(time.time() - req["written"])
    except (json.JSONDecodeError, OSError, KeyError, TypeError) as e:
        raise Fail(f"unreadable .api-request ({e}). Delete it and ask the agent to retry.")

    def verify_digests(when: str) -> None:
        """Refuse if any bound file changed. Called TWICE: once here to fail before the
        user is asked anything, and again immediately before launching gen.py -- the
        passphrase prompt is a window in which a file could still be swapped, and
        checking only up front left exactly that window open."""
        import hashlib
        for path, expected in (req.get("digests") or {}).items():
            # Keys are vault-relative (gen.py writes them that way); resolve against
            # ROOT, never against unlock.py's cwd, or running it from elsewhere fails
            # closed on a perfectly readable file.
            target = Path(path) if Path(path).is_absolute() else ROOT / path
            try:
                actual = hashlib.md5(target.read_bytes()).hexdigest()
            except OSError as e:
                raise Fail(f"a file this request depends on is unreadable: {path} ({e}). "
                           "Nothing was spent.")
            if actual != expected:
                raise Fail(
                    f"REFUSING: {path} has CHANGED {when}.\n"
                    "  You would be approving something other than what the summary "
                    "describes.\n"
                    "  Delete .api-request, ask the agent to prepare the call again, and "
                    "read the new summary.")

    if req.get("selftest"):
        raise Fail(
            "this request is marked as a selftest artefact, so it will not be approved.\n"
            "  gen.py sets that marker whenever VAULT_SELFTEST=1 is in its environment --\n"
            "  if you exported that while debugging, unset it and prepare the call again.\n"
            "  Otherwise deleting it is safe:  rm .api-request")

    verify_digests("since this request was written")
    if not req.get("digests"):
        print("  NOTE: this request binds no file digests — it predates that check.")

    if "--key-fd" in argv:
        raise Fail("the request already carries --key-fd, which only this script may "
                   "add. Refusing it. Delete .api-request and ask what happened.")
    _b = argv.index("--backend") + 1 if "--backend" in argv else -1
    if _b < 1 or _b >= len(argv) or argv[_b] != "api":
        raise Fail("that request is not a paid api call; refusing to run it.")

    if not ENC.exists():
        raise Fail(f"no {ENC.name}. Set the key up first:  ! python3 -I bin/seal-key.py")

    # gen.py refuses --key-fd while a readable key sits in the vault, because then the
    # fd proves nothing -- anything could have supplied it. Check here too, BEFORE the
    # approval prompt: otherwise you read the summary, type your passphrase, and only
    # then get refused.
    plain = find_plaintext_keys(ROOT)
    if plain:
        raise Fail(
            f"a plaintext key is still in the vault ({', '.join(plain)}), so this "
            f"approval cannot mean anything —\n"
            f"  anything on this machine can already read that file and spend without "
            f"asking you. gen.py will refuse the call.\n"
            f"  Delete it first, then run this again:\n"
            f"    rm {ROOT / plain[0]}"
        )

    print()
    print("  PAID API CALL — you are approving this one call")
    print("  " + "-" * 60)
    for line in summary:
        print(f"  {line}")
    print(f"  written {age}s ago")
    print("  " + "-" * 60)
    print("  command that will run:")
    print(f"    python3 bin/gen.py {' '.join(argv)}")
    print("  " + "-" * 60)
    if age > 1800:
        print("  NOTE: over 30 minutes old. Check it is still what you mean to pay for.")

    if sys.stdin.isatty():
        try:
            with open("/dev/tty", "r+") as tty:
                tty.write("\n  run it? [y/N] ")
                tty.flush()
                if tty.readline().strip().lower() not in ("y", "yes"):
                    print("  not approved; nothing was spent.")
                    return 1
        except OSError:
            pass

    key = decrypt(ENC.read_bytes(), tty_prompt("  passphrase: ")).strip()
    if not key.startswith("sk-"):
        raise Fail("decrypted value is not an OpenAI key. Nothing was spent.")

    # Hand the key to gen.py down a pipe: not argv, not the environment.
    r, w = os.pipe()
    try:
        os.write(w, key.encode())
    finally:
        os.close(w)
    del key

    # Re-verify immediately before the call: everything above gave an attacker a window
    # -- reading the summary, typing the passphrase -- in which a bound file could be
    # swapped for one the user never approved.
    verify_digests("while you were approving it")

    # Consume the request BEFORE the call, so a failure cannot be silently retried.
    REQUEST.unlink(missing_ok=True)

    print("\n  running the call...\n")
    try:
        proc = subprocess.run(
            [sys.executable, "-I", str(BIN / "gen.py"), *argv, "--key-fd", str(r)],
            pass_fds=(r,), cwd=str(ROOT),
        )
    finally:
        try:
            os.close(r)
        except OSError:
            pass

    print()
    if proc.returncode == 0:
        print("  call completed. The approval is used up — another call needs another unlock.")
    else:
        print(f"  gen.py exited {proc.returncode}. Whether it billed depends on how far "
              "it got; check the receipt and your OpenAI usage page.")
        print("  The approval is used up either way.")
    return proc.returncode


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Fail as e:
        print(e, file=sys.stderr)
        sys.exit(1)
