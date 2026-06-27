class Employee:
    def __init__(self, name, department, salary, department_size=10):
        self.name = name
        self.department = department
        self.salary = salary
        self.department_size = department_size

    def greet(self):
        return f"Hi, I'm {self.name} from {self.department}."

    def give_raise(self, amount):
        self.salary += amount
        return f"{self.name}'s new salary: ${self.salary}"

    def __str__(self):
        return f"{self.name} | {self.department} | ${self.salary}"


class Manager(Employee):
    def __init__(self, name, department, salary, team_size=0):
        super().__init__(name, department, salary)
        self.team_size = team_size

    def team_summary(self):
        return f"{self.name} manages {self.team_size} people in {self.department}."


if __name__ == "__main__":
    print("Hello, World!")
    emp = Employee("Alice", "Engineering", 70000)
    print(emp.greet())
    print(emp.give_raise(5000))
