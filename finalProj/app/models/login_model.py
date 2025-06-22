# external/built-in modules/libs
from customtkinter import StringVar, IntVar
# our modules/libs
from backend import UserRepository

from models import Model


#--------------------------------------------------------------------------------------------------------


class LoginPageModel(Model):
    def __init__(self, user_repository: UserRepository, user_id_var: IntVar, username_var: StringVar):
        self.initialize_managers(user_repository)
        self.initialize_vars(user_id_var, username_var)        
        
        self.is_current_page = False


    def initialize_managers(self, user_repository: UserRepository):
        self.u_repo = user_repository
    

    def initialize_vars(self, user_id_var: IntVar, username_var: StringVar):
        self.user_id_var = user_id_var
        self.username_var = username_var


    def load_amounts(self):
        pass


    def save_user_inputs_to_database(self):
        pass


    def load_transactions_per_filter(self):
        pass
