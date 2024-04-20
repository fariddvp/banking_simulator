from src.menu_option import MenuOption
from src.loan import Loan


class ShowerDataLoaner(MenuOption):
    def execute(self):
        print('*** Your Loans: ')
        Loan.show_info()

        print('\n')
        
        input("\nPress Enter to continue...")
