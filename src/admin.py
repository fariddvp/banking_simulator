from src.user import User
from src.security import Security


class Admin(User, Security):
    def __init__(self, nationality_code, first_name, last_name):
        super().__init__(nationality_code, first_name, last_name)
        self.password = None

    def set_password(self, password):
        if len(str(password)) == 4:
            self.set_password = password
        
        else:
            print('Admin\'s Password must be exactly 4 characters long.')

    @property
    def password(self):
        return self._password
    



        

    
    