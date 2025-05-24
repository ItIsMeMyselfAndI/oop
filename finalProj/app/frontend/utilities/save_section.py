# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from backend.transaction_manager import Transaction
from frontend.utilities.styles import *


# save section
class Save(ctk.CTkFrame):
    def __init__(self, tm, user_id, pages, master, **kwargs):
        super().__init__(master, **kwargs)
        self.tm = tm
        self.user_id = user_id
        self.pages = pages
        self.font = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_2, slant="italic", weight="normal")
        self.btn = ctk.CTkButton(self, width=BTN_W2, height=BTN_H2, text="Save Changes",
                                 font=self.font, text_color=WHITE,
                                 fg_color=BLUE, hover_color=DARK_BLUE,
                                 corner_radius=RAD_2, command=self.onClickSave)
        self.btn.pack()

    def onClickSave(self):
        # save to database
        for page_name, page in self.pages.items():
            if page_name == "edit" and page.isCurrentPage == True:
                self.pages["edit"].saveEditedTransactionToDatabase()
            elif page_name == "add" and page.isCurrentPage == True:
                self.pages["add"].saveNewTransactionToDatabase()
        # self.updateAppMemory()
        self.pages["edit"].updatePageDisplay()
        self.pages["profile"].updatePageDisplay()

