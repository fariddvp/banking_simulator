from src.menu_option import MenuOption
from src.file_admin_repository import FileAdminRepository
from src.admin_manager import AdminManager

PATH = '/home/farid/Documents/BankingSystemFinal/banking_simulator/src/password.txt'
class AdminSignup(MenuOption):
    def execute(self):
        data_repository = FileAdminRepository(PATH)
        admin_manager = AdminManager(data_repository)
        admin_manager.signup()