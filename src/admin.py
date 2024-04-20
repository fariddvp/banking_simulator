from src.user import User
from src.security import Security


class Admin(User, Security):
    def __init__(self, nationality_code, password, first_name, last_name):
        super().__init__(nationality_code, first_name, last_name)
        self._password = password

    def set_password(self, password):
            self.set_password = password
        
    @property
    def password(self):
        return self._password
    



        

    
    