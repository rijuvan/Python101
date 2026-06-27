# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Structure

```
basic python/
├── src/                   # Source code modules
│   ├── __init__.py
│   └── hello_employee.py
├── tests/                 # Unit tests
│   ├── __init__.py
│   └── test_hello_employee.py
├── hooks/                 # Hook scripts (pre-commit, post-run, etc.)
│   ├── pre_commit.py
│   └── post_run.py
├── env/                   # Environment configuration
│   └── .env.example
├── requirements.txt
├── .gitignore
└── CLAUDE.md
```

## Running Code

```powershell
python src/hello_employee.py
```

## Running Tests

```powershell
python -m unittest discover -s tests
```

## Adding New Modules

Add new `.py` files under `src/` and their tests under `tests/`.

## Environment Setup

Copy `env/.env.example` to `env/.env` and fill in values. Create a virtual environment with:

```powershell
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

## Hooks

- `hooks/pre_commit.py` — runs tests; call from `.git/hooks/pre-commit` to block bad commits
- `hooks/post_run.py` — logs run status with a timestamp
