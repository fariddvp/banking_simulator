from src.menu_option import MenuOption

PATH = '/home/farid/Documents/TAAV_vscode_prj/banking_simulator/src/password.txt'

class PasswordChanger(MenuOption):

    def read_admin_password(self):
        try:
            with open(PATH, 'r') as file:
                return file.read().split('#')
        except FileNotFoundError:
            print("Error: Password file not found.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    def write_admin_password(self, new_admin):
        try:
            with open(PATH, 'w') as writer:
                writer.write(new_admin)
            print('Your Password Successfully Changed.')
        except Exception as e:
            print(f"Error: {e}")

    def execute(self):
        admin = self.read_admin_password()
        if admin:
            print(f'*** Hi, dear {admin[2]} {admin[3]} Welcome to Change Password Menu')
            old_password = input('Please Enter Your Old Password: ')
            new_password = input('And Please Enter Your New Password: ')

            if old_password == admin[1]:
                result = input('Are You Sure(y/n): ')
                if result.lower() == 'y':
                    new_admin = f"{admin[0]}#{new_password}#{admin[2]}#{admin[3]}"
                    self.write_admin_password(new_admin)
            else:
                print('Oops! Your Old Password is Wrong!')

        input('\nPress any Key for Return to Admin Menu. Please Enter again to System.')
        
        exit()
        
        
