from src.reporter import Reporter

class Account(Reporter):
    account_list = []

    def __init__(self, account_number, account_amount, account_owner):
        self.account_number = account_number
        self.account_amount = account_amount
        self.accoun_owner = account_owner
        Account.account_list.append(self)

    def show_details(self, nationality_code):
        if self.accoun_owner == nationality_code:
            print(f'Account Number: {self.account_number}, ' 
                f'Account Amount: {self.account_amount}, '
                f'Account Owner: {self.accoun_owner}')
        