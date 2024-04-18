from src.menu_option import MenuOption
from src.branch_saver import BranchSaver

class BranchDeleter(MenuOption):
    def execute(self):
        branch_name = input('Please Enter Branch Name: ')
        for branch in BranchSaver.branch_list:
            if branch.branch_name != branch_name:
                print(f'\n*** Warning: Branch with Name: \"{branch_name}\" Does not Exist.')
                input('Enter any Key for Return to Admin Option.')
                return
            
        bank_name = input('And Enter Bank Name of Branch: ')

        for branch in BranchSaver.branch_list:
            if branch.bank_name == bank_name:
                result = input('Are You Sure?(y/n)')
                if result.lower() == 'y':
                    BranchSaver.branch_list.remove(branch)
                    print(f'\n*** Warning: Branch with Name: \"{branch_name}\" Successfully Removed.')
                    input('Enter any Key for Return to Admin Option.')
                    return
            else:
                print(f'\n*** Warning: Branch with Name: \"{branch_name}\" and \"{bank_name}\" Does not Exist.')
                input('Enter any Key for Return to Admin Option.')
                return
 



