# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from backend.transaction_manager import Transaction
from frontend.styles import Styles as s # contains paddings, dimensions, colors, etc


# save section
class Save(ctk.CTkFrame):
    def __init__(self, user_id, tm, pages, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        self.pages = pages
        self.font = ctk.CTkFont(family="Bodoni MT", size=s.FONT_SIZE_3, slant="italic", weight="normal")
        self.btn = ctk.CTkButton(self, width=s.SAVE_BTN_W, height=s.SAVE_BTN_H, text="Save Changes",
                                 font=self.font, text_color=s.WHITE,
                                 fg_color=s.BLUE, hover_color=s.DARK_BLUE,
                                 corner_radius=s.RAD_2, command=self.onClickSave)
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
        self.pages["history"].updatePageDisplay()

