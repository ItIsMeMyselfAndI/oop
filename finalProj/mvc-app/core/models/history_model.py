# external/built-in modules/libs
import customtkinter as ctk
from customtkinter import StringVar, IntVar
from typing import Dict, List
# our modules/libs
from backend import Transaction

from backend import Transaction, TransactionManager, UserRepository # db manager

from core.models import Model


#--------------------------------------------------------------------------------------------------------


class HistoryPageModel(Model):
    def __init__(self, transaction_manager: TransactionManager, user_id_var: IntVar):
        self.initialize_managers(transaction_manager)
        self.initialize_vars(user_id_var)

        self.is_current_page = False


    def initialize_managers(self, transaction_manager: TransactionManager):
        self.t_man = transaction_manager
    

    def initialize_vars(self, user_id_var: IntVar):
        self.user_id_var = user_id_var
    
    
    def load_transactions_per_filter(self) -> Dict[str, List[Transaction]]:
        print("\n[DEBUG] loading transactions per filter...")
        transactions_per_filter = {
            "All Types": self.t_man.repo.getAllTransactions(int(self.user_id_var.get())),
            "Income": self.t_man.repo.getTransactionsByType(int(self.user_id_var.get()), "income"),
            "Savings": self.t_man.repo.getTransactionsByType(int(self.user_id_var.get()), "savings"),
            "Expenses": self.t_man.repo.getTransactionsByType(int(self.user_id_var.get()), "expense"),
            "Investment": self.t_man.repo.getTransactionsByType(int(self.user_id_var.get()), "investment"),
            # income
            "Salary":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Salary"),
            "Bonus":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Bonus"),
            "Side-hustles":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Side-hustles"),
            "Tips":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Tips"),
            # expenses
            "Bills":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Bills"),
            "Education":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Education"),
            "Entertainment":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Entertainment"),
            "Food & Drinks":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Food & Drinks"),
            "Grocery":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Grocery"),
            "Healthcare":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Healthcare"),
            "House":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "House"),
            "Shopping":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Shopping"),
            "Transportation":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Transportation"),
            "Wellness":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Wellness"),
            "Other":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Other"),
            # savings
            "Monthly Allowance":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Monthly Allowance"),
            "Change":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Change"),
            "Miscellaneous":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Miscellaneous"),
            # investment
            "Stocks":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Stocks"),
            "Crypto":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Crypto"),
            "Bonds":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Bonds"),
            "Real Estate":self.t_man.repo.getTransactionsByCategory(int(self.user_id_var.get()), "Real Estate")
        }
        print("\n[DEBUG] transactions per filter loaded successfully...")
        return transactions_per_filter
    
    
    def save_user_inputs_to_database(self):
        pass


    def load_amounts(self):
        pass
