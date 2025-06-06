import sqlite3
from pathlib import Path
import os
from datetime import datetime


# data holder for a user
class Account:
    def __init__(self, username, password):
        self.username: str = username
        self.password: str = password


class UserRepository:
    def __init__(self, db_folder, db_name):
        os.makedirs(db_folder, exist_ok=True)
        self.connection = sqlite3.connect(db_folder + "/" + db_name)
        self.cursor = self.connection.cursor()
        self.initializeDatabase()

    def initializeDatabase(self):
        command_users = """
        CREATE TABLE IF NOT EXISTS "users"(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password CHAR(16),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
        command_transactions = """
        CREATE TABLE IF NOT EXISTS "transactions"(
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_date TEXT,
            transaction_type TEXT,
            transaction_category TEXT,
            transaction_amount REAL,
            transaction_description TEXT,
            user_id INTEGER,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )        
        """
        self.cursor.execute(command_users)
        self.cursor.execute(command_transactions)
        self.cursor.execute("PRAGMA foreign_keys = ON") 
        self.connection.commit()

    def addAccount(self, account: Account) -> bool:
        was_added = False
        command = """
            SELECT 1 FROM users
            WHERE username = ? LIMIT 1
        """
        values = (account.username,)
        username_exists = self.cursor.execute(command, values).fetchone()
        # check if username doesn't exist and if not empty fields
        if not username_exists and account.username and account.password:
            command = """
                INSERT INTO users(
                    username, password, created_at, updated_at
                )
                VALUES (?, ?, ?, ?)
            """
            local_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            values = (account.username, account.password, local_time, local_time)
            # add account
            self.cursor.execute(command, values)
            self.connection.commit()
            was_added = True
        return was_added


    def getAccountID(self, account: Account) -> int:
        command = """
            SELECT user_id FROM users
            WHERE username = ? AND password = ? LIMIT 1
        """
        values = (account.username, account.password)
        user_id = self.cursor.execute(command, values).fetchone()
        if user_id:
            user_id = user_id[0]
        return user_id

# ------------------------------- Tests ------------------------------------------

    def testAddAccount(self):
        account = Account(username="jone doe", password="jonedoe123")
        was_added = self.addAccount(account)
        print("\n\n[Recently Added user Row]\n")
        if not was_added:
            print(f"\tUsername already exist")
            return
        command = """
            SELECT * FROM users
            ORDER BY created_at DESC
            LIMIT ?
        """
        values = (1,)
        # check if reflected in db
        result = self.cursor.execute(command, values).fetchone()
        print(f"\t{result = }")

    def testGetAccountID(self):
        account = Account(username="jone", password="jonedoe123")
        user_id = self.getAccountID(account)
        print(f"\n\n[{account.username} Account ID]\n")
        if user_id:
            print(f"\t{user_id = }")
        else:
            print("\tNo Match Found")





if __name__ == "__main__":

    # db_path = os.path.abspath("../db/transactions.db")
    db_path = Path(__file__).parent.parent / "db/transactions.db"
    print(db_path)
   
    userRepo = UserRepository(db_path)

    # --- USER REPOSITORY TESTS ---
    # userRepo.testAddAccount()
    # userRepo.testGetAccountID()
    
    userRepo.connection.close()