"""Employee Module"""

# System Imports
from abc import ABC, abstractmethod
from person_filter import Person


class Employee(Person, ABC):
    """Class to represent a single Employee"""

    WEEKS_PER_YEAR = 52

    def __init__(self, first_name, last_name):
        """Constructor"""
        self._first_name = first_name
        self._last_name = last_name

    def __str__(self):
        """String method"""
        return f"{self.first_name:<10} {self.last_name:<20}"

    def first_and_last_name(self):
        """Return first and last name concated together"""
        return f"{self.first_name:<10} {self.last_name:<20}"
        # Can't do it with below statement as it will then
        # try to run the __str__ of the child class and
        # end up printing more than we want.
        # return self.__str__()

    # Properties that are required for us to write from the Person class.
    # Person has these three properties marked as abstract, so if we plan
    # to inherit from it, we must provide implementations for them.
    @property
    def first_name(self):
        """First Name Property"""
        return self._first_name

    @property
    def last_name(self):
        """Last Name Property"""
        return self._last_name

    @property
    def age(self):
        """Age Property"""
        return None

    # Made this property abstract so that child classes of this class
    # must make an implementation for this method / property
    @property
    @abstractmethod
    def weekly_salary(self):
        """Property for weekly salary"""
        raise NotImplementedError()

    # Now that the above abstract method is required in children and
    # technically defined in here, we can use that property in this method.
    # No need to redefine it in the child classes.
    @property
    def formatted_weekly_salary(self):
        """Property for weekly salary formatted as currency"""
        return f"${self.weekly_salary:.2f}"

    # Made this property abstract so that child classes of this class
    # must make an implementation for this method / property
    @property
    @abstractmethod
    def yearly_salary(self):
        """Property for yearly salary"""
        raise NotImplementedError()

    # Now that the above abstract method is required in children and
    # technically defined in here, we can use that property in this method.
    # No need to redefine it in the child classes.
    @property
    def formatted_yearly_salary(self):
        """Property for yearly salary formatted as currency"""
        return f"${self.yearly_salary:.2f}"


class SalaryEmployee(Employee):
    """Class to represent a single salary employee"""

    def __init__(self, first_name, last_name, weekly_salary):
        """Constructor"""
        super().__init__(first_name, last_name)
        self._weekly_salary = weekly_salary

    def __str__(self):
        """String method"""
        return f"{super().__str__()} " f"{self.formatted_weekly_salary:>14}"

    @property
    def weekly_salary(self):
        """Property for weekly salary"""
        return self._weekly_salary

    @property
    def yearly_salary(self):
        """Property for yearly salary"""
        return self.weekly_salary * self.WEEKS_PER_YEAR

    def apply_percentage_raise(self, percentage):
        """Accept a percentage raise and apply it to the weekly salary"""
        self.weekly_salary = self.weekly_salary * (1 + (percentage / 100))


class HourlyEmployee(Employee):
    """Class to represent a single hourly employee"""

    def __init__(self, first_name, last_name, hourly_rate, hours_per_week):
        """Constructor"""
        super().__init__(first_name, last_name)
        self.hourly_rate = hourly_rate
        self.hours_per_week = hours_per_week

    def __str__(self):
        """String method"""
        return f"{super().__str__()} " f"{self.formatted_weekly_salary:>14}"

    @property
    def weekly_salary(self):
        """Property for weekly salary"""
        return self.hourly_rate * self.hours_per_week

    @property
    def yearly_salary(self):
        """Property for yearly salary"""
        return self.weekly_salary * self.WEEKS_PER_YEAR

    def apply_percentage_raise(self, percentage):
        """Accept a percentage raise and apply it to the hourly rate"""
        self.hourly_rate = self.hourly_rate * (1 + (percentage / 100))
