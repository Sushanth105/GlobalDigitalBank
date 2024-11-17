import datetime as dt
import csv

class TransactionManager:
    transaction_log=[]
    log_file_path="services/transaction_log.csv"
    
    try:
        with open(log_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['account_number', 'amount', 'transaction_type', 'date', 'to_account_number'])
    except IOError as e:
        print(f"Error initializing log file: {e}")
        
    @staticmethod
    def get_current_timestamp():
        return dt.datetime.now()
    
    @staticmethod
    def get_current_timestamp():
        return dt.datetime.now()
    
    @classmethod
    def log_transaction(cls, account_number,amount,transaction_type,to_account_number=None):
        transaction_record = {
            'account_number':account_number,
            'amount' : amount,
            'transaction_type' : transaction_type,
            'date' : cls.get_current_timestamp(),
            'to_account_number' : to_account_number
        }
        cls.transaction_log.append(transaction_record)
        
        try:
            with open(cls.log_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    transaction_record['account_number'],
                    transaction_record['amount'],
                    transaction_record['transaction_type'],
                    transaction_record['date'],
                    transaction_record['to_account_number']
                ])
        except IOError as e:
            print(f"Error writing to log file: {e}")