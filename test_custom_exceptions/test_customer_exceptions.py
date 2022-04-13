"""
Assignment name: Custom Exceptions Assignment
Program: Student.py
Author: Colby Boell
Last date modified: 04/11/2022

The purpose of this program is to use custom exceptions on a class and to test the custom exceptions with
unit tests
"""
import unittest
from custom_exceptions import Customer as c
from custom_exceptions.customer_exceptions import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.customer = c.Customer(1221, "Boell", "Colby", "111-222-3333")

    def tearDown(self):
        del self.customer

    def test_attributes(self):  # test constructor with all valid input
        customer = c.Customer(1221, 'Boell', 'Colby', '111-222-3333')
        assert customer.customer_id == 1221
        assert customer.last_name == 'Boell'
        assert customer.first_name == 'Colby'
        assert customer.phone_number == '111-222-3333'

    def test_error_customer_id(self):
        with self.assertRaises(InvalidCustomerIDException):
            c.Customer(999999, 'Nala', 'Margot', '888-888-8888')

    def test_error_last_name(self):
        with self.assertRaises(InvalidNameException):
            c.Customer(1344, 'N8t', 'Andy', '111-111-1111')

    def test_error_fist_name(self):
        with self.assertRaises(InvalidNameException):
            c.Customer(8881, 'Torgerson', 'Anth0n', '987-654-3210')

    def test_error_phone_number(self):
        with self.assertRaises(InvalidPhoneNumberFormat):
            c.Customer(2626, 'Lamp', 'Kyle', '(101)-999-0654')

    def test_customer_str(self):
        self.assertEqual(str(self.customer), 'Customer #1221: Boell, Colby, 111-222-3333')


if __name__ == '__main__':
    unittest.main()
