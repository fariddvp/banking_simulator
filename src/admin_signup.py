from src.menu_option import MenuOption
from src.signup import signup


class AdminSignup(MenuOption):
    def execute(self):
        signup()