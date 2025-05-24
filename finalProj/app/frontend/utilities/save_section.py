import customtkinter as ctk
from backend.transaction_manager import Transaction


FONT_SIZE_1 = 25
FONT_SIZE_2 = 30
FONT_SIZE_3 = 40
FONT_SIZE_4 = 50
FONT_SIZE_5 = 60

SKY_BLUE = "#cef2ff"
BLUE = "#559eef"
DARK_BLUE = "#427cbd"
LIGHT_GREY = "#c4c4c4"
GREY = "grey"
DARK_GREY = "#545454"
WHITE= "white"

ENTRY_W1 = 1430
ENTRY_W2 = 600
ENTRY_H = 60

MENU_W1 = 800
MENU_W2 = 1360 
MENU_H = 60
YEAR_MENU_W = 180
MONTH_MENU_W = 220
DAY_MENU_W = 180

PAD_X1 = 10
PAD_X2 = 20
PAD_X3 = 30
PAD_X4 = 40
PAD_X5 = 50

PAD_Y1 = 10
PAD_Y2 = 20
PAD_Y3 = 30
PAD_Y4 = 40
PAD_Y5 = 50

BTN_W = 350
BTN_H = 60

RAD = 20


# save section
class Save(ctk.CTkFrame):
    def __init__(self, tm, user_id, pages, master, **kwargs):
        super().__init__(master, **kwargs)
        self.tm = tm
        self.user_id = user_id
        self.pages = pages
        self.font = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_2, slant="italic", weight="normal")
        self.btn = ctk.CTkButton(self, width=BTN_W, height=BTN_H, text="Save Changes",
                                 font=self.font, text_color=WHITE,
                                 fg_color=BLUE, hover_color=DARK_BLUE,
                                 corner_radius=RAD, command=self.onClickSave)
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

