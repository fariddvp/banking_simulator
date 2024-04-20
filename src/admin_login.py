from src.menu_option import MenuOption
from src.login_manager import LoginManager
from src.exit_option import ExitOption

PATH = '/home/farid/Documents/BankingSystemFinal/banking_simulator/src/password.txt'

class AdminLogin(MenuOption):
    def execute(self):
        login_manager = LoginManager(ExitOption())
        login_manager.login()