"""
build_notebook_index.py

Optional helper script: scan notebooks/core/* and print a simple list
you can paste into docs/notebook-index.md.

You can extend this later to auto-generate the table.
"""

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
nb_root = ROOT / "notebooks" / "core"

def main():
    print("# Detected notebooks\n")
    for repo_dir in sorted(nb_root.glob("*")):
        if not repo_dir.is_dir():
            continue
        for nb in sorted(repo_dir.glob("*.ipynb")):
            rel = nb.relative_to(ROOT)
            print(f"- {rel}")

if __name__ == "__main__":
    main()
