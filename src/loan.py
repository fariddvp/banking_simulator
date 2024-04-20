from src.generate_loan_number import generate_loan_number

class Loan:
    loan_list = []

    def __init__(self, loan_number, loan_amount, customer_id, account_id, branch_id):
        self.loan_number = loan_number
        self.loan_amount = loan_amount
        self.customer_id = customer_id
        self.account_id = account_id
        self.branch_id = branch_id
        Loan.loan_list.append(self)

    def show_info():
        for loan in Loan.loan_list:
            print(f'Loan Number: {loan.loan_number}, Loan Amount: {loan.loan_amount}, '
                  f'Customer ID: {loan.customer_id}, Account ID: {loan.account_id}, '
                   f'Branch ID: {loan.branch_id}')

    