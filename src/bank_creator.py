from src.menu_option import MenuOption
from src.bank import Bank
from src.bank_saver import BankSaver
import time


class BankCreator(MenuOption):

    def execute(self):
        bank_name = input('Please Enter Bank Name: ')
        bank_id = input('And Enter Bank ID: ')
        
        bank = Bank(bank_name, bank_id)
        
        BankSaver.save_bank(bank)
        time.sleep(2)