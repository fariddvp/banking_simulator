from src.admin_menu import AdminMenu
from src.exit_option import ExitOption
import time
import os

PATH = '/home/farid/Documents/BankingSystemFinal/banking_simulator/src/password.txt'

class LoginManager:
    
    def __init__(self, exit_option):
        self.exit_option = exit_option

    def login(self):

        if not os.path.exists(PATH):
            print('\n*** Warning: There is not any Admin in System, please signup first.\n')
            input('Enter any Key for Return to Admin Option.')
        else:
            with open(PATH, 'r') as r:
                admin = r.read().split('#')
                nationality_code = input('Please Enter Your Nationality Code: ')
                password = input('And Enter Your Password: ')

                if nationality_code == admin[0] and password == admin[1]:
                    print(f'\nHi, Admin with ID({admin[0]}), Welcome to Banking System. Please Wait...\n')
                    time.sleep(2)
                    admin_menu = AdminMenu(ExitOption)
                    admin_menu.select_option()

                else:
                    print('\n*** Warning: Your Nationality Code or Password is Invalid.')
                    input('Enter any Key to Return Admin Option.')

    
        
