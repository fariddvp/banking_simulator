from src.menu_option import MenuOption
from src.branch import Branch
from src.branch_saver import BranchSaver
import time


class BranchCreator(MenuOption):

    def execute(self):
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