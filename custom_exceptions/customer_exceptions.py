"""
Assignment name: Custom Exceptions Assignment
Program: Student.py
Author: Colby Boell
Last date modified: 04/11/2022

The purpose of this program is to use custom exceptions on a class and to test the custom exceptions with
unit tests
"""
class InvalidCustomerIDException(Exception):
    """
    Invalid Customer ID Exception Class
    """
    pass


class InvalidNameException(Exception):
    """
    Invalid Name Exception Class
    """
    pass


class InvalidPhoneNumberFormat(Exception):
    """
    Invalid Phone Number Format Class
    """
    pass
