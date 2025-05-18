import sqlite3


# data holder for a transaction
class Transaction:
    def __init__(self, t_date:str, t_type:str, t_category:str,
                 t_amount:float, t_description:str, t_id:int=None):
        self.t_id: int = t_id  #naka default as None (sa "get methods" lng toh mag kakalaman)
        self.t_date: str = t_date
        self.t_type: str = t_type
        self.t_category: str = t_category
        self.t_amount: float = t_amount
        self.t_description: str = t_description


class TransactionRepository:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def getAllTransactions(self, user_id: int) -> list[Transaction]:
        # retrieve transaction data
        table_name = "transactions"
        command = (
            f"SELECT * FROM {table_name} "
            f"WHERE user_id = ?"
        )
        values = (user_id,)
        rows: list[tuple] = self.cursor.execute(command, values).fetchall()
        # convert transaction tuple to obj
        all_transactions: list[Transaction] = []
        for row in rows:
            t = Transaction(t_id=row[0], t_date=row[1], t_type=row[2], t_category=row[3], t_amount=row[4], t_description=row[5])
            all_transactions.append(t)
        # return list of transaction obj
        return all_transactions
    
    def getTransactionsByType(self, user_id: int, t_type: str) -> list[Transaction]:
        # retrieve transaction data
        table_name = "transactions"
        command = (
            f"SELECT * FROM {table_name} "
            "WHERE user_id = ? AND transaction_type = ? "
        )
        values = (user_id, t_type)
        rows: list[tuple] = self.cursor.execute(command, values).fetchall()
        # convert transaction tuple to obj
        type_transactions: list[Transaction] = []
        for row in rows:
            t = Transaction(t_id=row[0], t_date=row[1], t_type=row[2], t_category=row[3], t_amount=row[4], t_description=row[5])
            type_transactions.append(t)
        # return list of transaction obj
        return type_transactions
    
    def getTransactionsByCategory(self, user_id: int, t_category: str) -> list[Transaction]:
        pass
    
    def addTransaction(self, user_id: int, new_transaction: Transaction) -> None:
        command = """
            INSERT INTO transactions (
                transaction_date,
                transaction_type,
                transaction_category,
                transaction_amount,
                transaction_description,
                user_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """
        values = (
            new_transaction.t_date,
            new_transaction.t_type,
            new_transaction.t_category,
            new_transaction.t_amount,
            new_transaction.t_description,
            user_id
        )
        self.cursor.execute(command, values)
        self.connection.commit()

        # get the auto-generated transaction_id
        new_id = self.cursor.lastrowid

        # return "tuple version" of the transaction object
        transaction_tuple = (
            new_id,
            new_transaction.t_date,
            new_transaction.t_type,
            new_transaction.t_category,
            new_transaction.t_amount,
            new_transaction.t_description
        )
        return transaction_tuple
    
    def modifyTransaction(self, user_id: int, t_id: int, updated_transaction: Transaction) -> tuple:
        command = (
            "UPDATE transactions SET "
            "transaction_date = ?, "
            "transaction_type = ?, "
            "transaction_category = ?, "
            "transaction_amount = ?, "
            "transaction_description = ? "
            "WHERE user_id = ? AND transaction_id = ?"  # Use the column name
        )
        values = (
            updated_transaction.t_date, 
            updated_transaction.t_type,
            updated_transaction.t_category,
            updated_transaction.t_amount,
            updated_transaction.t_description,
            user_id,
            t_id
        )
        self.cursor.execute(command, values)
        self.connection.commit()
        return values

    def deleteTransaction(self, user_id: int, t_id: int) -> None:
        pass


class TransactionManager:
    def __init__(self, db_path):
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
        self.repo = TransactionRepository(db_path)

    def testMirasolGetAllTransactions(self):
        all_transactions = self.repo.getAllTransactions(user_id=self.user_id)
        # display results
        print("\n[All Transactions]\n")
        for t in all_transactions:
            print(f" {t.t_id:<10} | {t.t_date:<12} | {t.t_type:<12} | {t.t_category:<20} | {t.t_amount:<10} | {t.t_description}")
    
    def testMirasolGetTransactionByType(self):
        type_transactions = self.repo.getTransactionsByType(user_id=self.user_id, t_type='expense')
        # display results
        print("\n\n[Type (expense) Transactions]\n")
        for t in type_transactions:
            print(f" {t.t_id:<10} | {t.t_date:<12} | {t.t_type:<12} | {t.t_category:<20} | {t.t_amount:<10} | {t.t_description}")
    
    def testNicolasGetTransactionsByCategory(self):
        category_transactions = self.repo.getTransactionsByCategory(user_id=self.user_id, t_category='Salary')
        # display results
        print("\n[Category (Salary) Transactions]\n")
        for t in category_transactions:
            print(f" {t.t_id:<10} | {t.t_date:<13} | {t.t_type:<12} | {t.t_category:<20} | {t.t_amount:<10} | {t.t_description}")
    
    def testNicolasAddTransaction(self):
        # new Transaction obj sample
        new_transaction = Transaction(t_date='2025-05-15', t_type='expense', t_category='Shopping',
                                      t_amount=3000.0, t_description='sample description')
        # add new row to transaction table
        transaction_tuple = self.repo.addTransaction(user_id=self.user_id, new_transaction=new_transaction)
        print("\n\n[Tuple version of Transaction obj]\n")
        print(f"\t{transaction_tuple}")
        # pang check kung na update sa db; dat pareho toh sa tuple moh
        print(self.repo.cursor.execute("SELECT * FROM transactions WHERE transaction_id = 1445").fetchone())
        
    def testAzcarragaModifyTransaction(self):
        # updated Transaction obj sample
        updated_transaction = Transaction(t_date='2025-05-15', t_type='expense', t_category='Education',
                                          t_amount=3000.0, t_description='sample description')
        # modify last row
        transaction_tuple = self.repo.modifyTransaction(user_id=self.user_id, t_id=1440, updated_transaction=updated_transaction)
        # display results
        print("\n[Tuple version of Transaction obj]")
        print(f"\n{transaction_tuple}")
        # pang check kung na update sa db; dat pareho toh sa tuple moh
        print(self.repo.cursor.execute("SELECT * FROM transactions WHERE transaction_id = 1440").fetchone())    

    def testAzcarragaDeleteTransaction(self):
        # delete last row
        self.repo.deleteTransaction(user_id=self.user_id, t_id=1445)
        
    
        
if __name__ == "__main__":
    db_path = "../db/transactions.db"
    tm = TransactionManager(db_path)
    # uncomment nyo inyo if mag sasample run kayo
    # tm.testMirasolGetAllTransactions()
    # tm.testMirasolGetTransactionByType()
    # tm.testNicolasGetTransactionsByCategory()
    tm.testNicolasAddTransaction()
    # tm.testAzcarragaModifyTransaction()
    # tm.testAzcarragaDeleteTransaction()
    tm.repo.connection.close()