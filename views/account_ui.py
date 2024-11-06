from services.account_manager import AccountManager
from services.transaction_manager import TransactionManager
from repositories.account_repository import AccountRepository

class AccountUI:
    def start(self):
        while True:
            print('\nWelcome to Global Digital Bank')
            print('\nSelect an option')
            print('1. Open Account')
            print('2. Close Account')
            print('3. Withdraw Fund')
            print('4. Deposit Fund')
            print('5. Transfer Fund')
            print('9. Exit')
            
            choice = int(input("Enter your choice : "))
            
            if choice==1:
                self.open_account()
            elif choice==2:
                self.close_account()
            elif choice==3:
                self.withdraw_fund()
            elif choice==4:
                self.deposit_fund()
            elif choice==5:
                self.transfer_fund()
            elif choice==9:
                break
            else:
                print('Invalid choice. Please try again')

    def open_account(self):
        account_type = input('Enter account type (saving/current): ').strip().lower()
        name = input('Enter your name : ')
        amount = float(input('Enter initial deposit amount: '))
        pin_number=input('Enter your pin number: ')
        privilege = input('Enter account privilege (PREMIUM/GOLD/SILVER): ').strip().upper()
        
    def close_account(self):
        pass
    def withdraw_fund(self):
        pass
    def deposit_fund(self):
        pass
    def transfer_fund(self):
        pass