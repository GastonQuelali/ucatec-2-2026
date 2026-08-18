#!/usr/bin/env python3
"""
Genera presentacion.pptx (y opcionalmente presentacion.pdf) a partir de
presentacion.md usando Marp CLI.

Requisitos:
    npm install -g @marp-team/marp-cli

Uso:
    python3 generate_pptx.py --all
    python3 generate_pptx.py --all --pdf
    python3 generate_pptx.py --base ../prog-avanzada --all
    python3 generate_pptx.py 00_introduccion_erp
"""

import shutil
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
MARP_BIN = "marp"
_marp_path = None


def _check_marp():
    global _marp_path
    _marp_path = shutil.which(MARP_BIN)
    if _marp_path is None:
        print(
            "Error: marp CLI no encontrado en PATH.\n"
            "Instalar con:  npm install -g @marp-team/marp-cli",
            file=sys.stderr,
        )
        sys.exit(1)


def find_presentations(base_dir: Path):
    themes = sorted(
        d for d in base_dir.iterdir()
        if d.is_dir() and d.name[0:2].isdigit()
    )
    found = []
    for theme_dir in themes:
        md = theme_dir / "presentacion.md"
        if md.exists():
            found.append((theme_dir.name, md))
        else:
            print(f"  Saltando {theme_dir.name}: no existe presentacion.md",
                  file=sys.stderr)
    return found


def convert_one(md_path: Path, also_pdf: bool) -> bool:
    pptx_out = md_path.parent / "presentacion.pptx"

    cmd_pptx = [_marp_path, str(md_path), "--allow-local-files", "--pptx"]
    print(f"  Convirtiendo {md_path.parent.name}/presentacion.md -> .pptx ...")
    result = subprocess.run(cmd_pptx, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"  ERROR en {md_path.parent.name}: {result.stderr.strip()}",
              file=sys.stderr)
        return False

    print(f"  OK: {pptx_out.name}")

    if also_pdf:
        pdf_out = md_path.parent / "presentacion.pdf"
        cmd_pdf = [_marp_path, str(md_path), "--allow-local-files", "--pdf"]
        result = subprocess.run(cmd_pdf, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  ERROR (PDF) en {md_path.parent.name}: "
                  f"{result.stderr.strip()}", file=sys.stderr)
            return False
        print(f"  OK: {pdf_out.name}")

    return True


def main():
    base_dir = SCRIPT_DIR
    also_pdf = False
    args = sys.argv[1:]

    if "--pdf" in args:
        also_pdf = True
        args.remove("--pdf")

    if len(args) >= 2 and args[0] == "--base":
        base_dir = Path(args[1])
        args = args[2:]

    if len(args) < 1:
        print(
            "Uso: python3 generate_pptx.py [--base DIR] [--pdf] <tema> | --all",
            file=sys.stderr,
        )
        sys.exit(1)

    _check_marp()

    arg = args[0]

    if arg == "--all":
        presentations = find_presentations(base_dir)
        if not presentations:
            print("No se encontraron presentaciones", file=sys.stderr)
            sys.exit(1)
        print(f"Convirtiendo {len(presentations)} presentaciones...")
    else:
        theme_dir = base_dir / arg
        md = theme_dir / "presentacion.md"
        if not md.exists():
            print(f"Error: no existe {md}", file=sys.stderr)
            sys.exit(1)
        presentations = [(arg, md)]

    ok = 0
    fail = 0
    for name, md in presentations:
        if convert_one(md, also_pdf):
            ok += 1
        else:
            fail += 1

    print(f"\nListo: {ok} generadas, {fail} errores")
    if fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
