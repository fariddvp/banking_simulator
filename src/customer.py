from src.reporter import Reporter
from src.loan import Loan

class Customer(Reporter):
    customers_list = []
    

    def __init__(self, first_name, last_name, nationality_code, 
                 home_town, account_number, branch_id, loan_number=None):
        
        self.first_name = first_name
        self.last_name = last_name
        self.nationality_code = nationality_code
        self.home_town = home_town
        self.account_number = account_number
        self.loan_number = loan_number
        self.branch_id = branch_id
        Customer.customers_list.append(self)

       
    def show_details(self, nationality_code):
        if self.nationality_code == nationality_code:
            print(f'First Name: {self.first_name}, ' 
                f'Last Name: {self.last_name}, '
                f'Nationality Code: {self.nationality_code}, '
                f'Home Town: {self.home_town}, '
                f'Branch ID: {self.branch_id}, '
                f'Account Number: {self.account_number}, '
                f'Loan Number: {self.loan_number}')
                
            

    def loan_request(nationality_code, account_number, loan_amount):
        pass

    def deposit():
        pass

    def with_draw():
        pass
