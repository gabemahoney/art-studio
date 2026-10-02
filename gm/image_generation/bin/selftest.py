#!/usr/bin/env python3
"""Exercise every paid-call guard without spending a cent.

  python3 -I bin/selftest.py

Runs gen.py under --dry-run and in its fail-closed mode only. It never passes
--key-fd, never runs unlock.py or seal-key.py, and never completes an API call, so
it is safe against a funded account. Run it after touching anything in bin/.

Each case asserts that a specific invariant FAILS CLOSED. A guard that stops firing
is a guard that has silently been removed.
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import re as _re_top
import builtins
import os
import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GEN = [sys.executable, "-I", str(ROOT / "bin" / "gen.py")]
ANCHOR = "ref_images/style_references/canonical_style_reference.png"
TARGET = "outputs/the-rusty-robot/v061/image.png"
TARGET2 = "outputs/the-rusty-robot/v060/image.png"


def run(args: list[str]) -> tuple[int, str]:
    p = subprocess.run(GEN + args, cwd=ROOT, capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def main() -> int:
    # The headline used to be `len(cases) + <a literal>`, and the literal drifted the
    # first time a check was added without it -- 35 checks reported as 34. Count the
    # lines that actually announce a check instead, so the number cannot lie.
    _checks = [0]
    _real_print = builtins.print

    def print(*a, **kw):  # noqa: A001 - shadows builtins inside main deliberately
        if a and isinstance(a[0], str) and a[0].lstrip().startswith(("[ok ]", "[FAIL]")):
            _checks[0] += 1
        _real_print(*a, **kw)

    # gen.py is loaded once, up front: several checks below must call ITS functions
    # rather than reimplement them, which is how the gate check drifted weaker.
    import ast
    import importlib.util as _iu
    _gspec = _iu.spec_from_file_location("_gen", ROOT / "bin" / "gen.py")
    _gen = _iu.module_from_spec(_gspec); _gspec.loader.exec_module(_gen)

    if not _gen.vpath(TARGET).exists():
        print(f"  skip: {TARGET} missing; pass a different target in selftest.py")
        return 0

    tmp = Path(tempfile.mkdtemp(prefix="selftest-", dir=ROOT / "tmp"))
    # Build a REAL prompt with prompt.py, so the One Rule #2 check passes and the
    # guards under test are the ones that actually fire.
    prompt, spec = tmp / "p.txt", tmp / "spec.txt"
    spec.write_text("A single horizontal test frame of empty ground under a dark sky.\n")
    built = subprocess.run(
        [sys.executable, "-I", str(ROOT / "bin" / "prompt.py"),
         "--role", "STYLE:Match its hand-painted matte rendering only.",
         "--task", "A single horizontal test frame.",
         "--spec-file", str(spec), "-o", str(prompt)],
        cwd=ROOT, capture_output=True, text=True)
    if built.returncode != 0 or not prompt.exists():
        print("  FAIL: could not build a test prompt with prompt.py:")
        print("   ", (built.stdout + built.stderr).strip()[:300])
        return 1

    def mask(name: str, *draw: str) -> Path:
        p = tmp / name
        subprocess.run(["magick", "-size", "1536x1024", "xc:black", "-fill", "white",
                        *draw, "-alpha", "off", str(p)], check=True)
        return p

    small = mask("small.png", "-draw", "rectangle 60,430 390,930")
    black = mask("black.png")
    big = mask("big.png", "-draw", "rectangle 0,0 1536,700")      # 68% — past the 1e6 fx cutoff
    alpha_mask = tmp / "alpha.png"                                 # shape lives in alpha
    subprocess.run(["magick", "-size", "1536x1024", "xc:black", "-fill", "white",
                    "-draw", "rectangle 60,430 390,930", "-blur", "0x12",
                    str(alpha_mask)], check=True)
    wrong = tmp / "wrong.png"
    subprocess.run(["magick", "-size", "800x600", "xc:white", "-alpha", "off",
                    str(wrong)], check=True)

    # a second prompt, built for masked calls (EDIT TARGET first, anchor named by role)
    mprompt = tmp / "pm.txt"
    subprocess.run(
        [sys.executable, "-I", str(ROOT / "bin" / "prompt.py"), "--masked",
         "--role", "EDIT TARGET:The image being repaired.",
         "--role", "STYLE:Match its hand-painted matte rendering only.",
         "--task", "Repair one region.", "--spec-file", str(spec), "-o", str(mprompt)],
        cwd=ROOT, capture_output=True, text=True)

    # a prompt ending in the LEGACY closing wording, which names image 1 by index
    lprompt = tmp / "pl.txt"
    body = mprompt.read_text().rstrip().splitlines()
    body[-1] = ("Render everything in image 1's exact brush scale: fewest possible "
                "flat shapes, no blending, no micro-detail.")
    lprompt.write_text("\n".join(body) + "\n")

    base = ["--scene", "the-rusty-robot", "--prompt-file", str(prompt)]
    mbase = ["--scene", "the-rusty-robot", "--prompt-file", str(mprompt)]
    lbase = ["--scene", "the-rusty-robot", "--prompt-file", str(lprompt)]
    T = ["--attach", f"{TARGET}:EDIT TARGET"]
    A = ["--attach", f"{ANCHOR}:STYLE"]
    M = ["--mask", str(small.relative_to(ROOT))]

    cases = [
        ("anchor must be image 1 when unmasked",
         base + T + A + ["--dry-run"], "One Rule #1"),
        ("anchor may not be image 1 of a masked call, under ANY role",
         mbase + A + T + ["--backend", "api"] + M + ["--dry-run"], "repaint the anchor"),
        ("anchor relabelled EDIT TARGET is still refused",
         mbase + ["--attach", f"{ANCHOR}:EDIT TARGET"] + ["--backend", "api"] + M
         + ["--dry-run"], "repaint the anchor"),
        ("image 1 must carry role EDIT TARGET when masked",
         mbase + ["--attach", f"{TARGET}:IDENTITY"] + A + ["--backend", "api"] + M
         + ["--dry-run"], "EDIT TARGET as image 1"),
        ("--size must match the masked image",
         mbase + T + A + ["--backend", "api", "--size", "1200x1500"] + M + ["--dry-run"],
         "does not match the image being masked"),
        ("only one EDIT TARGET on a masked call",
         mbase + T + ["--attach", f"{TARGET2}:EDIT TARGET"] + A + ["--backend", "api"]
         + M + ["--dry-run"], "more than one EDIT TARGET"),
        ("anchor still required on a masked call",
         mbase + T + ["--backend", "api"] + M + ["--dry-run"], "must still attach the style anchor"),
        ("anchor may not be attached twice",
         mbase + T + A + A + ["--backend", "api"] + M + ["--dry-run"], "anchor attached twice"),
        ("dead codex model caught by --dry-run, not at call time",
         base + A + ["--model", "gpt-5.6-terra", "--dry-run"], "cannot generate images"),
        ("more than five attachments refused",
         base + A + [x for _ in range(5) for x in ("--attach", f"{TARGET}:IDENTITY")]
         + ["--dry-run"], "at most FIVE"),
        ("mask rejected on the codex backend",
         base + A + T + M + ["--dry-run"], "only applies to --backend api"),
        ("mask over 63.6% does not crash on scientific notation",
         mbase + T + A + ["--backend", "api", "--mask", str(big.relative_to(ROOT))],
         "holds no key"),
        ("mask carrying an alpha channel rejected",
         mbase + T + A + ["--backend", "api", "--mask", str(alpha_mask.relative_to(ROOT)),
                          "--dry-run"], "carries an alpha channel"),
        ("mask outside the vault rejected",
         mbase + T + A + ["--backend", "api", "--mask", "/tmp/not-in-vault.png",
                          "--dry-run"], "no such mask"),
        ("all-black mask rejected",
         mbase + T + A + ["--backend", "api", "--mask", str(black.relative_to(ROOT)), "--dry-run"],
         "entirely black"),
        ("mask dimensions must match",
         mbase + T + A + ["--backend", "api", "--mask", str(wrong.relative_to(ROOT)), "--dry-run"],
         "they must match"),
        ("stdin prompt rejected on a paid call",
         ["--scene", "the-rusty-robot", "--prompt-file", "-"] + T + A
         + ["--backend", "api", "--dry-run"], "cannot be used with --backend api"),
        ("mask meaningless with --refinish",
         ["--refinish", "outputs/the-rusty-robot/v061", "--final-size", "2172x1448"] + M,
         "no meaning with --refinish"),
        ("ordinary closing line refused on a masked call",
         base + T + A + ["--backend", "api"] + M + ["--dry-run"],
         "image being repainted"),
        ("masked closing line refused on an unmasked call",
         mbase + A + ["--dry-run"], "not masked"),
        ("prompt.py still demands STYLE first without --masked",
         None, "One Rule #1"),
        ("legacy closing line refused on a masked call",
         lbase + T + A + ["--backend", "api"] + M + ["--dry-run"],
         "legacy closing style line"),
        ("paid call fails closed without a key",
         mbase + T + A + ["--backend", "api"] + M, "holds no key"),
        # --key-fd is the user's approval arriving from unlock.py. While a readable
        # *.key sits in the vault, anyone can forge it -- `--key-fd 3 3< gpt.key`
        # spends with no approval -- so gen.py must refuse the fd path outright.
        # Only meaningful while a plaintext key exists; skipped once sealed.
        *([("--key-fd refused while a plaintext key is in the vault",
            mbase + T + A + ["--backend", "api", "--key-fd", "0"] + M,
            "refusing --key-fd")]
          if _gen.find_plaintext_keys(ROOT) else []),
    ]

    # Mark every request this run provokes: unlock.py refuses marked requests, so a
    # strand left by a crash between writing and cleanup cannot be approved.
    os.environ["VAULT_SELFTEST"] = "1"

    failures = 0
    for name, args, expect in cases:
        if args is None:
            r = subprocess.run(
                [sys.executable, "-I", str(ROOT / "bin" / "prompt.py"),
                 "--role", "EDIT TARGET:x", "--role", "STYLE:y",
                 "--task", "t", "--spec-file", str(spec)],
                cwd=ROOT, capture_output=True, text=True)
            code, out = r.returncode, r.stdout + r.stderr
        else:
            code, out = run(args)
        ok = code != 0 and expect in out
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")
        if not ok:
            failures += 1
            print(f"         expected {expect!r}, exit {code}; got:\n         "
                  + out.strip().replace("\n", "\n         ")[:400])

    # positive control — a correctly built masked call must be ACCEPTED
    code, out = run(mbase + T + A + ["--backend", "api"] + M + ["--dry-run"])
    ok = code == 0 and "invariants OK" in out
    print(f"  [{'ok ' if ok else 'FAIL'}] a correctly built masked call is accepted")
    failures += 0 if ok else 1
    if not ok:
        print("         " + out.strip().replace("\n", "\n         ")[:300])

    # the fail-closed case above should have written a request that binds content
    req = ROOT / ".api-request"
    if req.exists():
        d = json.loads(req.read_text())
        n = len(d.get("digests") or {})
        # Keys must be vault-RELATIVE for anything under ROOT, or unlock.py resolves
        # them against its own cwd and fails closed on a readable file. A refactor back
        # to absolute keys, or to skipping an unhashable file, otherwise passes silently.
        keys = list((d.get("digests") or {}).keys())
        abs_keys = [k for k in keys if k.startswith("/")
                    and Path(k).resolve().is_relative_to(ROOT)]
        ok = (n >= 3 and any("mask" in s for s in d.get("summary", []))
              and not abs_keys)
        print(f"  [{'ok ' if ok else 'FAIL'}] approval request binds file content "
              f"({n} digests, vault-relative) and names the mask")
        for k in abs_keys:
            print(f"         {k} is absolute but lies under the vault")
        failures += 0 if ok else 1
        req.unlink()
    else:
        print("  [FAIL] fail-closed run wrote no .api-request")
        failures += 1

    # THREAT MODEL, so nobody mistakes this for more than it is. Every bypass found so
    # far -- a nested def inside the exempt function, a second definition of it, a
    # method of the same name -- requires the ability to EDIT gen.py. Anything that can
    # edit gen.py can delete the gate outright, so this check cannot defend against it
    # and does not try. What it defends against is a key read REINTRODUCED BY ACCIDENT,
    # by a future maintainer or model that did not know the rule, and a reviewer who
    # would not have spotted it. Judge new cases by that standard: a shape someone might
    # write innocently is worth catching; one that only an adversary with write access
    # would construct is not, and the exemption bound below exists to stop the obvious
    # accidents from hiding there, not to resist an attacker.
    #
    # gen.py must not read a key. This is a TRIPWIRE FOR THE OBVIOUS, not a proof:
    # static analysis cannot rule out an obfuscated read, and it only parses gen.py.
    # Its predecessor was a grep for "gpt.key"/"OPENAI_API_KEY", which a plain
    # `ROOT.glob("*.key")[0].read_text()` walked straight past; an ast-only version
    # missed the env lookups the grep caught. So it does both, and exempts the guard's
    # own detection glob BY USE SITE -- does the statement read? -- never by value.
    # The probes below are live cases that defeated an earlier version of this check --
    # positive ones are real reads it must catch, negative ones are false positives it
    # must not. They run every time, so the detector cannot be quietly weakened. The
    # printed line counts them rather than naming a number that goes stale.
    import ast

    KEYISH = ("key", "secret", "token", "credential")
    READISH = ("read_text", "read_bytes", "open", "cat", "environ", "getenv",
               "check_output", "Popen", "run", "popen", "system", "loads", "read",
               "get", "copy", "copyfile", "copy2", "move", "write_text", "write_bytes")

    def _fold(node):
        """Constant-fold concatenation, so "gpt." + "key" reads as one literal."""
        if isinstance(node, ast.Constant) and isinstance(node.value, (str, bytes)):
            v = node.value
            return v.decode("utf8", "replace") if isinstance(v, bytes) else v
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            a, b = _fold(node.left), _fold(node.right)
            if a is not None and b is not None:
                return a + b
        return None

    def _callee(call):
        """Name of whatever is being called: `_load(...)`, `self._load(...)`, or a
        lambda bound to a name. Matching only a bare Name let a method bypass the
        call-site taint while the plain-function form was caught."""
        f = call.func
        if isinstance(f, ast.Name):
            return f.id
        if isinstance(f, ast.Attribute):
            return f.attr
        return None

    def _keyish(s):
        # A credential is an IDENTIFIER -- a filename or an env var name. Prose that
        # merely mentions a key is not one, and this codebase says "tokens" constantly
        # meaning model tokens: `return src.read_bytes(), f"...tokens used..."` is a
        # read of an IMAGE in the same statement as the word token.
        if s is None:
            return False
        # No length or token-count cap. Two earlier attempts each traded one innocent
        # shape for another: a 64-char whole-string cap hid absolute paths (71 chars
        # here, and the house idiom), and a >3-token "prose" rule then hid short shell
        # reads like os.system("cp gpt.key /tmp/k && chmod 600 /tmp/k"). What actually
        # separates prose from a credential is SENTENCE punctuation, stripped per token
        # in _cred below: "key." degrades to the plain word "key", while gpt.key,
        # OPENAI_API_KEY and a long absolute path keep their internal punctuation.
        toks = s.split()
        if not toks:
            return False
        # Prose is not a credential, but `os.popen("cat gpt.key")` is a whitespace
        # string that IS one -- so test each token, not the whole string. And a token
        # only looks like a credential if it is punctuated or shouted: "gpt.key",
        # "OPENAI_API_KEY", ".secret" qualify; the English word "tokens" does not,
        # and this codebase says "tokens used" in a receipt beside an image read.
        # The API's usage fields are input_tokens/output_tokens/total_tokens. The
        # underscore makes them non-alpha, so they read as credentials and honest cost
        # reporting would fail this check -- which is pressure to loosen the predicate
        # again, the thing that caused two regressions already.
        # Only the API's own field names: input_tokens / output_tokens / total_tokens.
        # A "tokens_" prefix was also exempt and no API field uses it, so it only hid
        # real credential names like tokens_secret.
        USAGE_FIELDS = ("_tokens",)

        def _cred(tok: str) -> bool:
            tok = tok.rstrip(".,;:!?\"')")          # sentence punctuation, not path dots
            low = tok.lower()
            if any(u in low for u in USAGE_FIELDS):
                return False
            if not any(w in low for w in KEYISH):
                return False
            return not tok.isalpha() or tok.isupper()
        return any(_cred(tok) for tok in toks)

    # find_plaintext_keys() reads files looking for keys -- that is its job, and with
    # if/while tests now examined it trips its own detector. Exempt it by NAME, which is
    # bounded and auditable; selftest already asserts the function is byte-identical in
    # gen.py and unlock.py, so the exemption cannot be widened by editing one copy.
    BY_DESIGN = {"find_plaintext_keys"}

    def _exempt_nodes(tree) -> tuple[set, list[str]]:
        """Ids of statements inside a by-design reader, and any reason to refuse.

        A bare name matched anywhere in the tree is a hiding place, not an exemption:
        a nested def, a second module-level def, or a method of the same name all got
        skipped, and the byte-identity check could not see it because it compared the
        FIRST match. So: the name must resolve to exactly ONE definition, that
        definition must be a direct child of the module, and only its OWN statements
        are skipped -- never a nested function's body.
        """
        skip, problems = set(), []
        for name in sorted(BY_DESIGN):
            defs = [n for n in ast.walk(tree)
                    if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
                    and n.name == name]
            defs += [n for n in ast.walk(tree) if isinstance(n, ast.Assign)
                     and any(isinstance(tg, ast.Name) and tg.id == name
                             for tg in n.targets)]
            if not defs:
                continue            # nothing to exempt in this source; not a problem
            if len(defs) > 1:
                problems.append(f"{name} has {len(defs)} definitions; expected exactly 1")
                continue
            fn = defs[0]
            if fn not in getattr(tree, "body", []):
                problems.append(f"{name} is not a module-level definition")
                continue

            def own(node):
                """Statements belonging to this function, stopping at nested defs."""
                for child in ast.iter_child_nodes(node):
                    if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef,
                                          ast.ClassDef, ast.Lambda)):
                        continue
                    yield child
                    yield from own(child)

            skip |= {id(n) for n in own(fn)}
        return skip, problems

    def key_reads(src: str) -> list[str]:
        out = []
        tree = ast.parse(src)
        _skip, _problems = _exempt_nodes(tree)
        out += [f"by-design exemption is unsafe: {p}" for p in _problems]
        # Pass 1: taint. `KEYFILE = "gpt.key"` then `open(KEYFILE)` is two statements,
        # and no single-statement check sees it -- a module-level path constant is the
        # likeliest way a key read gets reintroduced here.
        tainted = set()

        def _arg_keyish(node) -> bool:
            """A key-ish constant anywhere in the expression, or a tainted name.
            `_fold` alone returns None for `ROOT / "gpt.key"` because the BinOp has a
            Name on the left -- and that is the native path idiom here, so every
            call-site test must use this, not `_keyish(_fold(...))`."""
            return any(_keyish(_fold(n)) for n in ast.walk(node)
                       if isinstance(n, (ast.Constant, ast.BinOp))) or any(
                       isinstance(n, ast.Name) and n.id in tainted
                       for n in ast.walk(node))

        def _root_name(node):
            """Base variable of an attribute chain: `p.name.lower()` -> `p`. Tainting the
            bare attribute instead ('name') poisons every expression in the file."""
            while isinstance(node, (ast.Attribute, ast.Call, ast.Subscript)):
                if isinstance(node, ast.Call):
                    # `str(p)` -> p, not str: a plain function wrapping the thing we
                    # care about. `p.read_text()` -> the attribute's own value.
                    node = (node.args[0] if isinstance(node.func, ast.Name) and node.args
                            else node.func)
                else:
                    node = node.value
            return node if isinstance(node, ast.Name) else None

        def _side_keyish(node) -> bool:
            """Is this expression itself a known key reference? A key-ish literal
            anywhere in it, or the node IS a tainted name/attribute. Deliberately not
            "contains a tainted name": that spreads through every comparison."""
            if any(_keyish(_fold(n)) for n in ast.walk(node)
                   if isinstance(n, (ast.Constant, ast.BinOp))):
                return True
            if isinstance(node, ast.Name):
                return node.id in tainted
            if isinstance(node, ast.Attribute):
                return node.attr in tainted
            return False

        def _bind(targets, source):
            """Taint names bound from anything key-ish. Runs to a fixed point, so
            CANDS = ["gpt.key"] then `for c in CANDS` taints c as well."""
            if not any(_keyish(_fold(n)) for n in ast.walk(source)
                       if isinstance(n, (ast.Constant, ast.BinOp))) and not any(
                       isinstance(n, ast.Name) and n.id in tainted
                       for n in ast.walk(source)):
                return
            for tgt in targets:
                for n in ast.walk(tgt):
                    if isinstance(n, ast.Name):
                        tainted.add(n.id)
                    elif isinstance(n, ast.Attribute):
                        # `class C: f = "gpt.key"` -> taint the attribute name, so a
                        # later `open(C.f)` is seen
                        tainted.add(n.attr)

        for _ in range(4):                      # fixed point; depth is tiny here
            before = len(tainted)
            for stmt in ast.walk(tree):
                # The by-design reader is exempt from TAINT too, not just from read
                # sites. It legitimately iterates the key-name globs and matches paths
                # against them, so letting its locals (`pat`, `lower`, `f`) become
                # tainted poisons every same-named variable elsewhere in the file.
                if id(stmt) in _skip:
                    continue
                if (isinstance(stmt, ast.Assign) and isinstance(stmt.value, ast.Lambda)
                      and any(isinstance(tg, ast.Name) for tg in stmt.targets)):
                    # `load = lambda p: p.read_text()` is a def by another spelling
                    name = next(tg.id for tg in stmt.targets if isinstance(tg, ast.Name))
                    lam = stmt.value
                    if any(_arg_keyish(a) for call in ast.walk(tree)
                           if isinstance(call, ast.Call) and _callee(call) == name
                           for a in list(call.args) + [k.value for k in call.keywords]):
                        for arg in list(lam.args.args) + list(lam.args.kwonlyargs):
                            tainted.add(arg.arg)
                elif isinstance(stmt, ast.Assign):
                    _bind(stmt.targets, stmt.value)
                elif isinstance(stmt, ast.AnnAssign) and stmt.value is not None:
                    _bind([stmt.target], stmt.value)
                elif isinstance(stmt, (ast.For, ast.AsyncFor)):
                    # `for p in ROOT.rglob("*.key")` and `for c in CANDS`
                    _bind([stmt.target], stmt.iter)
                elif isinstance(stmt, (ast.comprehension,)):
                    _bind([stmt.target], stmt.iter)
                elif isinstance(stmt, ast.Compare):
                    # Any suffix test taints the thing being tested, whichever side the
                    # literal is on: `p.suffix == ".key"`, `".key" in p.name`,
                    # `p.suffix in {".key", ".pem"}`. _fold sees through neither a Set
                    # nor a List, so walk every constant in the comparison.
                    # _arg_keyish, not a constants-only test: the key-ish side is often
                    # a module constant (`if p.name == KEYNAME`), which is the plainest
                    # accidental shape there is -- this file's own comment calls a
                    # module-level path constant the likeliest reintroduction.
                    # Taint only the sides that are NOT already key-ish, and judge a
                    # side key-ish by a literal OR by being exactly a tainted name --
                    # never by "contains a tainted name somewhere", which taints both
                    # sides of every comparison and cascades until nothing is clean.
                    sides = [stmt.left] + list(stmt.comparators)
                    known = [s for s in sides if _side_keyish(s)]
                    if known and len(known) < len(sides):
                        for s in sides:
                            if s in known:
                                continue
                            root = _root_name(s)
                            if root is not None:
                                tainted.add(root.id)
                elif (isinstance(stmt, ast.Call)
                      and isinstance(stmt.func, ast.Attribute)
                      and stmt.func.attr in ("endswith", "startswith", "match",
                                             "fnmatch", "glob", "rglob")
                      and any(_side_keyish(a) for a in stmt.args)):
                    # `p.name.endswith(".key")`, `p.match("*.key")` -- the latter is the
                    # idiom find_plaintext_keys itself uses, so it is the likeliest
                    # shape anyone here would write.
                    root = _root_name(stmt.func.value)
                    if root is not None:
                        tainted.add(root.id)
                elif isinstance(stmt, ast.AugAssign):
                    # `K = ROOT` then `K /= "gpt.key"` -- the pathlib spelling of
                    # `KEYFILE = "gpt.key"`, which is already a probe
                    _bind([stmt.target], stmt.value)
                elif isinstance(stmt, ast.NamedExpr):
                    # `if (P := ROOT / "gpt.key"):` binds inside a test expression
                    _bind([stmt.target], stmt.value)
                elif isinstance(stmt, (ast.With, ast.AsyncWith)):
                    # `with open("gpt.key") as f:` -- the most idiomatic file read there
                    # is, and the literal lives only in the header
                    for item in stmt.items:
                        if item.optional_vars is not None:
                            _bind([item.optional_vars], item.context_expr)
                elif isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    # A helper taints its parameters when any CALL SITE passes a
                    # key-ish literal -- positionally, by keyword, or as a default.
                    args = stmt.args
                    passed = any(
                        _arg_keyish(a)
                        for call in ast.walk(tree)
                        if isinstance(call, ast.Call) and _callee(call) == stmt.name
                        for a in list(call.args) + [k.value for k in call.keywords])
                    if passed or any(_keyish(_fold(d)) for d in args.defaults
                                     if d is not None):
                        for arg in list(args.args) + list(args.kwonlyargs):
                            tainted.add(arg.arg)
                    # ...and the helper's NAME is tainted if it RETURNS something
                    # key-ish: `def _kf(): return ROOT / "gpt.key"` then
                    # `_kf().read_text()` is the idiomatic accessor shape here.
                    for node in ast.walk(stmt):
                        if isinstance(node, ast.Return) and node.value is not None:
                            if any(_keyish(_fold(n)) for n in ast.walk(node.value)
                                   if isinstance(n, (ast.Constant, ast.BinOp))) or any(
                                   isinstance(n, ast.Name) and n.id in tainted
                                   for n in ast.walk(node.value)):
                                tainted.add(stmt.name)
            if len(tainted) == before:
                break
        for stmt in ast.walk(tree):
            # SIMPLE statements only. A compound one (if/try/def) contains its whole
            # body, so an enclosing block pairs an unrelated message with an unrelated
            # read and reports a leak that is neither.
            # Simple statements, plus `for` HEADERS -- header only. A loop body is
            # walked as its own statements, and unparsing the For node would drag the
            # whole body in, which is how an unrelated message once paired with an
            # unrelated read. `for p in ROOT.rglob("*.key")` sets the taint; the body's
            # `p.read_text()` is then caught on its own line.
            if id(stmt) in _skip:
                continue
            if isinstance(stmt, (ast.For, ast.AsyncFor)):
                stmt = ast.Module(body=[ast.Expr(value=stmt.target),
                                        ast.Expr(value=stmt.iter)], type_ignores=[])
            elif isinstance(stmt, (ast.With, ast.AsyncWith)):
                stmt = ast.Module(type_ignores=[], body=[
                    ast.Expr(value=i.context_expr) for i in stmt.items])
            elif isinstance(stmt, ast.Lambda):
                # A lambda's body is an EXPRESSION, so it is never visited as a
                # statement -- `load = lambda p: p.read_text()` tainted its parameter
                # and the read still went unseen. Scan the body on its own.
                stmt = ast.Module(body=[ast.Expr(value=stmt.body)], type_ignores=[])
            elif isinstance(stmt, (ast.If, ast.While)):
                # `if open("gpt.key").read():` -- the test is a read, and the body is
                # walked separately. Third time this class appeared: for, with, now if.
                stmt = ast.Module(body=[ast.Expr(value=stmt.test)], type_ignores=[])
            elif not isinstance(stmt, ast.stmt) or hasattr(stmt, "body"):
                continue
            lits = [s for s in (_fold(n) for n in ast.walk(stmt)
                                if isinstance(n, (ast.Constant, ast.BinOp)))
                    if _keyish(s)]
            hits = {n.id for n in ast.walk(stmt)
                    if isinstance(n, ast.Name) and n.id in tainted}
            hits |= {n.attr for n in ast.walk(stmt)
                     if isinstance(n, ast.Attribute) and n.attr in tainted}
            if not lits and not hits:
                continue
            lits = lits or [f"<{sorted(hits)[0]}>"]
            # Look for a read in the CODE, never in the statement's text: a message
            # saying "ask the user to run: ..." is not a subprocess.run, and matching
            # text flagged nine of gen.py's own error strings.
            called = {n.attr for n in ast.walk(stmt) if isinstance(n, ast.Attribute)}
            called |= {n.id for n in ast.walk(stmt) if isinstance(n, ast.Name)}
            idx = any(_keyish(_fold(n.slice))
                      or (isinstance(n.slice, ast.Name) and n.slice.id in tainted)
                      for n in ast.walk(stmt) if isinstance(n, ast.Subscript))
            if idx or called & set(READISH):
                out.append(f"{sorted(set(lits))[0][:60]!r} in a reading statement")
        return out

    probes = {
        'k = sorted(ROOT.glob("*.key"))[0].read_text()': True,
        'k = open("gpt." + "key").read()': True,
        'e = os.environ\nk = e["OPENAI_API_KEY"]': True,
        'k = os.environb[b"OPENAI_API_KEY"].decode()': True,
        'k = Path("gpt.KEY").read_text()': True,
        'k = subprocess.run(["cat"] + [str(p) for p in ROOT.glob("*.key")]).stdout': True,
        'k = open(".api-key.pem").read()': True,
        'k = getattr(os, "envi" + "ron")["OPENAI_API_KEY"]': True,
        'k = os.environ["OPENAI_API_KEY"]': True,
        'plain = sorted(p.name for p in ROOT.glob("*.key"))': False,
        'd = os.environ.get("TMPDIR", "/tmp")': False,
        'ap.add_argument("--key-fd", type=int, help="fd to read the key from")': False,
        # gen.py's own prose: mentions a key AND the word "run", but reads nothing
        'raise Fail("no key. Ask the user to run: ! python3 -I bin/unlock.py")': False,
        'parser.add_argument("--key-fd", help="never pass this; it is unlock.py\'s")': False,
        # prose mentioning tokens, in the same statement as a read of an IMAGE
        'return src.read_bytes(), f"codex source {src}; tokens used {n}"': False,
        # two-statement reads: the likeliest reintroduction, invisible to any
        # single-statement check
        'KEYFILE = "gpt.key"\nk = open(KEYFILE).read()': True,
        'KEY = ROOT / "gpt.key"\nk = KEY.read_text()': True,
        'NAME = "OPENAI_API_KEY"\nk = os.environ[NAME]': True,
        # the guard's own glob assigns a key-ish literal, then only reads NAMES
        'plain = sorted(p.name for p in ROOT.glob("*.key"))\nmsg = ", ".join(plain)': False,
        # loop targets, and shell strings whose whitespace used to nullify the check
        'for p in ROOT.rglob("*.key"):\n    blob = p.read_text()': True,
        'CANDS = ["gpt.key"]\nfor c in CANDS:\n    k = open(c).read()': True,
        'k = os.popen("cat gpt.key").read()': True,
        'k = subprocess.run("cat gpt.key", shell=True).stdout': True,
        'for f in ROOT.rglob("*.png"):\n    img = f.read_bytes()': False,
        # `with` headers, and a one-line helper taking a key-ish literal
        'with open("gpt.key") as f:\n    k = f.read()': True,
        'with open("gpt.key") as f, open("x") as g:\n    k = f.read()': True,
        'def _load(p):\n    return p.read_text()\nk = _load("gpt.key")': True,
        'with open("scene.png", "rb") as f:\n    img = f.read()': False,
        # helper return values, defaults, keyword args, class attributes
        'def _kf():\n    return ROOT / "gpt.key"\nk = _kf().read_text()': True,
        'def _load(p="gpt.key"):\n    return open(p).read()': True,
        'def _load(p):\n    return open(p).read()\nk = _load(p="gpt.key")': True,
        'class C:\n    f = "gpt.key"\nk = open(C.f).read()': True,
        # a helper returning an ordinary path must NOT taint
        'def _out():\n    return ROOT / "deliverable.png"\nd = _out().read_bytes()': False,
        # if/while test expressions, and walrus bindings inside them
        'if (k := open("gpt.key").read()):\n    pass': True,
        'while (k := open("gpt.key").readline()):\n    pass': True,
        'if open("gpt.key").read().startswith("sk-"):\n    pass': True,
        'if (P := ROOT / "gpt.key"):\n    k = P.read_text()': True,
        'if (img := open("scene.png", "rb").read()):\n    pass': False,
        # the by-design exemption must not become a hiding place
        'def helper():\n    def find_plaintext_keys(p):\n        return open("gpt.key").read()': True,
        'def find_plaintext_keys(r):\n    return []\ndef find_plaintext_keys(r):\n    return open("gpt.key").read()': True,
        'class C:\n    def find_plaintext_keys(self):\n        return open("gpt.key").read()': True,
        'def find_plaintext_keys(r):\n    def inner():\n        return open("gpt.key").read()\n    return inner()': True,
        # the native path idiom reaching a helper, and taint through a comparison
        'def _load(p):\n    return p.read_text()\nk = _load(ROOT / "gpt.key")': True,
        'KEY = ROOT / "gpt.key"\ndef _load(p):\n    return p.read_text()\nk = _load(KEY)': True,
        'def _load(p):\n    return p.read_text()\nk = _load(f"{ROOT}/gpt.key")': True,
        'for p in ROOT.iterdir():\n    if p.suffix == ".key":\n        k = p.read_text()': True,
        'def _load(p):\n    return p.read_text()\nd = _load(ROOT / "deliverable.png")': False,
        # suffix tests other than ==, including the idiom find_plaintext_keys uses
        'for p in ROOT.iterdir():\n    if p.suffix in {".key", ".pem"}:\n        k = p.read_text()': True,
        'for p in ROOT.iterdir():\n    if p.name.endswith(".key"):\n        k = p.read_text()': True,
        'for p in ROOT.iterdir():\n    if ".key" in p.name:\n        k = p.read_text()': True,
        'for p in ROOT.iterdir():\n    if p.match("*.key"):\n        k = p.read_text()': True,
        # a method or lambda helper, not only a bare function
        'class C:\n    def _load(self, p):\n        return p.read_text()\nk = C()._load(ROOT / "gpt.key")': True,
        'load = lambda p: p.read_text()\nk = load(ROOT / "gpt.key")': True,
        # bare read()/get() reaching a key
        'cfg.read(ROOT / "gpt.key")': True,
        'E = os.environ\nk = E.get("OPENAI_API_KEY")': True,
        # and the same shapes on ordinary files must stay clean
        'for p in ROOT.iterdir():\n    if p.suffix == ".png":\n        img = p.read_bytes()': False,
        'for p in ROOT.iterdir():\n    if p.name.endswith(".png"):\n        img = p.read_bytes()': False,
        # the pathlib /= spelling, and copying a key rather than reading it
        'K = ROOT\nK /= "gpt.key"\nk = K.read_text()': True,
        'shutil.copy(ROOT / "gpt.key", tmp)': True,
        # absolute paths: the house idiom here, and a whole-string length cap hid them
        'k = open("/Users/x/projects/rf/gm/image_generation/gpt.key").read()': True,
        'KEYFILE = "/Users/x/projects/rf/gm/image_generation/gpt.key"\nk = open(KEYFILE).read()': True,
        'd = open("/Users/x/projects/rf/gm/image_generation/outputs/s/v001/image.png").read()': False,
        # multi-token shell reads: a "prose by token count" rule hid all five of these
        'os.system("cp gpt.key /tmp/k && chmod 600 /tmp/k")': True,
        'k = os.popen("cat gpt.key | tr -d chars").read()': True,
        'k = subprocess.run("cat gpt.key > /tmp/k", shell=True).stdout': True,
        'k = os.popen("head -c 200 gpt.key").read()': True,
        'k = os.popen("openssl enc -d -in gpt.key").read()': True,
        'os.system("cp scene.png /tmp/s && chmod 600 /tmp/s")': False,
        # the API's own usage fields, which honest cost reporting would read
        'n = usage.get("input_tokens", 0)': False,
        'total = usage["total_tokens"]': False,
        'cost = usage["input_tokens"] * rate + usage["output_tokens"] * out_rate': False,
        'k = cfg["tokens_secret"]': True,
        'k = open("tokens_keyfile").read()': True,
        # the key-ish side of a test being a module constant rather than a literal
        'KEYNAME = "gpt.key"\nfor p in ROOT.iterdir():\n    if p.name == KEYNAME:\n        k = p.read_text()': True,
        'KEYS = ("gpt.key", "api.key")\nfor p in ROOT.iterdir():\n    if p.name in KEYS:\n        k = p.read_text()': True,
        'KEYNAME = "gpt.key"\nfor p in ROOT.iterdir():\n    if KEYNAME in str(p):\n        k = p.read_text()': True,
        'KEYNAME = "gpt.key"\nfor p in ROOT.iterdir():\n    if p.name.endswith(KEYNAME):\n        k = p.read_text()': True,
        'PNG = ".png"\nfor p in ROOT.iterdir():\n    if p.suffix == PNG:\n        img = p.read_bytes()': False,
    }
    blind = [s for s, want in probes.items() if bool(key_reads(s)) != want]
    print(f"  [{'ok ' if not blind else 'FAIL'}] the key-read detector catches its "
          f"{sum(probes.values())} known bypasses")
    failures += 1 if blind else 0
    for b in blind:
        print(f"         blind to: {b}")

    leak = key_reads((ROOT / "bin" / "gen.py").read_text())
    print(f"  [{'ok ' if not leak else 'FAIL'}] gen.py has no obvious key read"
          + (f" — found {leak}" if leak else ""))
    failures += 1 if leak else 0

    # The Style Block must not have swallowed a neighbouring section. This shipped
    # 188 extra words to the model for 39 generations before anyone ran the extractor.
    import importlib.util
    spec = importlib.util.spec_from_file_location("_g", ROOT / "bin" / "gen.py")
    _g = importlib.util.module_from_spec(spec); spec.loader.exec_module(_g)
    try:
        blk = _g.style_block()
        clean = "##" not in blk
    except Exception:
        clean = False
    print(f"  [{'ok ' if clean else 'FAIL'}] Style Block extract carries no foreign section")
    failures += 0 if clean else 1

    # Is the paid-call gate actually ARMED? gen.py holding no key is necessary but
    # not sufficient: a plaintext key anywhere in the vault is a live bypass, and
    # without .api-key.enc the approval path cannot run at all. Reported, not
    # failed — it is vault state the user must act on, not a code defect.
    # Must be gen.py's own search, not a weaker glob: with tmp/k.txt holding a key,
    # ROOT.glob("*.key") returns nothing and this printed "gate is armed" while gen.py
    # would have refused --key-fd. The check that vouches for the gate has to be at
    # least as thorough as the gate.
    enc = ROOT / ".api-key.enc"
    plain = [ROOT / n for n in _gen.find_plaintext_keys(ROOT)]
    if plain:
        print(f"  [WARN] gate is DECORATIVE: plaintext key present "
              f"({', '.join(str(p.relative_to(ROOT)) for p in plain)}) — "
              f"anything can read it")
    if not enc.exists():
        print("  [WARN] no .api-key.enc — bin/unlock.py cannot run, so the approval "
              "path is dead")
    if not plain and enc.exists():
        print("  [ok ] paid-call gate is armed (key sealed, no plaintext in vault)")

    # and no stale bytecode, which would be an ungated copy
    cache = list((ROOT / "bin").glob("__pycache__/gen*.pyc"))
    print(f"  [{'ok ' if not cache else 'FAIL'}] no ungated gen bytecode in __pycache__")
    failures += 1 if cache else 0

    # gen.py checks the ANCHOR IMAGE against its frozen copy but nothing checked the
    # style TEXT. They had already drifted: live style.md carried a masked closing line
    # that frozen style-v2.md never had, so a masked receipt would stamp a version whose
    # frozen copy lacks the line it used -- unreproducible.
    import re as _re2_pre
    _sv = ROOT / "style_versions" / f"style-v{_gen.style_version()}.md"
    if not _sv.exists():
        print(f"  [FAIL] style.md says v{_gen.style_version()} but {_sv.name} is missing")
        failures += 1
    else:
        # de-blockquote the frozen copy the same way style_block() does, or every
        # comparison fails on the "> " markers rather than on real drift
        _frozen = _re2_pre.sub(r"^>\s?", "", _sv.read_text(), flags=_re2_pre.M)
        _want = [("Style Block", _gen.style_block())]
        _re2 = _re2_pre
        for _m in _re2.finditer(r"^> (Render everything in the exact brush scale[^\n]*(?:\n> [^\n]*)*)",
                              (ROOT / "style.md").read_text(), _re2.M):
            _want.append(("closing line", _re2.sub(r"\n> ", " ", _m.group(1))))
        _drift = [lbl for lbl, txt in _want
                  if " ".join(txt.split()) not in " ".join(_frozen.split())]
        print(f"  [{'ok ' if not _drift else 'FAIL'}] live style text is present in "
              f"{_sv.name} ({len(_want)} parts checked)")
        for d in _drift:
            print(f"         {d} in style.md is absent from {_sv.name}")
        failures += 1 if _drift else 0

    # rules.md describes find_plaintext_keys' coverage. A one-directional check caught
    # a glob missing from the doc but not a doc claiming a pattern the code lacks, nor a
    # skip-list or size figure that drifted -- so a doc-side OVERCLAIM passed clean,
    # which is the more dangerous direction: it tells a reader they are covered.
    _doc = (ROOT / "rules.md").read_text()
    _drift = []
    # Scope the comparison to the table ROW that makes the claim. Checking the whole
    # file let two mutations pass: an added pattern the regex did not recognise, and a
    # dropped "under 1 MB" that still appeared in the Missed row.
    _found_row = ""
    for line in _doc.splitlines():
        if line.startswith("| **Found**"):
            _found_row = line
    if not _found_row:
        _drift.append("rules.md has no | **Found** | row describing the key search")
    else:
        _globs = set(_gen.PLAINTEXT_KEY_GLOBS)
        # any backticked token that looks like a filename pattern
        _doc_globs = set(_re_top.findall(r"`(\*[A-Za-z0-9.*_-]+)`", _found_row))
        for g in sorted(_globs - _doc_globs):
            _drift.append(f"{g} is in PLAINTEXT_KEY_GLOBS but not in the Found row")
        for g in sorted(_doc_globs - _globs):
            _drift.append(f"the Found row claims pattern {g}, which the code does not match")
        if "under 1 MB" not in _found_row:
            _drift.append("the Found row no longer states the 'under 1 MB' sniff limit")
        _fn = (ROOT / "bin" / "gen.py").read_text()
        if "1_000_000" not in _fn:
            _drift.append("gen.py's 1 MB limit changed; the Found row still says 1 MB")
        for d in (".git", "__pycache__", "node_modules", ".obsidian"):
            if f"`{d}`" not in _found_row:
                _drift.append(f"skip dir {d} is in the code but not named in the Found row")
        if "case-insensitiv" in _found_row.lower() and "lower()" not in _fn:
            _drift.append("the Found row claims case-insensitive matching; the code does not")

    # The Missed row was unverified, so a doc-side overclaim there passed silently --
    # and that row is the one a reader consults to decide what is NOT covered.
    _missed_row = ""
    for line in _doc.splitlines():
        if line.startswith("| **Missed**"):
            _missed_row = line
    if not _missed_row:
        _drift.append("rules.md has no | **Missed** | row")
    else:
        _fn2 = (ROOT / "bin" / "gen.py").read_text()
        # each documented miss must correspond to something the code actually skips
        if "binary" in _missed_row and "BINARY_SUFFIXES" not in _fn2:
            _drift.append("Missed claims binaries are skipped; BINARY_SUFFIXES is gone")
        if "1 MB" in _missed_row and "1_000_000" not in _fn2:
            _drift.append("Missed claims a 1 MB limit; the code no longer has one")
        if "skipped subtree" in _missed_row and "slow =" not in _fn2:
            _drift.append("Missed claims skipped subtrees; the code no longer skips any")
        if "auth.json" not in _missed_row:
            _drift.append("Missed no longer names ~/.codex/auth.json as out of scope")
        if "outside" not in _missed_row:
            _drift.append("Missed no longer states the search is bounded to the vault")
    ok = not _drift
    print(f"  [{'ok ' if ok else 'FAIL'}] rules.md's key-search description matches the code")
    for d in _drift:
        print(f"         {d}")
    failures += 0 if ok else 1

    # image-surgery quotes a recoverability census (how many candidates git can
    # restore, how many have a live codex source). Those numbers move every time a
    # candidate is generated or committed, and a stale one sends an agent past a free
    # byte-exact recovery. Recompute and compare.
    import re as _re
    SKILL = ROOT.parent.parent / ".claude" / "skills" / "image-surgery" / "SKILL.md"
    if SKILL.exists():
        # Images now live outside this repo, so git recovery is a question about whichever
        # repo CONTAINS them -- not this one. Ask that repo, and note that a receipt
        # (generation.md, still here) and its image can now be tracked separately.
        IMG = _gen.IMAGES
        cands = sorted(IMG.glob("outputs/*/v[0-9][0-9][0-9]/image.png")) + \
                sorted(IMG.glob("assets/*/*/candidates/v[0-9][0-9][0-9]/image.png"))
        img_repo = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=IMG,
                                  capture_output=True, text=True).stdout.strip()
        tracked, rel = set(), {}
        if img_repo:
            base = Path(img_repo)
            rel = {p: str(p.relative_to(base)) for p in cands}
            tracked = set(subprocess.run(
                ["git", "ls-files", "--full-name", "--"] + [str(p) for p in cands],
                cwd=IMG, capture_output=True, text=True).stdout.split())
        n_git = sum(1 for p in cands if rel.get(p) in tracked)
        n_codex = n_live = 0
        for p in cands:
            rec = ROOT / p.relative_to(IMG).parent / "generation.md"
            if not rec.exists():
                continue
            m = _re.search(r"codex source (/\S+?\.png)", rec.read_text())
            if m:
                n_codex += 1
                n_live += Path(m.group(1)).exists()
        union = 0
        for p in cands:
            rec = ROOT / p.relative_to(IMG).parent / "generation.md"
            has = rec.exists() and _re.search(r"codex source (/\S+?\.png)", rec.read_text())
            union += bool(has) or rel.get(p) in tracked
        doc = SKILL.read_text()
        want = {"tracked": n_git, "codex": n_codex, "total": len(cands),
                "union": union, "lost": len(cands) - union}
        claims = {
            "tracked": _re.search(r"\((\d+) of (\d+) are\)", doc),
            "codex":   _re.search(r"\((\d+) of (\d+) do; all (\d+) still resolve\)", doc),
            "union":   _re.search(r"Union: (\d+)", doc),
            "lost":    _re.search(r"other (\d+) cannot be recovered", doc),
        }
        drift = []
        if claims["tracked"] and (int(claims["tracked"].group(1)) != n_git
                                  or int(claims["tracked"].group(2)) != len(cands)):
            drift.append(f"git-tracked: doc says {claims['tracked'].group(1)} of "
                         f"{claims['tracked'].group(2)}, actual {n_git} of {len(cands)}")
        if claims["codex"]:
            d1, d2, d3 = (int(x) for x in claims["codex"].groups())
            if (d1, d2, d3) != (n_codex, len(cands), n_live):
                drift.append(f"codex source: doc says {d1} of {d2}, {d3} resolve; "
                             f"actual {n_codex} of {len(cands)}, {n_live} resolve")
        if claims["union"] and int(claims["union"].group(1)) != union:
            drift.append(f"union: doc says {claims['union'].group(1)}, actual {union}")
        if claims["lost"] and int(claims["lost"].group(1)) != len(cands) - union:
            drift.append(f"unrecoverable: doc says {claims['lost'].group(1)}, "
                         f"actual {len(cands) - union}")
        print(f"  [{'ok ' if not drift else 'FAIL'}] image-surgery's recoverability "
              f"census matches the vault")
        for d in drift:
            print(f"         {d}")
        failures += 1 if drift else 0

    # rules.md and prompt.py both claim the standard role wording comes from
    # rules.md. STYLE and IDENTITY matched; EDIT TARGET's sentence existed only in
    # prompt.py, so an agent hand-writing the role from rules.md wrote different text.
    import importlib.util as _ilu
    _spec = _ilu.spec_from_file_location("_pr", ROOT / "bin" / "prompt.py")
    _pr = _ilu.module_from_spec(_spec)
    try:
        _spec.loader.exec_module(_pr)
    except SystemExit:
        pass
    _rules = (ROOT / "rules.md").read_text()
    _norm = lambda s: " ".join(s.split()).replace("\u2019", "'")
    missing = [role for role, text in getattr(_pr, "STANDARD", {}).items()
               if _norm(text) not in _norm(_rules)]
    print(f"  [{'ok ' if not missing else 'FAIL'}] prompt.py's standard role wording "
          f"appears verbatim in rules.md")
    for m in missing:
        print(f"         {m} wording is in prompt.py but not rules.md")
    failures += 1 if missing else 0

    # find_plaintext_keys is duplicated in gen.py and unlock.py by necessity (neither
    # imports the other). Duplicated security code that drifts is worse than none.
    def _fn_src(path, name):
        tree = ast.parse(path.read_text())
        for n in ast.walk(tree):
            if isinstance(n, ast.FunctionDef) and n.name == name:
                return ast.unparse(n)
        return None
    a = _fn_src(ROOT / "bin" / "gen.py", "find_plaintext_keys")
    b = _fn_src(ROOT / "bin" / "unlock.py", "find_plaintext_keys")
    # The function body alone is not the search: it reads three module constants, and
    # adding a pattern to one file is the likeliest innocent edit here. Widening
    # gen.py's PLAINTEXT_KEY_GLOBS while leaving unlock.py's alone left unlock's search
    # weaker with no signal at all, so compare the constants too.
    def _const_src(path, names):
        tree = ast.parse(path.read_text())
        out = {}
        for n in tree.body:
            if isinstance(n, ast.Assign):
                for tg in n.targets:
                    if isinstance(tg, ast.Name) and tg.id in names:
                        out[tg.id] = ast.unparse(n.value)
        return out
    CONSTS = {"PLAINTEXT_KEY_GLOBS", "KEY_RE", "BINARY_SUFFIXES"}
    ca = _const_src(ROOT / "bin" / "gen.py", CONSTS)
    cb = _const_src(ROOT / "bin" / "unlock.py", CONSTS)
    diff = sorted(CONSTS - set(ca)) + sorted(CONSTS - set(cb))
    diff += sorted(k for k in CONSTS & set(ca) & set(cb) if ca[k] != cb[k])
    same = a is not None and a == b and not diff
    print(f"  [{'ok ' if same else 'FAIL'}] find_plaintext_keys and its constants are "
          f"identical in gen.py and unlock.py")
    if a != b:
        print("         the function bodies differ")
    for d in sorted(set(diff)):
        print(f"         {d} differs or is missing in one file")
    failures += 0 if same else 1

    # rules.md's model table is prose that goes stale the moment a model dies. The
    # table said "three dead models" above a list of five for a day. Compare it to
    # the only authority, gen.py's own constants.
    import re
    rules = (ROOT / "rules.md").read_text()
    documented = {m.group(1): "yes" in m.group(2).lower()
                  for m in re.finditer(r"^\| `([a-z0-9.\-]+)` \| (.*?) \|", rules, re.M)}
    sys.path.insert(0, str(ROOT / "bin"))
    import importlib.util
    spec = importlib.util.spec_from_file_location("gen_const", ROOT / "bin" / "gen.py")
    gen = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gen)
    actual = {m: False for m in gen.CODEX_MODELS_BROKEN} | {m: True for m in gen.CODEX_MODELS_OK}
    drift = [f"{m}: table says {'works' if documented.get(m) else 'dead/absent'}, "
             f"gen.py says {'works' if ok else 'dead'}"
             for m, ok in actual.items() if documented.get(m) != ok]
    drift += [f"{m}: in rules.md's table but in neither gen.py constant"
              for m in documented if m not in actual]
    # (A counted-prose check lived here. rules.md now says "every dead model is in
    # CODEX_MODELS_BROKEN" with no number, so there is no count to contradict -- the
    # right outcome, since a hand-maintained count was the bug this guard first caught.)
    print(f"  [{'ok ' if not drift else 'FAIL'}] rules.md's model table matches gen.py")
    for d in drift:
        print(f"         {d}")
    failures += 1 if drift else 0

    for f in tmp.iterdir():
        f.unlink()
    tmp.rmdir()
    for leftover in (ROOT / "tmp").glob("api-mask-*.png"):
        leftover.unlink()

    # The total is DERIVED from the checks that actually ran, so it legitimately varies
    # with vault state: the --key-fd case only runs while a plaintext key exists, and the
    # "gate is armed" line only prints when none does. They happen to cancel today. Treat
    # the left number matching the right as the pass condition, never a fixed count.
    print(f"\n  {_checks[0] - failures}/{_checks[0]} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
