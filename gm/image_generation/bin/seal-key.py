#!/usr/bin/env python3
"""Encrypt the OpenAI API key under a passphrase. Run ONCE, by the user.

  ! python3 -I bin/seal-key.py

The -I is not optional: without it a planted usercustomize.py can capture both the
key and the passphrase as you type them.

Writes .api-key.enc (AES-256-CBC, PBKDF2-SHA256, 600k iterations). The passphrase
is never stored anywhere — it lives only in your head, which is the entire point:
an agent running with your shell privileges can read every file on this machine,
so the only thing it cannot obtain is something that was never written down.

Afterwards, delete the plaintext key:

  rm gm/image_generation/gpt.key

While that file exists the gate is decorative — an agent can read it and spend
without asking.
"""

from __future__ import annotations

import sys

# A compiled copy of this file in __pycache__ is a copy that does not carry
# later changes — including the paid-call gate. Never leave one behind.
sys.dont_write_bytecode = True

import getpass
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENC = ROOT / ".api-key.enc"
ITERATIONS = 600_000


class Fail(SystemExit):
    def __init__(self, msg: str):
        super().__init__(f"FAIL: {msg}")


def tty_prompt(prompt: str) -> str:
    """Read a secret from the terminal, never from stdin, so it cannot be piped in."""
    try:
        with open("/dev/tty", "r+") as tty:
            return getpass.getpass(prompt, stream=tty)
    except OSError:
        raise Fail("no /dev/tty — run this in a terminal, not through a pipe. "
                   "In Claude Code: ! python3 -I bin/seal-key.py")


def encrypt(plaintext: str, passphrase: str) -> bytes:
    """Encrypt via openssl. The passphrase goes down a pipe on fd 3, so it never
    appears in argv (where `ps` would show it)."""
    r, w = os.pipe()
    try:
        os.write(w, (passphrase + "\n").encode())
    finally:
        os.close(w)
    try:
        proc = subprocess.run(
            ["openssl", "enc", "-aes-256-cbc", "-pbkdf2", "-iter", str(ITERATIONS),
             "-salt", "-pass", "fd:3"],
            input=plaintext.encode(), capture_output=True,
            pass_fds=(r,), timeout=120,
        )
    except FileNotFoundError:
        raise Fail("openssl not found.")
    finally:
        os.close(r)
    if proc.returncode != 0:
        raise Fail(f"openssl failed: {proc.stderr.decode(errors='replace').strip()[:200]}")
    return proc.stdout


def find_key_in_history(key: str) -> list[tuple[str, int]]:
    """Has this key already leaked into a shell history or session file? A key typed
    as `echo sk-... > gpt.key` is in ~/.zsh_history forever, outside the repo, where
    no vault rule reaches it. Sealing such a key protects nothing.

    Compares by value, and reports only counts — never the key itself."""
    home = Path.home()
    candidates = [home / n for n in (
        ".zsh_history", ".bash_history", ".sh_history", ".histfile",
        ".local/share/fish/fish_history", ".python_history")]
    if (home / ".zsh_sessions").is_dir():
        candidates += sorted((home / ".zsh_sessions").glob("*.history"))
    hits = []
    for f in candidates:
        try:
            if not f.is_file():
                continue
            text = f.read_bytes().decode("utf-8", "replace")
        except OSError:
            continue
        n = sum(1 for line in text.splitlines() if key in line)
        if n:
            try:
                label = str(f.relative_to(home))
                label = f"~/{label}"
            except ValueError:
                label = str(f)
            hits.append((label, n))
    return hits


def decrypt_sealed() -> str:
    """Decrypt .api-key.enc for a --check comparison. Needs the passphrase, so only
    the user can run it; the value is never printed."""
    from importlib import import_module
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    unlock = import_module("unlock")
    return unlock.decrypt(ENC.read_bytes(), tty_prompt("  passphrase: ")).strip()


