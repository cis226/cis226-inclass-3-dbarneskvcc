"""Filter Library Module"""

# System Imports
from abc import ABC, abstractmethod


class Person(ABC):
    """Person that can be used with filter functionality"""

    @property
    @abstractmethod
    def first_name(self):
        """First Name Attribte"""
        raise NotImplementedError()

    @property
    @abstractmethod
    def last_name(self):
        """Last Name Attribute"""
        raise NotImplementedError()

    @property
    @abstractmethod
    def age(self):
        """Age Attribute"""
        raise NotImplementedError()


class PersonFilter:
    """Person Filter class for filtering a list of person"""

    def filter_by_first_name(
        self,
        list_to_filter: list[Person],
        first_name_filter: str,
    ) -> list[Person]:
        """Filter list by first name"""
        return_list = []
        for person in list_to_filter:
            if person.first_name == first_name_filter:
                return_list.append(person)
        return return_list

    def filter_by_last_name(
        self,
        list_to_filter: list[Person],
        last_name_filter: str,
    ) -> list[Person]:
        """Filter list by last name"""
        return_list = []
        for person in list_to_filter:
            if person.last_name == last_name_filter:
                return_list.append(person)
        return return_list

    def filter_by_age(
        self,
        list_to_filter: list[Person],
        age_filter: str,
    ) -> list[Person]:
        """Filter list by age"""
        return_list = []
        for person in list_to_filter:
            if person.age == age_filter:
                return_list.append(person)
        return return_list
