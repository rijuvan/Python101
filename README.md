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
