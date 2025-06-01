import sqlite3
import customtkinter as ctk
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
from collections import defaultdict
from typing import List


# data holder for a transaction
class Transaction:
    def __init__(self, t_date:str, t_type:str, t_category:str,
                 t_amount:float, t_description:str, t_id:int=None,
                 created_at:datetime=None, updated_at:datetime=None):
        self.t_id: int = t_id  #naka default as None (sa "get methods" lng toh mag kakalaman)
        self.t_date: str = t_date
        self.t_type: str = t_type
        self.t_category: str = t_category
        self.t_amount: float = t_amount
        self.t_description: str = t_description
        self.created_at: datetime = created_at  #naka default as None (sa "get methods" lng toh mag kakalaman)
        self.updated_at: datetime = updated_at  #naka default as None (sa "get methods" lng toh mag kakalaman)


class Finance:
    def __init__(self, total_income:float, total_expenses:float,
                 total_savings:float, total_investment:float):
        self.total_income = total_income
        self.total_expenses = total_expenses
        self.total_savings = total_savings
        self.total_investment = total_investment


class TransactionRepository:
    def __init__(self, db_path):
        print(db_path)
        self.user_id: int = 1
        self.initializeDatabase(db_path)

    def initializeDatabase(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        command_users = """
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                username TEXT UNIQUE NOT NULL, 
                password CHAR(16)
            )
        """
        command_transactions = """
            CREATE TABLE IF NOT EXISTS transactions(
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                transaction_date TEXT,
                transaction_type TEXT,
                transaction_category TEXT,
                transaction_amount REAL,
                transaction_description TEXT,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """
        self.cursor.execute(command_users)
        self.cursor.execute(command_transactions)
        self.cursor.execute("PRAGMA foreign_keys = ON") 
        self.connection.commit()


    def getAllTransactions(self, user_id: int) -> List[Transaction]:
        # retrieve transaction data
        command = """
            SELECT * FROM transactions
            WHERE user_id = ?
        """
        values = (user_id,)
        rows: List[tuple] = self.cursor.execute(command, values).fetchall()
        # convert transaction tuple to obj
        all_transactions: List[Transaction] = []
        for row in rows:
            t = Transaction(t_id=row[0], t_date=row[1], t_type=row[2], t_category=row[3], t_amount=row[4], t_description=row[5], created_at=row[7], updated_at=row[8])
            all_transactions.append(t)
        # return list of transaction obj
        return all_transactions
    
    def getTransactionsByType(self, user_id: int, t_type: str) -> List[Transaction]:
        # retrieve transaction data
        command = """
            SELECT * FROM transactions
            WHERE user_id = ? AND transaction_type = ?
        """
        values = (user_id, t_type)
        rows: List[tuple] = self.cursor.execute(command, values).fetchall()
        # convert transaction tuple to obj
        type_transactions: List[Transaction] = []
        for row in rows:
            t = Transaction(t_id=row[0], t_date=row[1], t_type=row[2], t_category=row[3], t_amount=row[4], t_description=row[5], created_at=row[7], updated_at=row[8])
            type_transactions.append(t)
        # return list of transaction obj
        return type_transactions
    
    def getTransactionsByCategory(self, user_id: int, t_category: str) -> List[Transaction]:
        # kailangan toh para sa table filter ng history page
        pass

    def getRecentTransactions(self, user_id: int, t_count: int) -> List[Transaction]:
        command = """
            SELECT * FROM transactions 
            WHERE user_id = ? 
            ORDER BY created_at DESC, transaction_id DESC 
            LIMIT ?
        """
        values = (user_id, t_count)
        rows: List[tuple] = self.cursor.execute(command, values).fetchall()
            
        # Convert rows to Transaction objects
        recent_transactions: List[Transaction] = []
        for row in rows:
            t = Transaction(t_id=row[0], t_date=row[1], t_type=row[2], t_category=row[3], t_amount=row[4], t_description=row[5], created_at=row[7], updated_at=row[8])
            recent_transactions.append(t)

        return recent_transactions

    def addTransaction(self, user_id: int, new_transaction: Transaction) -> None:
        print(user_id)
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
            round(new_transaction.t_amount, 2),
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
        command = """
            UPDATE transactions SET
                transaction_date = ?, 
                transaction_type = ?,
                transaction_category = ?,
                transaction_amount = ?,
                transaction_description = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE
                user_id = ? AND transaction_id = ?
        """
        values = (
            updated_transaction.t_date, 
            updated_transaction.t_type,
            updated_transaction.t_category,
            round(updated_transaction.t_amount, 2),
            updated_transaction.t_description,
            user_id,
            t_id
        )
        self.cursor.execute(command, values)
        self.connection.commit()
        return values

    # def deleteTransaction(self, user_id: int, t_id: int) -> None:
    #     pass

# ------------------------------- Tests ------------------------------------------

    def testMirasolGetAllTransactions(self):
        all_transactions = self.getAllTransactions(user_id=self.user_id)
        # display results
        print("\n[All Transactions]\n")
        for t in all_transactions:
            print(f" {t.t_id:<10} | {t.t_date:<12} | {t.t_type:<12} | {t.t_category:<20} | {t.t_amount:<10} | {t.t_description} | {t.created_at} | {t.created_at}")
    
    def testMirasolGetTransactionByType(self):
        type_transactions = self.getTransactionsByType(user_id=self.user_id, t_type='expense')
        # display results
        print("\n\n[Type (expense) Transactions]\n")
        for t in type_transactions:
            print(f" {t.t_id:<10} | {t.t_date:<12} | {t.t_type:<12} | {t.t_category:<20} | {t.t_amount:<10} | {t.t_description} | {t.created_at} | {t.created_at}")
    
    def testNicolasGetTransactionsByCategory(self):
        category_transactions = self.getTransactionsByCategory(user_id=self.user_id, t_category='Salary')
        # display results
        print("\n[Category (Salary) Transactions]\n")
        for t in category_transactions:
            print(f" {t.t_id:<10} | {t.t_date:<13} | {t.t_type:<12} | {t.t_category:<20} | {t.t_amount:<10} | {t.t_description} | {t.created_at} | {t.created_at}")
    
    def testAzcarragaGetRecentTransactions(self):
        recent_transactions = self.getRecentTransactions(user_id=self.user_id, t_count=5)
        # display results
        print("\n[Five Recent Transactions]\n")
        for t in recent_transactions:
            print(f" {t.t_id:<10} | {t.t_date:<13} | {t.t_type:<12} | {t.t_category:<20} | {t.t_amount:<10} | {t.t_description} | {t.created_at} | {t.created_at}")
    
    def testNicolasAddTransaction(self):
        # new Transaction obj sample
        new_transaction = Transaction(t_date='2025-05-19', t_type='Expense', t_category='luho',
                                      t_amount=5500.0, t_description='sample description')
        # add new row to transaction table
        transaction_tuple = self.addTransaction(user_id=self.user_id, new_transaction=new_transaction)
        print("\n\n[Tuple version of Transaction obj]\n")
        print(f"\t{transaction_tuple}")
        # pang check kung na update sa db; dat pareho toh sa tuple moh
        print("\t" + self.cursor.execute("SELECT * FROM transactions WHERE transaction_id = 1455").fetchone())
        
    def testAzcarragaModifyTransaction(self):
        # updated Transaction obj sample
        updated_transaction = Transaction(t_date='2025-05-15', t_type='expense', t_category='Education',
                                          t_amount=3000.0, t_description='sample description')
        # modify last row
        transaction_tuple = self.modifyTransaction(user_id=self.user_id, t_id=1440, updated_transaction=updated_transaction)
        # display results
        print("\n[Tuple version of Transaction obj]")
        print(f"\n{transaction_tuple}")
        # pang check kung na update sa db; dat pareho toh sa tuple moh
        print(self.cursor.execute("SELECT * FROM transactions WHERE transaction_id = 1455").fetchone())    

    # def testAzcarragaDeleteTransaction(self):
    #     # delete last row
    #     self.deleteTransaction(user_id=self.user_id, t_id=1445)


class TransactionManager:
    def __init__(self, db_path):
        self.user_id: int = 1
        self.repo = TransactionRepository(db_path)


    def calculateOverallFinance(self, user_id: int) -> Finance:
        transactions = self.repo.getAllTransactions(user_id)

        total_income = 0.0
        total_expenses = 0.0
        total_savings = 0.0
        total_investment = 0.0

        for t in transactions:
            t_type = t.t_type.lower()
            if t_type == "income":
                total_income += t.t_amount
            elif t_type == "expense":
                total_expenses += t.t_amount
            elif t_type == "savings":
                total_savings += t.t_amount
            elif t_type == "investment":
                total_investment += t.t_amount

        return Finance(
            total_income=round(total_income, 2),
            total_expenses=round(total_expenses, 2),
            total_savings=round(total_savings, 2),
            total_investment=round(total_investment, 2)
        )


    def calculateOverallBalance(self, overall_finance: Finance) -> float:
        overall_balance = overall_finance.total_income - overall_finance.total_expenses + overall_finance.total_savings
        return round(overall_balance, 2)


    def calculateMonthlyFinances(self, user_id: int) -> List[Finance]:
        transactions = self.repo.getAllTransactions(user_id)
        monthly_data = defaultdict(lambda: {"income": 0.0, "expense": 0.0, "savings": 0.0, "investment": 0.0})
        month_keys = set()

        # Process all transactions and gather unique months
        for t in transactions:
            try:
                date_obj = datetime.strptime(t.t_date, "%Y-%m-%d")
                month_key = date_obj.strftime("%Y-%m")
                month_keys.add(month_key)
            except ValueError:
                continue  # skip invalid dates

            t_type = t.t_type.lower()
            if t_type in monthly_data[month_key]:
                monthly_data[month_key][t_type] += t.t_amount
        # Determine the full range of months (from earliest to latest transaction)
        if month_keys:
            first_month = min(datetime.strptime(k, "%Y-%m") for k in month_keys)
            last_month = max(datetime.strptime(k, "%Y-%m") for k in month_keys)
            current = first_month
            while current <= last_month:
                key = current.strftime("%Y-%m")
                if key not in monthly_data:
                    monthly_data[key]  # trigger default zero values
                current += timedelta(days=32)
                current = current.replace(day=1)

        # Convert to dictionary of Finance objects, sorted
        monthly_finances = {}
        for month, values in sorted(monthly_data.items()):
            finance = Finance(
                total_income=round(values["income"], 2),
                total_expenses=round(values["expense"], 2),
                total_savings=round(values["savings"], 2),
                total_investment=round(values["investment"], 2)
            )
            monthly_finances[month] = finance

        return monthly_finances


    def calculateQuarterlyFinances(self, user_id: int) -> List[Finance]:
        transactions = self.repo.getAllTransactions(user_id)
        quarterly_data = defaultdict(lambda: {"income": 0.0, "expense": 0.0, "savings": 0.0, "investment": 0.0})
        quarter_keys = set()

        # 1. process all transactions
        for t in transactions:
            try:
                date_obj = datetime.strptime(t.t_date, "%Y-%m-%d")
            except ValueError:
                # skip invalid dates
                continue
            year = date_obj.year
            month = date_obj.month
            # figures out the quarter from the month (1..3 -> Q1, 4..6 -> Q2, etc.)
            quarter = (month - 1) // 3 + 1
            year_quarter = f"{year}-Q{quarter}"
            quarter_keys.add(year_quarter)
            
            t_type = t.t_type.lower()
            if t_type in ["income", "expense", "savings", "investment"]:
                quarterly_data[year_quarter][t_type] += t.t_amount

        # 2. fills in missing quarters. first determine the range from earliest to latest
        def quarter_to_int(y, q):
            return y * 4 + (q - 1)  # 2024-Q1 => 2024*4+0 = 8096

        def int_to_quarter(val):
            y, r = divmod(val, 4)
            return y, r + 1  # e.g. (2024, 1)

        # parse existing quarters to numeric form
        numeric_quarters = []
        for k in quarter_keys:
            y_str, q_str = k.split("-Q")
            y = int(y_str)
            q = int(q_str)
            numeric_quarters.append(quarter_to_int(y, q))

        if numeric_quarters:
            first_qnum = min(numeric_quarters)
            last_qnum = max(numeric_quarters)
            for val in range(first_qnum, last_qnum + 1):
                y, q = int_to_quarter(val)
                key = f"{y}-Q{q}"
                if key not in quarterly_data:
                    # trigger default zero dictionary
                    quarterly_data[key]

        # 3. final dictionary of sorted quarters => Finance
        sorted_quarterly_finances = {}
        all_quarters = sorted(quarterly_data.keys())
        for k in all_quarters:
            values = quarterly_data[k]
            finance = Finance(
                total_income=round(values["income"], 2),
                total_expenses=round(values["expense"], 2),
                total_savings=round(values["savings"], 2),
                total_investment=round(values["investment"], 2)
            )
            sorted_quarterly_finances[k] = finance
        return sorted_quarterly_finances


    def createMonthlyGraph(self, user_id:int, width_in:float, height_in:float,
                           dpi:float, title_size:int, label_size:int) -> tuple[plt.Figure, plt.Figure]:
        monthly_finances = self.calculateMonthlyFinances(user_id=user_id)
        def filter_non_zero(data_dict, attr):
            filtered_months = []
            filtered_values = []
            for month, finance in sorted(data_dict.items()):
                value = getattr(finance, attr)
                if value != 0:
                    filtered_months.append(month)
                    filtered_values.append(value)
            return filtered_months, filtered_values

        # === Income Figure ===
        fig_income = plt.Figure(figsize=(width_in, height_in), dpi=dpi) # 1 in = 100 px
        ax_income = fig_income.add_subplot(111)

        months_inc, incomes = filter_non_zero(monthly_finances, "total_income")
        ax_income.plot(months_inc, incomes, color='green', marker='o', linestyle='-')
        ax_income.set_title("Income", fontsize=title_size)
        ax_income.set_ylabel("Amount (₱)")
        ax_income.tick_params(axis="y", labelsize=label_size)
        ax_income.grid(axis='y')
        ax_income.set_xticks(months_inc)
        ax_income.set_xticklabels(months_inc, rotation=80, ha='center', fontsize=label_size)

        if len(incomes) > 1:
            sorted_incomes = sorted(incomes, reverse=True)
            second_largest = sorted_incomes[1]
            cap = second_largest * 1.1
            if cap < sorted_incomes[0]:
                ax_income.set_ylim(0, cap)

        # === Expenses Figure ===
        fig_expenses = plt.Figure(figsize=(width_in, height_in), dpi=dpi) # 1 in = 100 px
        ax_expenses = fig_expenses.add_subplot(111)

        months_exp, expenses = filter_non_zero(monthly_finances, "total_expenses")
        ax_expenses.plot(months_exp, expenses, color='red', marker='o', linestyle='-')
        ax_expenses.set_title("Expenses", fontsize=title_size)
        ax_expenses.set_ylabel("Amount (₱)")
        ax_expenses.tick_params(axis="y", labelsize=label_size)
        ax_expenses.grid(axis='y')
        ax_expenses.set_xticks(months_exp)
        ax_expenses.set_xticklabels(months_exp, rotation=80, ha='center', fontsize=label_size)

        return fig_income, fig_expenses


    def createQuarterlyGraph(self, quarterly_finances: List[Finance]) -> matplotlib.figure.Figure:
        pass

# ------------------------------- Tests ------------------------------------------

    def testCalculateOverallFinance(self):
        overall_finance = self.calculateOverallFinance(user_id=self.user_id)
        # display result
        print("\n\n[Overall Finance]\n")
        print(f"\ttotal_income: {overall_finance.total_income}")
        print(f"\ttotal_expenses: {overall_finance.total_expenses}")
        print(f"\ttotal_savings: {overall_finance.total_savings}")
        print(f"\ttotal_investment: {overall_finance.total_investment}\n")

    def testCalculateOverallBalance(self):
        overall_finance = self.calculateOverallFinance(user_id=self.user_id)
        overall_balance = self.calculateOverallBalance(overall_finance=overall_finance)
        # display result
        print("\n\n[Overall Balance]\n")
        print(overall_balance)

    def testCalculateMonthlyFinances(self):
        monthly_finances = self.calculateMonthlyFinances(user_id=self.user_id)
        # display result
        print("\n\n[Monthly Finances]\n")
        for year_month, finance in monthly_finances.items():
            print(f"\t{year_month}")
            print(f"\t\ttotal_income: {finance.total_income}")
            print(f"\t\ttotal_expenses: {finance.total_expenses}")
            print(f"\t\ttotal_savings: {finance.total_savings}")
            print(f"\t\ttotal_investment: {finance.total_investment}\n")

    def testCalculateQuarterlyFinances(self):
        quarterly_finances = self.calculateQuarterlyFinances(user_id=self.user_id)
        # display result
        print("\n\n[Quarterly Finances]\n")
        for year_quarter, finance in quarterly_finances.items():
            print(f"\t{year_quarter}")
            print(f"\t\ttotal_income: {finance.total_income}")
            print(f"\t\ttotal_expenses: {finance.total_expenses}")
            print(f"\t\ttotal_savings: {finance.total_savings}")
            print(f"\t\ttotal_investment: {finance.total_investment}\n")

    def testCreateMonthlyGraph(self):
        # display result
        root = ctk.CTk()
        root.title("Monthly Graph")
        root.geometry("1630x1000")
        dpi = root.winfo_fpixels("1i") # px per in
        print(dpi)
        width_in = 780 / dpi
        height_in = 500 / dpi
        graph_income, graph_expenses = self.createMonthlyGraph(user_id=self.user_id,
                                                               width_in=width_in, height_in=height_in, dpi=dpi,
                                                               title_size=20, label_size=15)

        income_frame = ctk.CTkFrame(root) 
        canvas_income = FigureCanvasTkAgg(graph_income, master=income_frame)
        canvas_income.draw()
        canvas_income.get_tk_widget().pack()
        
        expense_frame = ctk.CTkFrame(root) 
        canvas_expenses = FigureCanvasTkAgg(graph_expenses, master=expense_frame)
        canvas_expenses.draw()
        canvas_expenses.get_tk_widget().pack()
        
        income_frame.pack()
        expense_frame.pack()
       
        root.mainloop()



    def testCreateQuarterlyGraph(self):
        root = ctk.CTk()
        root.title("Quarterly Graph")
        root.geometry("700x500")
        dpi = root.winfo_fpixels("1i") # px per in
        quarterly_finances = self.calculateQuarterlyFinances(user_id=self.user_id)
        graph = self.createQuarterlyGraph(quarterly_finances=quarterly_finances)
        # display result
        canvas = FigureCanvasTkAgg(graph, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        root.mainloop()

        
if __name__ == "__main__":

    # db_path = os.path.abspath("../db/transactions.db")
    db_path = Path(__file__).parent.parent / "db/transactions.db"
    print(db_path)
    tm = TransactionManager(db_path)
    # uncomment nyo inyo if magsasample run kayo

    # --- REPOSITORY tests ---
    # tm.repo.testMirasolGetAllTransactions()
    # tm.repo.testMirasolGetTransactionByType()
    # tm.repo.testNicolasGetTransactionsByCategory()
    tm.repo.testAzcarragaGetRecentTransactions()
    # tm.repo.testNicolasAddTransaction()
    # tm.repo.testAzcarragaModifyTransaction()
    # tm.repo.testAzcarragaDeleteTransaction()

    # --- MANAGER tests ---
    # tm.testCalculateOverallFinance()
    # tm.testCalculateOverallBalance()
    # tm.testCalculateMonthlyFinances()
    # tm.testCalculateQuarterlyFinances()
    # tm.testCreateMonthlyGraph()
    # tm.testCreateQuarterlyGraph()

    tm.repo.connection.close()