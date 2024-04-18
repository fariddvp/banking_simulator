from src.menu_option import MenuOption
from src.branch import Branch
from src.branch_saver import BranchSaver
from src.bank_saver import BankSaver
import time


class BranchCreator(MenuOption):

    def execute(self):
        if len(BankSaver.bank_list) == 0:
            print('You Don\'t Create any Bank yet. Please Create a Bank First.\n')
            input('Press any Key to Return Admin Menu.')
            return
        branch_name = input('Please Enter Branch Name: ')
        branch_id = input('And Enter Branch ID: ')
        bank_name = input('Please Enter Bank Name: ')
        bank_id = input('And Enter Bank ID: ')
        number_of_customer = 0
        budget = input('Enter Initial Budget: ')
        city_name = input('Enter City Name: ')
        
        branch = Branch(bank_name, bank_id, bank_name, branch_id, number_of_customer, budget, city_name)
        
        BranchSaver.save_branch(branch)
        time.sleep(2)