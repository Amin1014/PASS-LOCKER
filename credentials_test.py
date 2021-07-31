import unittest # Importing the unittest module
from account import Account # Importing the account class


class TestAccount(unittest.TestCase):
    def setUp(self):
       
        self.new_account = Account("Amin","Moha","123456","moha.m@.com") # create Account object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name,"Amin")
        self.assertEqual(self.new_account.user_name,"Moha")
        self.assertEqual(self.new_account.password,"123456")
        self.assertEqual(self.new_account.email,"moha.m@.com")

    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() # saving the new account
        self.assertEqual(len(Account.account_list),1)  