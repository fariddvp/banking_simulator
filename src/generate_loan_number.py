import random

def generate_loan_number():
    loan_number = ''.join([str(random.randint(0, 9)) for _ in range(4)])
    return loan_number