from src.menu_option import MenuOption
from src.account import Account
from src.customer import Customer
from src.generate_account_number import generate_account_number
from src.customer_saver import CustomerSaver
import os


class OpeningAccount(MenuOption):
    def execute(self):
        os.system('clear')
        first_name = input('Please Enter Your First Name: ')
        last_name = input('Please Enter Your Last Name: ')
        nationality_code = input('Please Enter Your Nationality Code: ')
        
        if str(nationality_code).isdigit() and len(nationality_code) == 10:
            self.nationality_code = nationality_code
        else:
            print('\nWarning: Your Nationality Code is invalid. National Code is 8-Digits.')
            input('Press any Key for Try Again.')
            self.execute()

        home_town = input('Please Enter Your Home Town: ')
        
        # Generate 8-digit and unique account number
        existing_account_numbers = set(customer.account_number for customer in Customer.customers_list)
        account_number = generate_account_number(existing_account_numbers)

        account = Account(account_number, 0, None)

        customer = Customer(first_name, last_name, nationality_code, home_town, account_number)
        account.accoun_owner = customer.nationality_code
        
        CustomerSaver.save_customer(customer)
        
        input('Press any Key for Return to Customer Option')


        





