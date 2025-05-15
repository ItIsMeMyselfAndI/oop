import sqlite3
import os

# data holder for a transaction
class Transaction:
    def __init__(self, t_id:int, t_date:str, t_type:str,
                 t_category:str, t_amount:float, t_description:str):
        self.t_id = t_id
        self.t_date = t_date
        self.t_type = t_type
        self.t_category = t_category
        self.t_amount = t_amount
        self.t_description = t_description


class TransactionRepository:
    database = os.path.abspath("../db/transactions.db")
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    @classmethod
    def getAllTransactions(cls, user_id: int) -> list[Transaction]:
        pass
    
    @classmethod
    def getTransactionsByType(cls, user_id: int, t_type: str) -> list[Transaction]:
        pass
    
    @classmethod
    def getTransactionsByCategory(cls, user_id: int, t_category: str) -> list[Transaction]:
        pass
    
    @classmethod
    def addTransaction(cls, user_id: int, transaction: Transaction) -> None:
        # since wla tong display at diretso sa database
        # add mo sa req nito ung pag return ng tuple version ng transaction obj
        pass
    
    @classmethod
    def modifyTransaction(cls, user_id: int, t_id: int, transaction: Transaction) -> None:
        # since wla tong display at diretso sa database
        # add mo sa req nito ung pag return ng tuple version ng transaction obj
        pass
    
    @classmethod
    def deleteTransaction(cls, user_id: int, t_id: int) -> None:
        pass


class TransactionManager:
    def __init__(self):
        self.user_id: int = 1
        # # self.transaction_id: int
        # self.transaction: Transaction
        # self.overall_finance: Finance
        # self.monthly_finances: list<Finance]
        # self.quarterly_finances: list<Finance]
        # self.overall_balance: float

    def runMirasol(self):
        all_t = TransactionRepository.getAllTransactions(user_id=self.user_id)
        t_by_type = TransactionRepository.getTransactionsByType(user_id=self.user_id,
                                                                t_type='Bills')
        # display results
        print("\n[All Transactions]")
        for t in all_t:
            print(f"{t.t_id} | {t.date} | {t.t_type} | {t.t_category} | {t.t_amount} | {t.t_description}")
        print("\n[Type (Bills) Transactions]")
        for t in t_by_type:
            print(f"{t.t_id} | {t.date} | {t.t_type} | {t.t_category} | {t.t_amount} | {t.t_description}")
    
    
    def runNicolas(self):
        # sample new Transaction object
        new_transaction_obj = Transaction(t_id=1, t_date='2025-05-15', t_type='expense',
                                             t_category='Bills', t_amount=1000.0,
                                             t_description='sample description')
        t_by_category = TransactionRepository.getTransactionsByCategory(user_id=self.user_id,
                                                                        t_category='Salary')
        # add new row
        t_tuple = TransactionRepository.addTransaction(user_id=self.user_id,
                                             transaction=new_transaction_obj)
        # display results
        print("\n[Category (Salary) Transactions]")
        for t in t_by_category:
            print(f"{t.t_id} | {t.date} | {t.t_type} | {t.t_category} | {t.t_amount} | {t.t_description}")
        print("\n[Tuple version of Transaction obj]")
        print(t_tuple)

        
    def runAzcarraga(self):
        # sample updated Transaction object
        updated_transaction_obj = Transaction(t_id=1, t_date='2025-05-15', t_type='expense',
                                             t_category='Bills', t_amount=1000.0,
                                             t_description='sample description')
        # modify last row
        t_tuple = TransactionRepository.modifyTransaction(user_id=self.user_id, t_id=1400,
                                                transaction=updated_transaction_obj)
        # delete last row
        TransactionRepository.deleteTransaction(user_id=self.user_id, t_id=1400)
        
        # display results
        print("\n[Tuple version of Transaction obj]")
        print(t_tuple)
    
    
        
if __name__ == "__main__":
    tm = TransactionManager()
    # uncomment nyo if mag sasample run kayo
    # tm.runMirasol()
    # tm.runNicolas()
    # tm.runAzcarraga()
    TransactionRepository.connection.close()