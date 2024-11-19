# Open Accounts 
# Close Accounts 
# Withdrawl 
# deposit 
# Check if Acccount is active 
# Validate pin number
from models.savings import Savings
from models.current import Current
from repositories.account_repository import AccountRepository
from exceptions.exceptions import AccountNotActiveException
from exceptions.exceptions import InsufficientFundsException
from exceptions.exceptions import InvalidPinException
from exceptions.exceptions import InvalidPrivilegeException
from exceptions.exceptions import TransferLimitExceededException
from services.transaction_manager import TransactionManager
from services.account_privileges_manager import AccountPrivilegesManager
import json

class AccountManager:
    def open_account(self,account_type,**kwargs):
        if account_type == 'saving':
            new_account = Savings(**kwargs)
        elif account_type == 'current':
            new_account=Current(**kwargs)
        else:
            raise ValueError('Invalid account type')
            
        AccountRepository.save_account(account_type,new_account)
        return new_account
    
    def check_account_active(self,account):
        if not account.is_active:
            raise AccountNotActiveException('Account is not Active')
        
    def validate_pin(self,account,pin_number):
        if int(account.pin_number) != int(pin_number):
            raise InvalidPinException('Invalid pin')
        
    def withdraw(self,account,amount,pin_number):
        self.check_account_active(account)
        self.validate_pin(account,pin_number)
        
        if account.balance < amount:
            raise InsufficientFundsException('Insufficient fund')
        
        account.balance -= amount
        TransactionManager.log_transaction(account.account_number,amount,'withdraw')
        
    def deposit(self,account,amount):
        self.check_account_active(account)
            
        account.balance += amount
        TransactionManager.log_transaction(account.account_number,amount,'deposit')
    
    def transfer(self,from_account,to_account,amount,pin_number):
        self.check_account_active(from_account)
        self.check_account_active(to_account)
        self.validate_pin(from_account,pin_number)
        
        if from_account.balance<amount:
            raise InsufficientFundsException('Insufficient fund')
        
        limit = AccountPrivilegesManager.get_transfer_limit(from_account.privilege)
        if amount>limit:
            raise TransferLimitExceededException('Transfer limit exceeded')
        
        from_account.balance -= amount
        to_account.balance += amount
        TransactionManager.log_transaction(from_account.account_number,amount,'transfered',to_account.account_number)
        
    def close_account(self,account):
        if not account.is_active:
            raise AccountNotActiveException('Account is already Deactivated')
        account.is_active=False
        
    def get_transfer_limit(self,account):
        if not account.privilege in AccountPrivilegesManager.privileges :
            raise InvalidPrivilegeException('Invalid Privilege')
        
        return AccountPrivilegesManager.get_transfer_limit(account.privilege)
    
    try:
        with open("services/Privilege_limit.json", mode='w', newline='') as file:
            json.dump(AccountPrivilegesManager.privileges,file,indent=4)
    except IOError as e:
        print(f"Error initializing log file: {e}")
        
    
    def change_transfer_limit(self,privilege,limit):
        if not privilege in AccountPrivilegesManager.privileges :
            raise InvalidPrivilegeException('Invalid Privilege')
        if not limit>0:
            raise ValueError('Limit should be greater than 0')
        
        AccountPrivilegesManager.privileges[privilege]=limit
        
        try:
            with open("services/Privilege_limit.json", mode='w', newline='') as file:
                json.dump(AccountPrivilegesManager.privileges,file,indent=4)
        except IOError as e:
            print(f"Error initializing log file: {e}")
            
    def check_withdrawal_count(self,date):
        i=0
        for tr in TransactionManager.transaction_log:
            if date in tr['date'] and tr['transaction_type'] == 'withdraw':
                i +=1
        return i
    
    def check_closed_account_count(self):
        i=0
        for acc in AccountRepository.account:
            if not acc.is_active:
                i +=1
        return i
    
    def check_transfer_count(self,limit):
        i=0
        for tr in TransactionManager.transaction_log:
            if tr['transaction_type'] == 'transfered' and tr['amount'] > limit:
                i +=1
        return i
    
    def check_transaction_count(self,account_type):
        if account_type not in ['saving','current']:
            raise ValueError('Invalid account type')
        i=0
        for acc in TransactionManager.transaction_log:
            if acc['account_type'] == account_type:
                i +=1
        return i