from src.reporter import Reporter
from src.bank_saver import BankSaver

class Bank(Reporter):
    bank_count = 0

    def __init__(self, bank_name, bank_id):
        self.bank_name = bank_name
        self.bank_id = bank_id
        Bank.bank_count += 1

    def show_details(self):
        print(f'Bank Name: {self.bank_name}, Bank ID: {self.bank_id}')