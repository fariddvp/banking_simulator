from src.menu_option import MenuOption
from src.login import login

class AdminLogin(MenuOption):
    def execute(self):
        login()