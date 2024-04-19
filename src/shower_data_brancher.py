from src.menu_option import MenuOption
from src.branch_saver import BranchSaver


class ShowerDataBrancher(MenuOption):
    def execute(self):

        print('*** Your Branchs: ')
        BranchSaver.print_info()

        print('\n')
        
        input("\nPress Enter to continue...")