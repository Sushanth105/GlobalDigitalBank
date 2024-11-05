from account import Account

class Saving(Account):
    def __init__(self, account_number, name, balance, is_active, privilege, date_of_birth, phone_number):
        super().__init__(account_number, name, balance, is_active, privilege)
        self.date_of_birth=date_of_birth
        self.phone_number=phone_number