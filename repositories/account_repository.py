# class to store all the account
class AccountRepository():
    account=[]
    account_counter=1000
    
    # Differences 
    # 1. class method takes cls as its first argument 
    # 2. Instance/regular method takes self as its first argument 
    # 3. static method takes neither cls nor self as its first argument
    
    # Method to generate a new account number
    @classmethod
    def generate_account_number(cls):
        cls.account_counter += 1
        return cls.account_counter
    
    # Method to save account
    @classmethod
    def save_account(cls, account):
        cls.account.append(account)
        
    # method to get all account
    def get_all_account(self):
        return self.account