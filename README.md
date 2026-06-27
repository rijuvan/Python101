# Python101

A beginner Python project exploring object-oriented programming with `Employee` and `Manager` classes.

## Project Structure

```
basic python/
├── src/
│   └── hello_employee.py   # Employee and Manager classes
├── tests/
│   └── test_hello_employee.py
├── hooks/
│   ├── pre_commit.py       # Runs tests before commit
│   └── post_run.py         # Logs run status with timestamp
├── requirements.txt
└── CLAUDE.md
```

## Setup

```powershell
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

## Usage

```python
from src.hello_employee import Employee, Manager

emp = Employee("Alice", "Engineering", 70000)
print(emp.greet())        # Hi, I'm Alice from Engineering.
print(emp.give_raise(5000))  # Alice's new salary: $75000

mgr = Manager("Bob", "Engineering", 90000, team_size=5)
print(mgr.team_summary())  # Bob manages 5 people in Engineering.
```

## Running

```powershell
python src/hello_employee.py
```

## Tests

```powershell
python -m unittest discover -s tests -v
```

## Contributing

This is a personal learning project, but suggestions and improvements are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and add tests if applicable
4. Run the test suite: `python -m unittest discover -s tests -v`
5. Commit your changes: `git commit -m "Add your feature"`
6. Push to your fork: `git push origin feature/your-feature`
7. Open a Pull Request

Please make sure all tests pass before submitting a PR.

## License

This project is licensed under the [MIT License](LICENSE) — free to use for learning and personal purposes.  
Copyright (c) 2026 Rijuvan Ansari.

## .gitignore

The `.gitignore` covers common Python patterns:

- `__pycache__/`, `*.pyc`, `*.pyd` — compiled bytecode
- `env/`, `.venv/`, `venv/` — virtual environments
- `.env` — environment variable files
- `dist/`, `build/`, `*.egg-info/` — packaging artifacts
- `.coverage`, `htmlcov/`, `.pytest_cache/` — test and coverage outputs
- `.mypy_cache/`, `.ruff_cache/` — type checker and linter caches
- `.vscode/`, `.idea/` — IDE folders
- `.DS_Store`, `Thumbs.db` — OS-generated files
