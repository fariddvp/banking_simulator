from src.menu_option import MenuOption
from src.exit_option import ExitOption
from src.previous_menu import PreviousMenu

import os


class AdminMenu(MenuOption):
    def __init__(self, previous_menu):
        self.options = {
            # '1': AdminOption(MainMenu),
            # '2': BankerOption(),
            # '3': CustomerOption(),
            # '4': UserOption(),
            # '5': ExitOption()
            # '6': PreviousMenu(),
            '7': PreviousMenu(),
            '8': ExitOption()
        }
        
    def select_option(self):
        while True:
            os.system('clear')

            print('*** Welcome To Admin Menu')
            admin_menu = input('Please Enter Your Option:\n'
                               '1- Show Data\n2- Create Bank\n'
                               '3- Create Branch\n4- Delete Branch\n'
                               '5- Determine Budget\n6- Change Password\n'
                               '7- Previous Menu\n8- Exit\n')
            
            os.system('clear')

            if admin_menu in self.options:
                self.options[admin_menu].execute()
                # Return to the previous menu
                if admin_menu == '7':
                    return
            else:
                print("Invalid option. Please choose again.")

    def execute(self):
        self.select_option()