"""Employee Module"""

class Employee:
    """Class to represent a single Employee"""

    WEEKS_PER_YEAR = 52

    def __init__(self, first_name, last_name):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name

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


class SalaryEmployee(Employee):
    """Class to represent a single salary employee"""

    def __init__(self, first_name, last_name, weekly_salary):
        """Constructor"""
        super().__init__(first_name, last_name)
        self.weekly_salary = weekly_salary

    def __str__(self):
        """String method"""
        return (
            f"{super().__str__()} "
            f"{self.formatted_weekly_salary:>14}"
        )

    @property
    def formatted_weekly_salary(self):
        """Property for weekly salary formatted as currency"""
        return f"${self.weekly_salary:.2f}"

    @property
    def yearly_salary(self):
        """Property for yearly salary"""
        return self.weekly_salary * self.WEEKS_PER_YEAR

    @property
    def formatted_yearly_salary(self):
        """Property for yearly salary formatted as currency"""
        return f"${self.yearly_salary:.2f}"

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
        return (
            f"{super().__str__()} "
            f"{self.formatted_weekly_salary:>14}"
        )

    @property
    def weekly_salary(self):
        """Property for weekly salary"""
        return self.hourly_rate * self.hours_per_week

    @property
    def formatted_weekly_salary(self):
        """Property for weekly salary formatted as currency"""
        return f"${self.weekly_salary:.2f}"

    @property
    def yearly_salary(self):
        """Property for yearly salary"""
        return self.weekly_salary * self.WEEKS_PER_YEAR

    @property
    def formatted_yearly_salary(self):
        """Property for yearly salary formatted as currency"""
        return f"${self.yearly_salary:.2f}"

    def apply_percentage_raise(self, percentage):
        """Accept a percentage raise and apply it to the hourly rate"""
        self.hourly_rate = self.hourly_rate * (1 + (percentage / 100))
