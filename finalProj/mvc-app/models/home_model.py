# external/built-in modules/libs
from customtkinter import  IntVar
from typing import List, Dict, Tuple
# our modules/libs

from backend import Transaction, TransactionManager # db manager

from models import Model


#--------------------------------------------------------------------------------------------------------


class HomePageModel(Model):
    def __init__(self, transaction_manager: TransactionManager, user_id_var: IntVar):
        self.initialize_managers(transaction_manager)
        self.initialize_vars(user_id_var)

        self.is_current_page = False
        self.balance_amount = 0


    def initialize_managers(self, transaction_manager: TransactionManager):
        self.t_man = transaction_manager
    

    def initialize_vars(self, user_id_var: IntVar):
        self.user_id_var = user_id_var


    def load_amounts(self):
        self.finance = self.t_man.calculateOverallFinance(int(self.user_id_var.get()))
        self.balance = self.t_man.calculateOverallBalance(self.finance)
    
    
    def load_transactions_per_filter(self) -> Dict[str, List[Transaction]]:
        print("\n[DEBUG] loading transactions per filter...")
        transactions_per_filter = {
            "Recent": self.t_man.repo.getRecentTransactions(user_id=int(self.user_id_var.get()), t_count=10)
        }
        print("\n[DEBUG] transactions per filter loaded successfully...")
        return transactions_per_filter


    def save_user_inputs_to_database(self):
        pass
