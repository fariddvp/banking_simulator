from src.menu_option import MenuOption
from src.bank_saver import BankSaver
from src.branch_saver import BranchSaver

class ShowData(MenuOption):
    def execute(self):
        print('*** Your Banks: ')
        BankSaver.print_info()

        print('\n')

        print('*** Your Branchs: ')
        BranchSaver.print_info()
        input("\nPress Enter to continue...")