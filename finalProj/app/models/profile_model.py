# external/built-in modules/libs
from customtkinter import StringVar, IntVar
# our modules/libs

from backend import TransactionManager, Finance # db manager

from models import Model


#--------------------------------------------------------------------------------------------------------


class ProfilePageModel(Model):
    def __init__(self, transaction_manager: TransactionManager, user_id_var: IntVar, username_var: StringVar):
        self.initialize_managers(transaction_manager)
        self.initialize_vars(user_id_var, username_var)        
        
        self.is_current_page = False
        self.finance = Finance(0, 0, 0, 0)
        self.balance = 0


    def initialize_managers(self, transaction_manager: TransactionManager):
        self.t_man = transaction_manager
    

    def initialize_vars(self, user_id_var: IntVar, username_var: StringVar):
        self.user_id_var = user_id_var
        self.username_var = username_var


    def load_amounts(self):
        self.finance = self.t_man.calculateOverallFinance(int(self.user_id_var.get()))
        self.balance = self.t_man.calculateOverallBalance(self.finance)


    def save_user_inputs_to_database(self):
        pass


    def load_transactions_per_filter(self):
        pass