from src.menu_option import MenuOption
from src.customer_saver import CustomerSaver
from src.account import Account
from src.customer import Customer
from src.check_budget_for_loan import check_budget_for_loan
from src.loan import Loan
from src.generate_loan_number import generate_loan_number
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
            
                    loan_number = generate_loan_number()

                    branch_id = ''
                    for customer in Customer.customers_list:
                        if customer.account_number == account_number:
                            branch_id = customer.branch_id
                            # Update loan number
                            for loan in Loan.loan_list:
                                if loan.branch_id == branch_id and loan.customer_id == nationality_code:
                                    print('\n*** Unfortunately! Your Loan Request Reject. You Have a Loan in Our Branch.')
                                    input('Press Any Key to Return to Customer Option.')
                                    return
                            customer.loan_number.append(loan_number)


                    Loan(loan_number, loan_amount, nationality_code, account_number, branch_id)

                    print('\n*** Congratulations! Your Loan Request Accepted.')
                    input('Press Any Key to Return to Customer Option.')
                    return
                
                else:
                    print('\n*** Warning: Your Loan Request Rejected. You Can Raise Your Amount and Try again.')
                    input('Press Any Key to Return to Customer Option.')
                    return       
                
        else:
            if flag == False:
                print(f'\n*** Warning: You Don\'t have an Account with ID: {account_number} ')
                input('Press Any Key for Try Again.\n')

        