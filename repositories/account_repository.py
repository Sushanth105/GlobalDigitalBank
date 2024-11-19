# class to store all the account
class AccountRepository():
    account=[]
    account_counter=1000
    account_dictionary={'saving':[],'current':[]}
    saving_count=0
    current_count=0
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
    def save_account(cls,account_type, account):
        cls.account.append(account)
        cls.account_dictionary[account_type].append(account)
        if account_type == 'saving':
            cls.saving_count += 1
        else:
            cls.current_count += 1
        
    # method to get all account
    def get_all_account(self):
        return self.account