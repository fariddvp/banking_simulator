from src.exit_option import ExitOption
from src.admin_option import AdminOption
from src.menu_option import MenuOption
import os


class MainMenu(MenuOption):
    def __init__(self):
        self.options = {
            '1': AdminOption(MainMenu),
            # '2': BankerOption(),
            # '3': CustomerOption(),
            # '4': UserOption(),
            '5': ExitOption()
        }
        
    def select_option(self):
        while True:
            os.system('clear')

            print('*** Welcome To Your Banking System ***')
            main_option = input('Please Enter Your Choice:\n'
                               '1- Admin\n2- Banker\n3- Customer\n4- User\n5- Exit\n')
            
            os.system('clear')

            if main_option in self.options:
                self.options[main_option].execute()
            else:
                print("Invalid option. Please choose again.")

    def execute(self):
        self.select_option()