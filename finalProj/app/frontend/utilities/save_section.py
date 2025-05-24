import customtkinter as ctk
from backend.transaction_manager import Transaction


# create global screen dimension
temp_root = ctk.CTk()
SCREEN_W = temp_root.winfo_screenwidth()
temp_root.destroy()
SCREEN_H = int(0.5625*SCREEN_W)
print(SCREEN_W, SCREEN_H)

FONT_SIZE_1 = int(0.0231*SCREEN_H) #25
FONT_SIZE_2 = int(0.0278*SCREEN_H) #30
FONT_SIZE_3 = int(0.0370*SCREEN_H) #40
FONT_SIZE_4 = int(0.0463*SCREEN_H) #50
FONT_SIZE_5 = int(0.0556*SCREEN_H) #60

WHITE= "white"

WHITE_RED = "#fdecec"
LIGHT_RED = "#ffc7c7"
RED = "#e14242"

WHITE_GREEN = "#dafbf0"
LIGHT_GREEN = "#b2fee3"
GREEN = "#28ab58"

WHITE_PURPLE = "#f3eefe"
LIGHT_PURPLE =  "#d6c5fb"
PURPLE = "#ceb9fe"

WHITE_BLUE = "#ebf2fe"
SKY_BLUE = "#cef2ff"
LIGHT_BLUE = "#bcd4fe"
BLUE = "#559eef"
DARK_BLUE = "#427cbd"

LIGHT_GREY = "#c4c4c4"
GREY = "grey"
DARK_GREY = "#545454"

ENTRY_W1 = int(1.3241*SCREEN_H) #1430
ENTRY_W2 = int(0.5556*SCREEN_H) #600
ENTRY_H = int(0.0556*SCREEN_H) #60

MENU_W1 = int(0.7407*SCREEN_H) #800
MENU_W2 = int(1.2593*SCREEN_H) #1360 
MENU_H = int(0.0556*SCREEN_H) #60

YEAR_MENU_W = int(0.4167*SCREEN_H) #450
MONTH_MENU_W = int(0.4630*SCREEN_H) #500 
DAY_MENU_W = int(0.4167*SCREEN_H) #450

PAD_X1 = int(0.0093*SCREEN_H) #10
PAD_X2 = int(0.0185*SCREEN_H) #20
PAD_X3 = int(0.0278*SCREEN_H) #30
PAD_X4 = int(0.0370*SCREEN_H) #40
PAD_X5 = int(0.0463*SCREEN_H) #50

PAD_Y1 = int(0.0093*SCREEN_H) #10
PAD_Y2 = int(0.0185*SCREEN_H) #20
PAD_Y3 = int(0.0278*SCREEN_H) #30
PAD_Y4 = int(0.0370*SCREEN_H) #40
PAD_Y5 = int(0.0463*SCREEN_H) #50

BTN_W1 = int(0.0648*SCREEN_H) #70
BTN_W2 = int(0.3241*SCREEN_H) #350

BTN_H1 = int(0.0648*SCREEN_H) #70
BTN_H2 = int(0.0556*SCREEN_H) #60

RAD = int(0.0185*SCREEN_H) #20


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

