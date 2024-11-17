from services.account_manager import AccountManager
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
            print('6. Check Transfer Limit')
            print('7. Set Transfer Limit')
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
            elif choice==6:
                self.check_transfer_limit()
            elif choice==7:
                self.set_transfer_limit()
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
        
        if account_type =='saving':
            date_of_birth=input('Enter your date of birth (YYYY-MM-DD)')
            gender = input('Enter your gender (M/F):')
            account = AccountManager().open_account(account_type, name=name, balance=amount,date_of_birth=date_of_birth, gender=gender, pin_number=pin_number, privilege=privilege)
            
        elif account_type == 'current':
            registration_number = input('Enter your registration number: ')
            website_url= input('Enter your website URL: ')
            account = AccountManager().open_account(account_type, name=name, balance=amount,registration_number=registration_number, website_url=website_url, pin_number=pin_number,privilege=privilege)
            
        else:
            print('Invalid account type. Please try again')
            return
        
        print(account_type.capitalize(), 'Account opened successfully. Account Number: ', account.account_number)
              
    def close_account(self):
        account_number = int(input('Enter your account number: '))
        account = next((acc for acc in AccountRepository.account if acc.account_number == account_number),None)
        
        if account:
            try:
                AccountManager().close_account(account)
                print('Account closed successfully')
            except Exception as e:
                print("Error: ", e)
                
        else:
            print('Account Not Found. Please try again')
            
    def withdraw_fund(self):
        account_number = int(input('Enter your account number: '))
        amount = float(input('Enter amount to withdraw: '))
        pin_number = int(input('Enter your pin number: '))
        account=next((acc for acc in AccountRepository.account if acc.account_number == account_number),None)
        
        if account:
            try:
                AccountManager().withdraw (account, amount, pin_number)
                print('Amount withdrawn successfully')
            except Exception as e:
                print('Error: ', e)
                
        else:
            print('Account Not Found. Please try again')
    def deposit_fund(self):
        account_number = int(input('Enter your account number: '))
        amount = float(input('Enter amount to deposit: '))
        account = next((acc for acc in AccountRepository.account if acc.account_number == account_number), None)
        
        if account:
            try:
                AccountManager().deposit(account, amount)
                print('Amount deposited successfully')
            except Exception as e:
                print('Error: ', e)
            
        else:
            print('Account Not Found. Please try again')
            
    def transfer_fund(self):
        from_account_number = int(input('Enter your account number: '))
        pin_number = int(input('Enter your pin number: '))
        to_account_number = int(input('Enter reciever account number: '))
        amount = float(input('Enter amount to deposit: '))
        from_account = next((acc for acc in AccountRepository.account if acc.account_number == from_account_number), None)
        to_account = next((acc for acc in AccountRepository.account if acc.account_number == to_account_number), None)
        
        if from_account and to_account:
            try:
                AccountManager().transfer(from_account,to_account,amount,pin_number)
                print('Amount transfered successfully')
            except Exception as e:
                print('Error: ', e)
            
        else:
            print('Account Not Found. Please try again')
            
    def check_transfer_limit(self):
        account_number= int(input('Enter your account number: '))
        account = next((acc for acc in AccountRepository.account if acc.account_number == account_number), None)
        if account:
            try:
                print('Transfer Limit: ',AccountManager().get_transfer_limit(account))
            except Exception as e:
                print('Error: ', e)
        else:
            print('Account Not Found. Please try again')
            
    def set_transfer_limit(self):
        password='Password'
        privilege= input('Enter the privilege(PREMIUM/GOLD/SILVER): ').strip().upper()
        limit=int(input("Enter the new limit: "))
        authenticate=input("Enter the password: ")
        if authenticate==password:
            try:
                AccountManager().change_transfer_limit(privilege,limit)
                print('Transfer Limit changed successfully')
            except Exception as e:
                print('Error: ', e) 
        else:
            print('Invalid Password. Please try again')