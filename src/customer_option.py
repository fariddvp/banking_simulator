from src.menu_option import MenuOption
from src.exit_option import ExitOption
from src.previous_menu import PreviousMenu
from src.opening_account import OpeningAccount
from src.show_data_customer import ShowDataCustomer
from src.deposit import Deposit
from src.with_draw import WithDraw
import os

class CustomerOption(MenuOption):
    def __init__(self, previous_menu):
        self.options = {
            '1': ShowDataCustomer(),
            '2': OpeningAccount(),
            # '3': LoanRequest(),
            '4': Deposit(),
            '5': WithDraw(),
            '6': PreviousMenu(),
            '7': ExitOption()
        }
        
    def select_option(self):
        while True:
            os.system('clear')

            print('*** Welcome To Customer Options')
            admin_option = input('Please Enter Your Choice:\n'
                               '1- Show Details\n2- Opening an Account\n'
                               '3- Loan Request\n4- Deposit\n5- With Draw\n'
                               '6- Previous Menu\n7- Exit\n')
            os.system('clear')

            if admin_option in self.options:
                self.options[admin_option].execute()
                # Return to the previous menu
                if admin_option == '6':
                    return  
            else:
                print("Invalid option. Please choose again.")
    
    def execute(self):
        self.select_option()

