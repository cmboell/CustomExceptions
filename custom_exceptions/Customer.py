"""
Assignment name: Custom Exceptions Assignment
Program: Student.py
Author: Colby Boell
Last date modified: 04/11/2022

The purpose of this program is to use custom exceptions on a class and to test the custom exceptions with
unit tests
"""
from custom_exceptions.customer_exceptions import *


class Customer:
    """
    Customer Class
    """

    def __init__(self, customer_id, last_name, first_name, phone_number):
        if isinstance(customer_id, int) and 1000 <= customer_id <= 9999:
            self.customer_id = customer_id
        else:
            raise InvalidCustomerIDException("Invalid Customer ID")
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(last_name) and name_characters.issuperset(first_name)):
            raise InvalidNameException("Name must be alphabetic characters")
        phone_set = set("0123456789-")
        if not phone_set.issuperset(phone_number):
            raise InvalidPhoneNumberFormat("Phone number must be in the format: ###-###-####")
        else:
            try:
                phone_number_array = str(phone_number).split('-')
                area_code = phone_number_array[0]
                prefix = phone_number_array[1]
                line_number = phone_number_array[2]
                if len(area_code) != 3 or len(prefix) != 3 or len(line_number) != 4:
                    raise InvalidPhoneNumberFormat("Phone number must be in the format: ###-###-####")
            except IndexError:
                raise InvalidPhoneNumberFormat("Phone number must be in the format: ###-###-####")
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number

    def __str__(self):
        return ("Customer #{self.customer_id}: {self.last_name}, {self.first_name}, "
                "{self.phone_number}".format(self=self))

    def __repr__(self):

        return ("{self.__class__.__name__}({self.customer_id}, '{self.last_name}', "
                "'{self.first_name}', '{self.phone_number}')".format(self=self))

    def display(self):

        return ("Customer ID: " + str(self.customer_id) + "\n" + str(self.first_name) + " "
                + str(self.last_name) + "\n" + str(self.phone_number))


# Driver
if __name__ == '__main__':
    try:
        # valid customer info
        print("Working Customer:")
        customer = Customer(1221, 'Boell', 'Colby', '123-456-7890')
        print(customer.display())
    except InvalidPhoneNumberFormat as e:
        print(e)
    try:
        # invalid customer id
        print("Invalid Customer ID:")
        customer1 = Customer(1234, 'Kellihan', 'Lisa', '222-222-2222')
        print(customer1.display())
        del customer1
    except InvalidCustomerIDException as e:
        print(e)
    try:
        # invalid last name
        print("Invalid Last Name:")
        customer2 = Customer(8888, 'N8', 'Tom', '999-000-8789')
        print(customer2.display())
    except InvalidNameException as e:
        print(e)
    try:
        # invalid first name
        print("Invalid First Name:")
        customer3 = Customer(1877, 'Boell', '99', '111-002-2234')
        print(customer3.display())
    except InvalidNameException as e:
        print(e)
    try:
        # invalid phone number
        print("Invalid Phone Number:")
        customer4 = Customer(1234, 'Meeker', 'Daniel', '(444)-113-0021')
        print(customer4.display())
    except InvalidPhoneNumberFormat as e:
        print(e)

    print(customer.__str__())
