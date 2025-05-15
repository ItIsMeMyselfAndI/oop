import sqlite3


# data holder for a transaction
class Transaction:
    def __init__(self, t_date:str, t_type:str, t_category:str,
                 t_amount:float, t_description:str, t_id:int=None):
        self.t_id: int = t_id  #naka default to None (sa "get methods" lng toh mag kakalaman)
        self.t_date: str = t_date
        self.t_type: str = t_type
        self.t_category: str = t_category
        self.t_amount: float = t_amount
        self.t_description: str = t_description


class TransactionRepository:
    database = "../db/transactions.db"
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    @classmethod
    def getAllTransactions(cls, user_id: int) -> list[Transaction]:
        # retrieve transaction data
        table_name = "transactions"
        command = (
            f"SELECT * FROM {table_name}\n"
            f"WHERE user_id = {user_id}"
        )
        rows: list[tuple] = cls.cursor.execute(command)
        # convert transaction tuple to obj
        all_transactions: list[Transaction] = []
        for row in rows:
            t = Transaction(t_id=row[0], t_date=row[1], t_type=row[2],
                            t_category=row[3], t_amount=row[4], t_description=row[5])
            all_transactions.append(t)
        # return list of transaction obj
        return all_transactions
    
    @classmethod
    def getTransactionsByType(cls, user_id: int, t_type: str) -> list[Transaction]:
        # retrieve transaction data
        table_name = "transactions"
        command = (
            f"SELECT * FROM {table_name}\n"
            f"WHERE user_id = {user_id} AND transaction_type = '{t_type}'"
        )
        rows: list[tuple] = cls.cursor.execute(command)
        # convert transaction tuple to obj
        type_transactions: list[Transaction] = []
        for row in rows:
            t = Transaction(t_id=row[0], t_date=row[1], t_type=row[2],
                            t_category=row[3], t_amount=row[4], t_description=row[5])
            type_transactions.append(t)
        # return list of transaction obj
        return type_transactions
    
    @classmethod
    def getTransactionsByCategory(cls, user_id: int, t_category: str) -> list[Transaction]:
        pass
    
    @classmethod
    def addTransaction(cls, user_id: int, transaction: Transaction) -> None:
        # wag mo pla sama ung {t_id} sa pag insert sa database
        # since c database na mag gegenerate nun automatically.
        # and since wla tong display at diretso sa database
        # add mo sa req nito ung pag return ng tuple version ng transaction obj
        pass
    
    @classmethod
    def modifyTransaction(cls, user_id: int, t_id: int, transaction: Transaction) -> None:
        # wag mo pla galawin ung {t_id} sa row na momodify mo sa database
        # gamitin mo lng {t_id} as condition
        # and since wla tong display at diretso sa database
        # add mo sa req nito ung pag return ng tuple version ng transaction obj
        pass
    
    @classmethod
    def deleteTransaction(cls, user_id: int, t_id: int) -> None:
        pass


class TransactionManager:
    def __init__(self):
        self.user_id: int = 1
        # self.categories_by_type = {
        #     "expense": ["Bills", "Education", "Entertainment",
        #                 "Food & Drinks", "Grocery", "Healthcare",
        #                 "House", "Shopping", "Transportation",
        #                 "Wellness", "Other"],
        #     "savings": ["Monthly Allowance", "Change", "Miscellaneous"],
        #     "investment": ["Stocks", "Crypto", "Bonds", "Real Estate"],
        #     "income": ["Salary", "Bonus", "Side-hustles", "Tips"]
        # }
        # self.transaction_id: int
        # self.transaction: Transaction
        # self.overall_finance: Finance
        # self.monthly_finances: list<Finance]
        # self.quarterly_finances: list<Finance]
        # self.overall_balance: float

    def testMirasol(self):
        all_transactions = TransactionRepository.getAllTransactions(user_id=self.user_id)
        type_transactions = TransactionRepository.getTransactionsByType(user_id=self.user_id,
                                                                        t_type='expense')
        # display results
        print("\n[All Transactions]\n")
        for t in all_transactions:
            print(f" {t.t_id:<10} | {t.t_date:<10} | {t.t_type:<10} | {t.t_category:<20} | {t.t_amount:<10} | {t.t_description}")
        print("\n\n[Type (expense) Transactions]\n")
        for t in type_transactions:
            print(f" {t.t_id:<10} | {t.t_date:<10} | {t.t_type:<10} | {t.t_category:<20} | {t.t_amount:<10} | {t.t_description}")
    
    
    def testNicolas(self):
        # new Transaction obj sample
        new_transaction = Transaction(t_date='2025-05-15', t_type='expense',
                                      t_category='Bills', t_amount=3000.0,
                                      t_description='sample description')
        category_transactions = TransactionRepository.getTransactionsByCategory(user_id=self.user_id,
                                                                                t_category='Salary')
        # add new row to transaction table
        transaction_tuple = TransactionRepository.addTransaction(user_id=self.user_id,
                                                                 transaction=new_transaction)
        # display results
        print("\n[Category (Salary) Transactions]\n")
        for t in category_transactions:
            print(f" {t.t_id:<10} | {t.t_date:<10} | {t.t_type:<10} | {t.t_category:<20} | {t.t_amount:<10} | {t.t_description}")
        print("\n\n[Tuple version of Transaction obj]\n")
        print(f"\t{transaction_tuple}")

        
    def testAzcarraga(self):
        # updated Transaction obj sample
        updated_transaction = Transaction(t_date='2025-05-15', t_type='expense',
                                          t_category='Bills', t_amount=3000.0,
                                          t_description='sample description')
        # modify last row
        transaction_tuple = TransactionRepository.modifyTransaction(user_id=self.user_id, t_id=1440,
                                                                    transaction=updated_transaction)
        # delete last row
        TransactionRepository.deleteTransaction(user_id=self.user_id, t_id=1440)
        
        # display results
        print("\n[Tuple version of Transaction obj]")
        print(f"\n{transaction_tuple}")
    
    
        
if __name__ == "__main__":
    tm = TransactionManager()
    # uncomment nyo if mag sasample run kayo
    # tm.testMirasol()
    # tm.testNicolas()
    # tm.testAzcarraga()
    TransactionRepository.connection.close()