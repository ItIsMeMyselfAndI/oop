# external/built-in modules/libs
import customtkinter as ctk
from customtkinter import StringVar, IntVar
# our modules/libs
from gui_styles import BaseStyles, EditStyles # paddings, dimensions, colors, etc
from gui_components import DatePicker
from backend import TransactionManager

from models import Model
from models import EditPageModel
from views import EditPageView
from controllers import Controller


#--------------------------------------------------------------------------------------------------------


class EditPageController(Controller):
    def __init__(self, transaction_manager: TransactionManager, user_id_var: IntVar, master):
        self.model = EditPageModel(transaction_manager=transaction_manager, user_id_var=user_id_var)
        self.view = EditPageView(model=self.model, master=master, fg_color=EditStyles.MAIN_FRAME_FG_COLOR)


    @property
    def model(self) -> Model:
        return self.__model
    
    
    @model.setter
    def model(self, value: Model):
        self.__model = value


    def run(self):
        pass


    def update_display(self):
        print("[DEBUG] updating edit page display...")
        for form in self.view.form_per_transaction_type.values():
            form.update_transaction_menu_options_per_type()
            form.transactionMenu.configure(values=form.transaction_options)
            form.transactionMenu.set(form.transaction_options[0])
        self.view.update_idletasks()
        print("[DEBUG] edit page display updated successfully")
