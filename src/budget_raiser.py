from src.menu_option import MenuOption
from src.branch_saver import BranchSaver

class BudgetRaiser(MenuOption):
    def execute(self):
        
        print('*** Welcome to Raise Budget of Branch\n')
        BranchSaver.print_info()

        branch_id = input('\nPlease Enter An ID Branch For Raise Budget: ')
        flag = False
        for branch in BranchSaver.branch_list:
            if branch.branch_id == branch_id:
                flag = True
                amount = input(f'And Enter Your Budget Amount for Raise Budget of Branch ID \"{branch_id}\": ')
                if amount.isdigit():
                    branch.budget += int(amount)
                    print('\n*** OK! Your Command Applied and Updated Branch.\n')
                    BranchSaver.print_info()
                    input('Press any Key for Return.')

                else:
                    print(f'\n*** Warning: Your Amount is Invlid.')
                    input('Press any Key for Return.')


        else:
            if flag == False:
                print(f'\n*** Warning: Branch ID \"{branch_id}\" Does not Exist.')
                input('Press any Key for Return.')





    
