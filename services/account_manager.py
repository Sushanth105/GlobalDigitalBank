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
from exceptions.exceptions import TransferLimitExceededException
from services.transaction_manager import TransactionManager
from services.account_privileges_manager import AccountPrivilegesManager

class AccountManager:
    def open_account(self,account_type,**kwargs):
        if account_type == 'saving':
            new_account = Savings(**kwargs)
        elif account_type == 'current':
            new_account=Current(**kwargs)
        else:
            raise ValueError('Invalid account type')
            
        AccountRepository.save_account(new_account)
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