from src.menu_option import MenuOption
from src.account import Account
from src.customer_saver import CustomerSaver
import os

class Deposit(MenuOption):
    def execute(self):
        os.system('clear')

        nationality_code = input('Please Enter Your Nationality Code: ')

        print('\n*** Information of Your Bank Accounts:\n')
        CustomerSaver.print_info(nationality_code)

        account_number = input('Please Enter Your Desired Account Number for Deposit: ')


        for account in Account.account_list:
            if account.account_number == account_number:
                amount = input('\nPlease Enter Your Desired Amount for Deposit: ')

                # for Check amount is valid
                if not(amount.isdigit() and int(amount) > 0):
                    print(f'\n*** Warning: Your Amount is not Valid.')
                    input('Press Any Key for Try Again.\n')
                    self.execute()

                
                account.account_amount += int(amount)
                
                os.system('clear')

                print('\n*** Updated Information of Your Bank Accounts: ')
                CustomerSaver.print_info(nationality_code)
                input('Press Any Key for Return to Customer Option.')
                break

        else:
            print(f'\n*** Warning: You Don\'t have an Account with ID: {account_number} ')
            input('Press Any Key for Try Again.\n')
