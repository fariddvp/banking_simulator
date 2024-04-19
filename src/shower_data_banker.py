from src.menu_option import MenuOption
from src.bank_saver import BankSaver


class ShowerDataBanker(MenuOption):
    def execute(self):
        print('*** Your Banks: ')
        BankSaver.print_info()

        print('\n')
        
        input("\nPress Enter to continue...")



