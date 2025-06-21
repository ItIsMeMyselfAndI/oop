# external/built-in modules/libs
from customtkinter import IntVar
# our modules/libs
from views.styles import AddStyles # paddings, dimensions, colors, etc
from backend import TransactionManager

from models import Model, AddPageModel
from views.pages import AddPageView
from controllers import Controller


#--------------------------------------------------------------------------------------------------------


class AddPageController(Controller):
    def __init__(self, transaction_manager: TransactionManager, user_id_var: IntVar, master):
        self.model = AddPageModel(transaction_manager=transaction_manager, user_id_var=user_id_var)
        self.view = AddPageView(model=self.model, master=master, fg_color=AddStyles.MAIN_FRAME_FG_COLOR)


    @property
    def model(self) -> Model:
        return self.__model
    
    
    @model.setter
    def model(self, value: Model):
        self.__model = value


    def run(self):
        pass


    def update_display(self):
        # print("[DEBUG] updating edit page display...")
        # print("[DEBUG] edit page display updated successfully")
        pass
