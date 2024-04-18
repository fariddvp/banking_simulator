from src.menu_option import MenuOption
import os

PATH = '/home/farid/Documents/TAAV_vscode_prj/banking_simulator/src/password.txt'

def signup():
    '''
    this function check for signup Admin to banking system.
    '''
    first_name = input('Please Enter Your First Name: ')
    last_name = input('Please Enter Your Last Name: ')
    nationality_code = input('Please Enter Your Nationality Code: ')

    if str(nationality_code).isdigit() and len(nationality_code) == 10:
        True
    else:
        print('\nWarning: Your Nationality Code is invalid. National Code is 8-Digits.')
        input('Press any Key for Try Again.\n')
        return

    password = input('And Enter Your Password: ')

    if not os.path.exists(PATH):
        with open(PATH, 'w') as w:
            w.write(nationality_code + '#' + password + '#' + first_name + '#' + last_name)
            print(f'\nYou Registered as Admin with'
                    f'Nationality Code: {nationality_code}\n')
    else:
        with open(PATH, 'r') as r:
            admin_info = r.read().split('#')
            if admin_info[0] == nationality_code:
                print(f'\nYou Already Signed Up with Nationality Code: ({nationality_code})')
            
            elif admin_info[0] != '' and admin_info[1] != '':
                print('\nAlready an Admin Registered and You Can not Add as another Admin, Please Login.')

            else:
                with open(PATH, 'w') as w:
                    w.write(nationality_code + '#' + password)
                    print(f'\nSuccessful! You Registered as Admin with'
                           f'Nationality Code: {nationality_code} and Password: {password}')
            
    input('Enter any Key for Return to Admin Option.')
                    