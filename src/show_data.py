from src.menu_option import MenuOption
from src.bank_saver import BankSaver
from src.branch_saver import BranchSaver
from src.customer_saver import CustomerSaver
from src.show_data_customer import ShowDataCustomer
from src.loan import Loan

class ShowData(MenuOption):
    def execute(self):
        print('*** Your Banks: ')
        BankSaver.print_info()

        print('\n')

        print('*** Your Branchs: ')
        BranchSaver.print_info()

        print('\n')

        print('*** Customer\'s System: ')
        # Add unique nationality_codes into a Set
        nationality_codes = set()
        for customer in CustomerSaver.customer_list:
            nationality_codes.add(customer.nationality_code)
        # Print Customers with national_codes    
        for code in nationality_codes:
            CustomerSaver.print_info(code)


        print('\n')

        print('*** Your Loans: ')
        Loan.show_info()
        
        
        input("\nPress Enter to continue...")