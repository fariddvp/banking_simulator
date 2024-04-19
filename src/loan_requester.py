from src.menu_option import MenuOption
from src.customer_saver import CustomerSaver
from src.account import Account
from src.customer import Customer
from src.check_budget_for_loan import check_budget_for_loan
from src.loan import Loan
import os

class LoanRequester(MenuOption):
    loan_request = []

    def execute(self):
        os.system('clear')

        nationality_code = input('Please Enter Your Nationality Code: ')

        print('\n*** Information of Your Bank Accounts:\n')
        CustomerSaver.print_info(nationality_code)

        account_number = input('Please Enter Your Desired Account Number for Loan: ')

        flag = False
        for account in Account.account_list:
            if account.account_number == account_number:
                loan_amount = input('\nPlease Enter Your Desired Amount for Loan: ')

                # for Check amount is valid
                if not(loan_amount.isdigit() and int(loan_amount) > 0):
                    print(f'\n*** Warning: Your Amount is not Valid.')
                    input('Press Any Key for Try Again.\n')
                    return
                
                flag = True
                if check_budget_for_loan(account_number, loan_amount):
                    Customer.loan_request(account.account_owner, account.account_number, loan_amount)
                    print('\n*** Congratulations! Your Loan Request Accepted.')
                    input('Press Any Key to Return to Customer Option.')
                    return
                
                else:
                    print('\n*** Warning: Your Loan Request Rejected.')
                    input('Press Any Key to Return to Customer Option.')
                    return
                
        else:
            if flag == False:
                print(f'\n*** Warning: You Don\'t have an Account with ID: {account_number} ')
                input('Press Any Key for Try Again.\n')

        