from account import Account
from credentials import Credentials

def create_account(account_name,user_name,password,email):
    '''
    Function to create a new account
    '''
    new_account = Account(account_name,user_name,password,email)
    return new_account

def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()    

def del_account(account):
    '''
    Function to delete a account
    '''
    account.delete_account()    


def find_account(name):
    '''
    Function that finds a account by nane and returns the account
    '''
    return Account.find_by_name(name)    