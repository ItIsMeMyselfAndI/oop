import sqlite3
import customtkinter as ctk
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
from collections import defaultdict
import os


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


class Finance:
    def __init__(self, total_income:float, total_expenses:float,
                 total_savings:float, total_investment:float):
        self.total_income = total_income
        self.total_expenses = total_expenses
        self.total_savings = total_savings
        self.total_investment = total_investment


class TransactionRepository:
    def __init__(self, db_path):
        self.user_id: int = 1
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.createTablesIfNotExist()

    def createTablesIfNotExist(self):
        command_users = (
            "CREATE TABLE IF NOT EXISTS users ( "
            "    user_id INTEGER PRIMARY KEY AUTOINCREMENT, " 
            "    username TEXT UNIQUE NOT NULL, " 
            "    password CHAR(16) "
            ")"
        )
        command_transactions = (
            "CREATE TABLE IF NOT EXISTS transactions( "
            "    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "    transaction_date TEXT, "
            "    transaction_type TEXT, "
            "    transaction_category TEXT, "
            "    transaction_amount REAL, "
            "    transaction_description TEXT, "
            "    user_id INTEGER, "
            "    FOREIGN KEY (user_id) REFERENCES users(user_id) "
            ")"
        )
        self.cursor.execute(command_users)
        self.cursor.execute(command_transactions)
        self.cursor.execute("PRAGMA foreign_keys = ON") 
        self.connection.commit()


    def getAllTransactions(self, user_id: int) -> list[Transaction]:
        # retrieve transaction data
        command = (
            "SELECT * FROM transactions "
            "WHERE user_id = ?"
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
        command = (
            "SELECT * FROM transactions "
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
            round(updated_transaction.t_amount, 2),
            updated_transaction.t_description,
            user_id,
            t_id
        )
        self.cursor.execute(command, values)
        self.connection.commit()
        return values

    def deleteTransaction(self, user_id: int, t_id: int) -> None:
        pass

# ------------------------------- Tests ------------------------------------------

    def testMirasolGetAllTransactions(self):
        all_transactions = self.getAllTransactions(user_id=self.user_id)
        # display results
        print("\n[All Transactions]\n")
        for t in all_transactions:
            print(f" {t.t_id:<10} | {t.t_date:<12} | {t.t_type:<12} | {t.t_category:<20} | {t.t_amount:<10} | {t.t_description}")
    
    def testMirasolGetTransactionByType(self):
        type_transactions = self.getTransactionsByType(user_id=self.user_id, t_type='expense')
        # display results
        print("\n\n[Type (expense) Transactions]\n")
        for t in type_transactions:
            print(f" {t.t_id:<10} | {t.t_date:<12} | {t.t_type:<12} | {t.t_category:<20} | {t.t_amount:<10} | {t.t_description}")
    
    def testNicolasGetTransactionsByCategory(self):
        category_transactions = self.getTransactionsByCategory(user_id=self.user_id, t_category='Salary')
        # display results
        print("\n[Category (Salary) Transactions]\n")
        for t in category_transactions:
            print(f" {t.t_id:<10} | {t.t_date:<13} | {t.t_type:<12} | {t.t_category:<20} | {t.t_amount:<10} | {t.t_description}")
    
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

    def testAzcarragaDeleteTransaction(self):
        # delete last row
        self.deleteTransaction(user_id=self.user_id, t_id=1445)


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

    def calculateMonthlyFinances(self, user_id: int) -> list[Finance]:
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

    def calculateQuarterlyFinances(self, user_id: int) -> list[Finance]:
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

    def createMonthlyGraph(self, monthly_finances: list[Finance]) -> matplotlib.figure.Figure:
        def filter_non_zero(data_dict, attr):
            filtered_months = []
            filtered_values = []
            for month, finance in sorted(data_dict.items()):
                value = getattr(finance, attr)
                if value != 0:
                    filtered_months.append(month)
                    filtered_values.append(value)
            return filtered_months, filtered_values

        fig, axs = plt.subplots(4, 1, figsize=(14, 12), sharex=False)

        # Remove top and bottom borders from all subplots
        for ax in axs:
            ax.spines['top'].set_visible(False)
            ax.spines['bottom'].set_visible(False)

        # Income
        months_inc, incomes = filter_non_zero(monthly_finances, "total_income")
        bars_income = axs[0].bar(months_inc, incomes, color='blue')
        axs[0].set_title("Income")
        axs[0].set_ylabel("Amount")
        axs[0].grid(axis='y')

        # Cap Income y-axis
        if len(incomes) > 1:
            sorted_incomes = sorted(incomes, reverse=True)
            second_largest = sorted_incomes[1]
            cap = second_largest * 1.1
            if cap < sorted_incomes[0]:
                axs[0].set_ylim(0, cap)

        # Expenses
        months_exp, expenses = filter_non_zero(monthly_finances, "total_expenses")
        bars_expenses = axs[1].bar(months_exp, expenses, color='orange')
        axs[1].set_title("Expenses")
        axs[1].set_ylabel("Amount")
        axs[1].grid(axis='y')

        # Savings
        months_sav, savings = filter_non_zero(monthly_finances, "total_savings")
        bars_savings = axs[2].bar(months_sav, savings, color='green')
        axs[2].set_title("Savings")
        axs[2].set_ylabel("Amount")
        axs[2].grid(axis='y')

        # Investments
        months_inv, investments = filter_non_zero(monthly_finances, "total_investment")
        bars_investments = axs[3].bar(months_inv, investments, color='red')
        axs[3].set_title("Investments")
        axs[3].set_ylabel("Amount")
        axs[3].set_xlabel("Month")
        axs[3].grid(axis='y')

        plt.suptitle("Monthly Finances Overview", fontsize=16)
        plt.tight_layout(rect=[0, 0, 1, 0.96])

        def human_format(num):
            for unit in ['', 'K', 'M', 'B', 'T']:
                if abs(num) < 1000:
                    return f"{num:.0f}{unit}"
                num /= 1000
            return f"{num:.0f}P"

        def annotate_bars(ax, bars, values, months):
            ax.set_xticks([bar.get_x() + bar.get_width() / 2 for bar in bars])
            ax.set_xticklabels(months, rotation=0)

            bar_heights = [bar.get_height() for bar in bars]
            max_bar_height = max(bar_heights) if bar_heights else 0
            padding_above = max_bar_height * 0.08  # 8% headroom above tallest bar
            ax.set_ylim(top=max_bar_height + padding_above)

            for bar, val in zip(bars, values):
                height = bar.get_height()
                x_pos = bar.get_x() + bar.get_width() / 2

                if height == 0:
                    continue  # Skip zero bars

                # Label position logic
                if height >= max_bar_height * 0.92:
                    y_pos = height + padding_above * 0.5
                    va = 'bottom'
                else:
                    y_pos = height * 0.5
                    va = 'center'

                ax.annotate(
                    human_format(float(val)),
                    xy=(x_pos, y_pos),
                    ha='center',
                    va=va,
                    fontsize=9,
                    color='black',
                    clip_on=False
                )

        annotate_bars(axs[0], bars_income, incomes, months_inc)
        annotate_bars(axs[1], bars_expenses, expenses, months_exp)
        annotate_bars(axs[2], bars_savings, savings, months_sav)
        annotate_bars(axs[3], bars_investments, investments, months_inv)

        # plt.show()
        return fig

    def createQuarterlyGraph(self, quarterly_finances: list[Finance]) -> matplotlib.figure.Figure:
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
        monthly_finances = self.calculateMonthlyFinances(user_id=self.user_id)
        graph = self.createMonthlyGraph(monthly_finances=monthly_finances)
        # display result
        root = ctk.CTk()
        root.title("Monthly Graph")
        root.geometry("1920x1080")
        canvas = FigureCanvasTkAgg(graph, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        root.mainloop()

    def testCreateQuarterlyGraph(self):
        quarterly_finances = self.calculateQuarterlyFinances(user_id=self.user_id)
        graph = self.createQuarterlyGraph(quarterly_finances=quarterly_finances)
        # display result
        root = ctk.CTk()
        root.title("Quarterly Graph")
        root.geometry("1920x1080")
        canvas = FigureCanvasTkAgg(graph, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        root.mainloop()

        
if __name__ == "__main__":

    db_path = Path(__file__).resolve().parent.parent / "db" / "transactions.db"
    tm = TransactionManager(db_path)
    # uncomment nyo inyo if magsasample run kayo

    # --- REPOSITORY tests ---
    # tm.repo.testMirasolGetAllTransactions()
    # tm.repo.testMirasolGetTransactionByType()
    # tm.repo.testNicolasGetTransactionsByCategory()
    # tm.repo.testNicolasAddTransaction()
    # tm.repo.testAzcarragaModifyTransaction()
    # tm.repo.testAzcarragaDeleteTransaction()

    # --- MANAGER tests ---
    # tm.testCalculateOverallFinance()
    # tm.testCalculateOverallBalance()
    # tm.testCalculateMonthlyFinances()
    # tm.testCalculateQuarterlyFinances()
    tm.testCreateMonthlyGraph()
    # tm.testCreateQuarterlyGraph()

    tm.repo.connection.close()