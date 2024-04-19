from src.account import Account
from src.customer import Customer

class CustomerSaver():
    customer_list = []

    @classmethod
    def save_customer(cls, customer):
        cls.customer_list.append(customer)
        print(f'\n*** Congratulations! You Registered in Our System with Nationality Code: {customer.nationality_code}, '
               f'Account Number: {customer.account_number}\n')

    @classmethod
    def print_info(cls, nationality_code):
        for customer in cls.customer_list:
            customer.show_details(nationality_code)

        for account in Account.account_list:
            account.show_details(nationality_code)
        
        

        print('-----------------------------------------------------------------------')

