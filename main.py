#!/usr/bin/env python3
"""Warning label for humans: writes the entry text to /output/entry.txt (deterministic)."""
import os
import tempfile

TEXT = "WARNING: This human runs on caffeine and poor decisions. Do not shake. May start a podcast at any moment."
# Real printed-label wording (WARNING / Do not shake), recognition first, turn in the last words.

def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(TEXT)
        os.replace(tmp, target)
        os.chmod(target, 0o644)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise

if __name__ == "__main__":
    main()
