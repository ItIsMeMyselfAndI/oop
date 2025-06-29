import sqlite3
import customtkinter as ctk
import matplotlib.pyplot as plt
from pathlib import Path
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
from collections import defaultdict
from typing import List, Dict


#--------------------------------------------------------------------------------------------------------


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


#--------------------------------------------------------------------------------------------------------


# data holder for a finance
class Finance:
    def __init__(self, total_income:float, total_expenses:float,
                 total_savings:float, total_investment:float):
        self.total_income = total_income
        self.total_expenses = total_expenses
        self.total_savings = total_savings
        self.total_investment = total_investment


#--------------------------------------------------------------------------------------------------------


class TransactionRepository:
    def __init__(self, db_path):
        print(db_path)
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.user_id = 1 # dummy
    
    
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
            t = Transaction(
                t_id=row[0],
                t_date=row[1],
                t_type=row[2],
                t_category=row[3],
                t_amount=row[4],
                t_description=row[5],
                created_at=row[7],
                updated_at=row[8]
            )
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
            t = Transaction(
                t_id=row[0],
                t_date=row[1],
                t_type=row[2],
                t_category=row[3],
                t_amount=row[4],
                t_description=row[5],
                created_at=row[7],
                updated_at=row[8]
            )
            type_transactions.append(t)
        # return list of transaction obj
        return type_transactions
    
    
    def getTransactionsByCategory(self, user_id: int, t_category: str) -> List[Transaction]:
        # retrieve transaction data
        command = """
            SELECT * FROM transactions
            WHERE user_id = ? AND transaction_category = ?
        """
        values = (user_id, t_category)
        rows = self.cursor.execute(command, values).fetchall()
        # convert transaction tuple to obj
        category_transactions: List[Transaction] = []
        for row in rows:
            t = Transaction(
                t_id=row[0],
                t_date=row[1],
                t_type=row[2],
                t_category=row[3],
                t_amount=row[4],
                t_description=row[5],
                created_at=row[7],
                updated_at=row[8]
            )
            category_transactions.append(t)
        # return list of transaction obj
        return category_transactions

    
    def getRecentTransactions(self, user_id: int, t_count: int) -> List[Transaction]:
        command = """
            SELECT * FROM transactions 
            WHERE user_id = ? 
            ORDER BY transaction_date DESC, transaction_id DESC 
            LIMIT ?
        """
        values = (user_id, t_count)
        rows: List[tuple] = self.cursor.execute(command, values).fetchall()
            
        # Convert rows to Transaction objects
        recent_transactions: List[Transaction] = []
        for row in rows:
            t = Transaction(
                t_id=row[0],
                t_date=row[1],
                t_type=row[2],
                t_category=row[3],
                t_amount=row[4],
                t_description=row[5],
                created_at=row[7],
                updated_at=row[8]
            )
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
                user_id, created_at, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        local_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        values = (
            new_transaction.t_date,
            new_transaction.t_type,
            new_transaction.t_category,
            round(new_transaction.t_amount, 2),
            new_transaction.t_description,
            user_id, local_time, local_time
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
                updated_at = ?
            WHERE
                user_id = ? AND transaction_id = ?
        """
        local_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        values = (
            updated_transaction.t_date, 
            updated_transaction.t_type,
            updated_transaction.t_category,
            round(updated_transaction.t_amount, 2),
            updated_transaction.t_description,
            local_time,
            user_id, t_id
        )
        self.cursor.execute(command, values)
        self.connection.commit()
        return values


#--------------------------------------------------------------------------------------------------------


class TransactionManager:
    def __init__(self, db_path):
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


    def calculateMonthlyFinances(self, user_id: int) -> Dict[str, Finance]:
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
        for month, values in sorted(monthly_data.items())[-12:]: # latest 12 months
            finance = Finance(
                total_income=round(values["income"], 2),
                total_expenses=round(values["expense"], 2),
                total_savings=round(values["savings"], 2),
                total_investment=round(values["investment"], 2)
            )
            monthly_finances[month] = finance

        return monthly_finances


    def calculateQuarterlyFinances(self, user_id: int) -> Dict[str, Finance]:
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
        all_quarters = sorted(quarterly_data.keys())[-4:] # latest 4 quarters
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


    def createMonthlyGraphs(self, user_id:int, width_in:float, height_in:float, dpi:float, title_size:int, label_size:int) -> tuple[plt.Figure, plt.Figure]:
        monthly_finances = self.calculateMonthlyFinances(user_id=user_id)
        months = list(monthly_finances.keys())
        incomes = [] 
        expenses = []
        for m in months:
            finance_data: Finance = monthly_finances[m]
            incomes.append(finance_data.total_income)
            expenses.append(finance_data.total_expenses)
        
        # === Income Figure ===
        fig_income = plt.Figure(figsize=(width_in, height_in), dpi=dpi) # 1 in = 100 px
        ax_income = fig_income.add_subplot(111)
        
        ax_income.plot(months, incomes, color='green', marker='o', linestyle='-')
        ax_income.set_title("Income", fontsize=title_size)
        ax_income.set_ylabel("Amount (₱)", fontsize=label_size)
        ax_income.set_xlabel("Months", fontsize=label_size)
        ax_income.set_xticks(range(len(months)))
        ax_income.set_xticklabels(months, rotation=45, ha='center', fontsize=label_size)
        ax_income.tick_params(axis="both", labelsize=label_size)
        ax_income.grid(True, linestyle='--', alpha=0.6)
        fig_income.tight_layout()

        # === Expenses Figure ===
        fig_expenses = plt.Figure(figsize=(width_in, height_in), dpi=dpi) # 1 in = 100 px
        ax_expenses = fig_expenses.add_subplot(111)

        ax_expenses.plot(months, expenses, color='red', marker='o', linestyle='-')
        ax_expenses.set_title("Expenses", fontsize=title_size)
        ax_expenses.set_ylabel("Amount (₱)", fontsize=label_size)
        ax_expenses.set_xlabel("Months", fontsize=label_size)
        ax_expenses.set_xticks(range(len(months)))
        ax_expenses.set_xticklabels(months, rotation=45, ha='center', fontsize=label_size)
        ax_expenses.tick_params(axis="both", labelsize=label_size)
        ax_expenses.grid(True, linestyle='--', alpha=0.6)
        fig_expenses.tight_layout()

        return fig_income, fig_expenses


    def createQuarterlyGraph(self, user_id:int, width_in:float, height_in:float, dpi:float, title_size:int, label_size:int) -> plt.Figure:
        quarterly_finances = self.calculateQuarterlyFinances(user_id=user_id)
        fig, ax = plt.subplots(figsize=(width_in, height_in), dpi=dpi)
        quarters = list(quarterly_finances.keys())
        
        incomes = []
        expenses = []
        savings = []
        investments = []

        for q in quarters:
            finance_data: Finance = quarterly_finances[q]
            
            incomes.append(finance_data.total_income)
            expenses.append(finance_data.total_expenses)
            savings.append(finance_data.total_savings)
            investments.append(finance_data.total_investment)

        ax.plot(quarters, incomes, color='green', marker='o', linestyle='-', label="Income")
        ax.plot(quarters, expenses, color='red', marker='o', linestyle='-', label="Expenses")
        ax.plot(quarters, savings, color='blue', marker='o', linestyle='-', label="Savings")
        ax.plot(quarters, investments, color='orange', marker='o', linestyle='-', label="Investment")

        ax.set_ylabel("Amount (₱)", fontsize=label_size)
        ax.set_xlabel("Quarters", fontsize=label_size)
        ax.set_xticks(range(len(quarters)))
        ax.set_xticklabels(quarters, ha='center', fontsize=label_size)
        ax.tick_params(axis="both", labelsize=label_size)
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()

        fig.tight_layout()
        return fig


#--------------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    # db_path = os.path.abspath("../db/transactions.db")
    db_path = Path(__file__).parent.parent / "db/transactions.db"
    print(db_path)


    t_man = TransactionManager(db_path)
    
    # --- TRANSACTION REPOSITORY tests ---
    # t_man.repo.testGetAllTransactions()
    # t_man.repo.testGetTransactionByType()
    # t_man.repo.testGetTransactionsByCategory()
    # t_man.repo.testGetRecentTransactions()
    # t_man.repo.testAddTransaction()
    # t_man.repo.test_manodifyTransaction()
    # t_man.repo.testDeleteTransaction()

    # --- TRANSACTION MANAGER tests ---
    # t_man.testCalculateOverallFinance()
    # t_man.testCalculateOverallBalance()
    # t_man.testCalculateMonthlyFinances()
    # t_man.testCalculateQuarterlyFinances()
    # t_man.testCreateMonthlyGraph()
    # t_man.testCreateQuarterlyGraph()

    t_man.repo.connection.close()
    exit(0)