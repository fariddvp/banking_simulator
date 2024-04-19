from src.menu_option import MenuOption
from src.customer_saver import CustomerSaver


class ShowerDataCustomer(MenuOption):
    def execute(self):

        print('*** Customer\'s System: ')
        # Add unique nationality_codes into a Set
        nationality_codes = set()
        for customer in CustomerSaver.customer_list:
            nationality_codes.add(customer.nationality_code)
        # Print Customers with national_codes    
        for code in nationality_codes:
            CustomerSaver.print_info(code)
        
        
        input("\nPress Enter to continue...")