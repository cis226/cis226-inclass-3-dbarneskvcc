"""Tests for Employee module"""

# System Imports
from unittest import TestCase

# First-party Imports
from employee import HourlyEmployee, SalaryEmployee


class HourlyEmployeeTest(TestCase):
    """Tests for Hourly Employee"""

    def setUp(self):
        """Set up method for all tests in this class"""
        self.hourly_employee = HourlyEmployee("Test", "User", 50, 10)

    def test_hourly_employee_creation(self):
        """Test hourly employee creation"""
        # Arrange
        expected_first_name = "Test"
        expected_last_name = "User"
        expected_weekly_salary = 500.00

        # Act
        # No longer need this due to using the one in setUp
        # hourly_employee = HourlyEmployee("Test", "User", 50.00, 10)

        # Assert
        self.assertEqual(self.hourly_employee.first_name, expected_first_name)
        self.assertEqual(self.hourly_employee.last_name, expected_last_name)
        self.assertEqual(self.hourly_employee.weekly_salary, expected_weekly_salary)

    def test_hourly_employee_str_method(self):
        """Test hourly employee str method"""
        # Arrange
        # expected = "Test User $500.00"
        expected = f"{'Test':<10} {'User':<20} {'$500.00':>14}"

        # Act
        actual = str(self.hourly_employee)

        # Assert
        self.assertEqual(expected, actual)

    def test_hourly_employee_formatted_yearly_salary(self):
        """Test hourly employee formatted yearly salary"""

        # Arrange
        expected = "$26000.00"

        # Act
        actual = self.hourly_employee.formatted_yearly_salary

        # Assert
        self.assertEqual(expected, actual)


class SalaryEmployeeTest(TestCase):
    """Tests for Salary Employee"""

    def setUp(self):
        """Set up method for all tests in this class"""
        self.salary_employee = SalaryEmployee("Test", "User", 500)

    def test_hourly_employee_creation(self):
        """Test hourly employee creation"""
        # Arrange
        expected_first_name = "Test"
        expected_last_name = "User"
        expected_weekly_salary = 500.00

        # Act
        # No longer need this due to using the one in setUp
        # hourly_employee = HourlyEmployee("Test", "User", 50.00, 10)

        # Assert
        self.assertEqual(self.salary_employee.first_name, expected_first_name)
        self.assertEqual(self.salary_employee.last_name, expected_last_name)
        self.assertEqual(self.salary_employee.weekly_salary, expected_weekly_salary)

    def test_hourly_employee_str_method(self):
        """Test hourly employee str method"""
        # Arrange
        # expected = "Test User $500.00"
        expected = f"{'Test':<10} {'User':<20} {'$500.00':>14}"

        # Act
        actual = str(self.salary_employee)

        # Assert
        self.assertEqual(expected, actual)

    def test_hourly_employee_formatted_yearly_salary(self):
        """Test hourly employee formatted yearly salary"""

        # Arrange
        expected = "$26000.00"

        # Act
        actual = self.salary_employee.formatted_yearly_salary

        # Assert
        self.assertEqual(expected, actual)