def main() -> int:
    if "--check" in sys.argv:
        if not ENC.exists():
            raise Fail(f"no {ENC.name} to check.")
        key = decrypt_sealed()
        leaks = find_key_in_history(key)
        del key
        if leaks:
            print("  NOT CLEAN — the sealed key still appears in:")
            for where, n in leaks:
                print(f"    {where}  ({n} line(s))")
            print("  A shell that was open during the scrub may have rewritten it.")
            return 2
        print("  clean: the sealed key does not appear in any history file I can read.")
        if (ROOT / "gpt.key").exists():
            print(f"  BUT {ROOT / 'gpt.key'} still exists — delete it.")
            return 2
        return 0

    if ENC.exists():
        print(f"  {ENC.name} already exists.")
        if tty_prompt("  overwrite it? type YES to confirm: ") != "YES":
            print("  left alone.")
            return 1

    existing = ROOT / "gpt.key"
    hint = f" (press Enter to use the contents of {existing.name})" if existing.exists() else ""
    key = tty_prompt(f"  OpenAI API key{hint}: ").strip()
    if not key and existing.exists():
        key = existing.read_text().strip()
        print(f"  using {existing.name}")
    if not key:
        raise Fail("no key given.")
    if not key.startswith("sk-"):
        raise Fail("that does not look like an OpenAI key (expected it to start 'sk-').")

    passphrase = tty_prompt("  passphrase to protect it: ")
    if len(passphrase) < 8:
        raise Fail("use at least 8 characters.")
    if passphrase != tty_prompt("  again: "):
        raise Fail("passphrases did not match.")

    blob = encrypt(key, passphrase)

    tmp = ENC.with_suffix(".tmp")
    tmp.write_bytes(blob)
    os.chmod(tmp, 0o600)
    tmp.replace(ENC)
    print(f"\n  wrote {ENC.name}  ({len(blob)} bytes, AES-256, {ITERATIONS:,} iterations)")
    print("  verifying it decrypts...")

    from importlib import import_module
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    unlock = import_module("unlock")
    if unlock.decrypt(ENC.read_bytes(), passphrase).strip() != key:
        raise Fail("the file did not decrypt back to the key. Do NOT delete gpt.key.")
    print("  verified.")

    leaks = find_key_in_history(key)
    if leaks:
        print()
        print("  " + "!" * 58)
        print("  THIS KEY IS ALREADY COMPROMISED. SEALING IT IS NOT ENOUGH.")
        print("  " + "!" * 58)
        for where, n in leaks:
            print(f"  found in {where} ({n} line(s))")
        print()
        print("  Those files are outside the repo, readable by any agent with no")
        print("  prompt, and almost certainly in your backups already. Deleting")
        print("  gpt.key does not help — the key just lives somewhere less obvious.")
        print()
        print("  SAFEST: rotate. Revoke this key at platform.openai.com/api-keys,")
        print("  create a new one, re-run this script and PASTE it at the prompt.")
        print("  Rotation works without having to find every stray copy.")
        print()
        print("  ALTERNATIVE: keep this key and scrub the strays yourself. That is")
        print("  fine, but it only works if it is COMPLETE — including any shell")
        print("  still open, which rewrites its history on exit.")
        print()
        if tty_prompt("  type SCRUB to keep this key and clean up yourself, "
                      "or Enter to stop: ").strip() != "SCRUB":
            print("\n  stopped. The key is sealed in .api-key.enc, but a working copy")
            print("  is still in the files above — the gate is not effective yet.")
            return 2
        print()
        print("  OK. The key is sealed. NOW DO ALL OF THIS:")
        print()
        print("    # in EVERY open terminal, so none rewrites history on exit:")
        print("    unset HISTFILE")
        print()
        print("    rm -f ~/.zsh_history ~/.zsh_sessions/*.history")
        print(f"    rm -f {existing}")
        print()
        print("  Then re-run this script with --check to confirm it is clean.")
        return 0

    if existing.exists():
        print(f"\n  NOW DELETE THE PLAINTEXT:  rm {existing.relative_to(ROOT.parent.parent)}")
        print("  while it exists, an agent can read it and spend without asking.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Fail as e:
        print(e, file=sys.stderr)
        sys.exit(1)
