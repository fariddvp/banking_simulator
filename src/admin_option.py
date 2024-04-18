from src.menu_option import MenuOption
from src.exit_option import ExitOption
from src.admin_login import AdminLogin
from src.admin_signup import AdminSignup
from src.previous_menu import PreviousMenu
import os

class AdminOption(MenuOption):
    def __init__(self, previous_menu):
        self.options = {
            '1': AdminLogin(),
            '2': AdminSignup(),
            '3': PreviousMenu(),
            '4': ExitOption()
        }
        
    def select_option(self):
        while True:
            os.system('clear')
            
            print('*** Welcome To Admin Options')
            admin_option = input('Please Enter Your Choice:\n'
                               '1- Login\n2- Signup(for first time)\n3- Previous Menu\n4- Exit\n')
            os.system('clear')

            if admin_option in self.options:
                self.options[admin_option].execute()
                # Return to the previous menu
                if admin_option == '3':
                    return  
            else:
                print("Invalid option. Please choose again.")
    
    def execute(self):
        self.select_option()

