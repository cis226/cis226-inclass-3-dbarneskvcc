"""Program code"""

# System Imports
import os

# First-Party imports
from employee import SalaryEmployee, HourlyEmployee
from user_interface import UserInterface


def main(*args):
    """Method to run program"""

    # Make a new instance of the UserInterface class
    ui = UserInterface()

    # List to hold employees
    employees = []
    employees.append(SalaryEmployee("David", "Barnes", 835.00))
    employees.append(SalaryEmployee("James", "Kirk", 453.00))
    employees.append(HourlyEmployee("Jean-Luc", "Picard", 9.00, 40))
    employees.append(HourlyEmployee("Benjamin", "Sisko", 7.00, 30))
    employees.append(SalaryEmployee("Kathryn", "Janeway", 184.00))
    employees.append(HourlyEmployee("Jonathan", "Archer", 15.00, 35))

    # Get some input from the user
    selection = ui.display_menu_and_get_response()

    # While the choice they selected is not 2, continue to do work.
    while selection != ui.MAX_MENU_CHOICES:
        # See if the input they sent is equal to 1.
        if selection == 1:
            # Create string for concatenation
            output_string = ""

            # Convert each employee to a string and add it to the outputstring
            for employee in employees:
                # Concatenate to the output_string
                output_string += f"{employee}{os.linesep}"

            # Use the UI class to print out the string
            ui.print_list(output_string)

        # Check for different choice here if there was one to check.

        # Lastly, re-prompt user for input on what to do.
        selection = ui.display_menu_and_get_response()
