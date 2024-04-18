class BankSaver():
    bank_list = []

    @classmethod
    def save_bank(cls, bank):
        cls.bank_list.append(bank)
        print('Your Bank Successfully Added.')

    @classmethod
    def print_info(cls):
        for bank in cls.bank_list:
            bank.show_details()