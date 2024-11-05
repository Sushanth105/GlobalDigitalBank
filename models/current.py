from account import Account

class Current(Account):
    def __init__(self, account_number, name, balance, is_active, privilege, company_name, registration_number):
        super().__init__(account_number, name, balance, is_active, privilege)
        self.company_name=company_name
        self.registration_number=registration_number