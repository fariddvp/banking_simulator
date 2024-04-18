from src.menu_option import MenuOption
from src.customer_saver import CustomerSaver

class ShowDataCustomer(MenuOption):
    def execute(self):

        nationality_code = input('Please Enter Your Nationality Code: ')

        print('*** Your Banking Information: ')
        CustomerSaver.print_info(nationality_code)

        print('\n')
        input('Press any Key for Return to Customer Option')
