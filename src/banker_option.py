from src.menu_option import MenuOption
from src.show_data import ShowData
from src.shower_data_customer import ShowerDataCustomer
from src.shower_data_brancher import ShowerDataBrancher
from src.shower_data_banker import ShowerDataBanker
from src.previous_menu import PreviousMenu
from src.show_data_loaner import ShowerDataLoaner
import os

class BankerOption(MenuOption):
    def __init__(self, previous_menu):
        self.options = {
            '1': ShowData(),
            '2': ShowerDataCustomer(),
            '3': ShowerDataBanker(),
            '4': ShowerDataBrancher(),
            '5': ShowerDataLoaner(),
            '6': PreviousMenu(),
            # '7': ExitOption()
        }
        
    def select_option(self):
        while True:
            os.system('clear')
            
            print('*** Welcome To Banker Options')
            admin_option = input('Please Enter Your Choice:\n'
                               '1- Show General View\n2- Show Customers View\n'
                               '3- Show Banks View\n4- Show Branches View\n'
                               '5- Show Loans View\n6- Previous Menu\n7- Exit\n')
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