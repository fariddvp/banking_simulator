from src.bank import Bank
from src.reporter import Reporter

class Branch(Bank, Reporter):
    branch_count = 0

    def __init__(self, bank_name, bank_id, branch_name, branch_id,
                  number_of_customers, budget, city_name):
        super().__init__(bank_name, bank_id)
        self.branch_name = branch_name
        self.branch_id = branch_id
        self.number_of_customers = number_of_customers
        self.budget = budget
        self.city_name = city_name
        Branch.branch_count += 1

    def show_details(self):
        print(f'Branch Name: {self.branch_name}, Branch ID: {self.branch_id}, '
               f'Bank Name: {self.bank_name}, Bank ID: {self.bank_id}, '
               f'Number of Customer: {self.number_of_customers}, Budget: {self.budget}, '
               f'City Name: {self.city_name}')