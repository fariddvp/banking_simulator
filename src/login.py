from src.admin_menu import AdminMenu
from src.exit_option import ExitOption
import os

PATH = '/home/farid/Documents/TAAV_vscode_prj/banking_simulator/src/password.txt'

# Login Admin to System Banking
def login():
    '''
    this function check for login Admin to banking system.
    '''
    
    # Create Password txt File if does not Exist.
    if not os.path.exists(PATH):
        print('There is not any Admin in System, please signup first.\n')
    
    else:
        with open(PATH, 'r') as r:
            admin = r.read().split('#')
            nationality_code = input('Please Enter Your Nationality Code: ')
            password = input('And Enter Your Password: ')

            if nationality_code == admin[0] and password == admin[1]:
                print(f'Hi, Admin with ID({admin[0]}), Welcome to Admin\'s Panel...\n')
                admin_menu = AdminMenu(ExitOption)
                admin_menu.select_option()

            else:
                print('Your Nationality Code or Password is Invalid.\n')
