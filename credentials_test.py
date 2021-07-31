import unittest # Importing the unittest module
from credentials import Credentials # Importing the account class


class TestCredentials(unittest.TestCase):
    def setUp(self):
       
        self.new_credentials = Credentials("Amin","Moha","123456","moha.m@.com") # create Account object

    