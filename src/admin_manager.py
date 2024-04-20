from src.admin import Admin

class AdminManager:
    def __init__(self, data_repository):
        self.data_repository = data_repository

    def signup(self):
        first_name = input('Please Enter Your First Name: ')
        last_name = input('Please Enter Your Last Name: ')
        nationality_code = input('Please Enter Your Nationality Code: ')

        if not self._validate_nationality_code(nationality_code):
            print('\nWarning: Your Nationality Code is invalid. National Code is 8-Digits.')
            input('Press any Key for Try Again.\n')
            return

        password = input('And Enter Your Password: ')

        admin = Admin(nationality_code, password, first_name, last_name)
        admin.set_password(password)
        self.data_repository.create_admin(admin)

        print(f'\nYou Registered as Admin with Nationality Code: {nationality_code}\n')

    def _validate_nationality_code(self, code):
        return code.isdigit() and len(code) == 10