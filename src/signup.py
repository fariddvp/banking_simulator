from src.menu_option import MenuOption
import os

PATH = '/home/farid/Documents/TAAV_vscode_prj/banking_simulator/src/password.txt'

def signup():
    first_name = input('Please Enter Your First Name: ')
    last_name = input('Please Enter Your Last Name: ')
    nationality_code = input('Please Enter Your Nationality Code: ')
    password = input('And Enter Your Password: ')

    if not os.path.exists(PATH):
        with open(PATH, 'w') as w:
            w.write(nationality_code + '#' + password + '#' + first_name + '#' + last_name)
            print(f'You Registered as Admin with'
                    f'Nationality Code: {nationality_code} and Password: {password}\n')
    else:
        with open(PATH, 'r') as r:
            admin_info = r.read().split('#')
            if admin_info[0] == nationality_code:
                print(f'You Already Signed Up with Nationality Code: ({nationality_code})\n')
            
            elif admin_info[0] != '' and admin_info[1] != '':
                print('Already an Admin Registered and You Can not Add as another Admin, Please Login.\n')

            else:
                with open(PATH, 'w') as w:
                    w.write(nationality_code + '#' + password)
                    print(f'Successful! You Registered as Admin with'
                           f'Nationality Code: {nationality_code} and Password: {password}\n')
                    