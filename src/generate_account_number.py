import random

def generate_account_number(existing_account_numbers):
    while True:
        account_number = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        if account_number not in existing_account_numbers:
            return account_number