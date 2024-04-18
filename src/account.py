from src.reporter import Reporter

class Account(Reporter):
    def __init__(self, account_number, account_amount, account_owner):
        self.account_number = account_number
        self.account_amount = account_amount
        self.accoun_owner = account_owner

    def show_details(self):
        print(f'Account Number: {self.account_number}, ' 
              f'Account Amount: {self.account_amount}, '
              f'Account Owner: {self.accoun_owner}')
        