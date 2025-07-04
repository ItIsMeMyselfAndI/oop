# external/built-in modules/libs
from customtkinter import StringVar, IntVar
# our modules/libs
from views.styles import ProfileStyles # paddings, dimensions, colors, etc

from backend import TransactionManager # db manager

from models import Model, ProfilePageModel
from views.pages import ProfilePageView
from controllers import Controller


#--------------------------------------------------------------------------------------------------------


class ProfilePageController(Controller):
    def __init__(self, transaction_manager: TransactionManager, user_id_var: IntVar, username_var: StringVar, master):
        self.model = ProfilePageModel(transaction_manager=transaction_manager, user_id_var=user_id_var, username_var=username_var)
        self.view = ProfilePageView(model=self.model, master=master, fg_color=ProfileStyles.MAIN_FRAME_FG_COLOR)


    @property
    def model(self) -> Model:
        return self.__model
    
    
    @model.setter
    def model(self, value: Model):
        self.__model = value


    def run(self):
        pass


    def update_display(self):
        print("[DEBUG] updating profile page display...")
        self.model.load_amounts()
        self.view.header.balance_amount_label.configure(text=f"₱ {self.model.balance:,}")
        self.view.income_frame.summary_amount_label.configure(text=f"₱ {self.model.finance.total_income:,}")
        self.view.expense_frame.summary_amount_label.configure(text=f"₱ {self.model.finance.total_expenses:,}")
        self.view.savings_frame.summary_amount_label.configure(text=f"₱ {self.model.finance.total_savings:,}")
        self.view.investment_frame.summary_amount_label.configure(text=f"₱ {self.model.finance.total_investment:,}")
        self.view.update_idletasks()
        print("[DEBUG] profile page display updated successfully")
