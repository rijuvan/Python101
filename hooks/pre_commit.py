"""
Pre-commit hook: runs tests before allowing a commit.
Place a call to this script in .git/hooks/pre-commit to use it.
"""
import subprocess
import sys


def run_tests():
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print("Tests failed — commit blocked.\n")
        print(result.stderr)
        sys.exit(1)
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
