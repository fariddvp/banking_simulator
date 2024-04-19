from src.customer import Customer
from src.account import Account
from src.branch_saver import BranchSaver

def check_budget_for_loan(account_number, loan_amount):
    
    # Update Branch Budget
    branch_id = ''
    customer_account_amount = 0
    for customer in Customer.customers_list:
        if customer.account_number == account_number:
            branch_id = customer.branch_id

    for account in Account.account_list:
        if account.account_number == account_number:
            customer_account_amount = account.account_amount

    for branch in BranchSaver.branch_list:
        if branch.branch_id == branch_id:
            if ((branch.budget * 0.25) >= int(loan_amount)) and (customer_account_amount >= (int(loan_amount) * 0.5)):
                branch.budget -= int(loan_amount)

    return True                        