from src.menu_option import MenuOption
from src.branch import Branch
from src.branch_saver import BranchSaver
from src.bank_saver import BankSaver
import time

class BranchCreator(MenuOption):

    def execute(self):
        if len(BankSaver.bank_list) == 0:
            print('*** Warning: You Don\'t Create any Bank yet. Please Create a Bank First.\n')
            input('Press any Key to Return Admin Menu.')
            return
        branch_name = input('Please Enter Branch Name: ')
        branch_id = input('And Enter Branch ID: ')
        bank_name = input('Please Enter Bank Name: ')
        # Get Bank ID Automatically
        flag = False
        for bank in BankSaver.bank_list:
            if bank.bank_name == bank_name:
                bank_id = bank.bank_id
                flag = True
                break
        # if Bank does not exist, so you can not create branch
        else:
            if flag == False:
                print(f'\n*** Warning: Bank with Name: \"{bank_name}\" does not Exist.')
                input('Press any Key for Return Admin Menu.')
                return

        number_of_customer = 0
        budget = input('Enter Initial Budget: ')
        if budget.isdecimal():
            budget = int(budget)
            if budget < 0:
                print('\n*** Warning: Your Budget Amount is Invalid.')
                input('Press any Key for Return Admin Menu.')
                return 

        else:
            print('\n*** Warning: Your Budget Amount is Invalid.')
            input('Press any Key for Return Admin Menu.')
            return    
        
        city_name = input('Enter City Name: ')
        
        branch = Branch(bank_name, bank_id, branch_name, branch_id, number_of_customer, budget, city_name)
        
        BranchSaver.save_branch(branch)
        time.sleep(2)