import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src'))

from hello_employee import Employee, Manager


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = Employee("Alice", "Engineering", 70000)

    def test_greet(self):
        self.assertEqual(self.emp.greet(), "Hi, I'm Alice from Engineering.")

    def test_give_raise(self):
        result = self.emp.give_raise(5000)
        self.assertEqual(self.emp.salary, 75000)
        self.assertIn("75000", result)

    def test_str(self):
        result = str(self.emp)
        self.assertIn("Alice", result)
        self.assertIn("Engineering", result)

    def test_default_department_size(self):
        self.assertEqual(self.emp.department_size, 10)

    def test_custom_department_size(self):
        emp = Employee("Bob", "HR", 60000, 5)
        self.assertEqual(emp.department_size, 5)


class TestManager(unittest.TestCase):
    def setUp(self):
        self.mgr = Manager("Bob", "Engineering", 90000, team_size=5)

    def test_inherits_greet(self):
        self.assertEqual(self.mgr.greet(), "Hi, I'm Bob from Engineering.")

    def test_inherits_give_raise(self):
        self.mgr.give_raise(10000)
        self.assertEqual(self.mgr.salary, 100000)

    def test_team_summary(self):
        self.assertEqual(self.mgr.team_summary(), "Bob manages 5 people in Engineering.")

    def test_default_team_size(self):
        mgr = Manager("Carol", "HR", 80000)
        self.assertEqual(mgr.team_size, 0)

    def test_is_employee(self):
        self.assertIsInstance(self.mgr, Employee)


if __name__ == '__main__':
    unittest.main()
