#!/usr/bin/env python3
"""
Code Fixer Agent — scans Python files and fixes errors using the OpenAI API.

Usage:
    python agent/code_fixer.py [--dir PATH] [--dry-run]

Environment:
    OPENAI_API_KEY — loaded from env/.env (never commit that file)
"""

import argparse
import glob
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

# Load env/.env relative to this script's parent directory
_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(_root, "env", ".env"))


def scan_python_files(directory: str) -> list:
    pattern = os.path.join(directory, "**", "*.py")
    return sorted(glob.glob(pattern, recursive=True))


def build_prompt(file_path: str, code: str) -> str:
    return (
        f"File: {os.path.basename(file_path)}\n\n"
        f"{code}"
    )


def strip_markdown(code: str) -> str:
    lines = code.splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "\n".join(lines).strip()


def fix_file(client: OpenAI, file_path: str) -> tuple:
    with open(file_path, "r", encoding="utf-8") as f:
        original = f.read()

    if not original.strip():
        return original, original

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a Python expert. Analyze the code for any issues:\n"
                    "- Syntax errors\n"
                    "- Runtime errors or unhandled exceptions\n"
                    "- Logic bugs\n"
                    "- Incorrect imports or missing dependencies\n"
                    "- Bad practices that would cause failures\n\n"
                    "Return ONLY the corrected Python source code — no markdown fences, "
                    "no explanations, no extra text. If the code has no errors, return it unchanged."
                ),
            },
            {
                "role": "user",
                "content": build_prompt(file_path, original),
            },
        ],
    )

    fixed = strip_markdown(response.choices[0].message.content.strip())
    return original, fixed


def main():
    parser = argparse.ArgumentParser(
        description="Fix Python files using OpenAI (gpt-4o)"
    )
    parser.add_argument(
        "--dir",
        default=None,
        help="Directory to scan (default: ../src relative to this script)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show which files would change without writing them",
    )
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.abspath(args.dir or os.path.join(script_dir, "..", "src"))

    if not os.path.isdir(src_dir):
        print(f"Error: directory not found: {src_dir}")
        sys.exit(1)

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable is not set.")
        sys.exit(1)

    mode = "[DRY-RUN] " if args.dry_run else ""
    print(f"{mode}Scanning Python files in: {src_dir}\n")

    files = scan_python_files(src_dir)
    if not files:
        print("No Python files found.")
        return

    client = OpenAI(api_key=api_key)

    changed = 0
    for file_path in files:
        rel = os.path.relpath(file_path, script_dir)
        print(f"  Processing: {rel}")
        try:
            original, fixed = fix_file(client, file_path)
            if original.strip() == fixed.strip():
                print("    No changes needed.")
            else:
                print("    Errors found and fixed.")
                if not args.dry_run:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(fixed + "\n")
                    print("    Saved.")
                else:
                    print("    (dry-run — file not written)")
                changed += 1
        except Exception as e:
            print(f"    Error: {e}")

    verb = "would be " if args.dry_run else ""
    print(f"\nDone. {changed} file(s) {verb}modified.")


if __name__ == "__main__":
    main()
