# built-in/external modules/libs
import customtkinter as ctk
from pathlib import Path
# our modules/libs
from frontend.utilities.styles import *
from frontend.utilities.sidebar import Sidebar # navigation page-tabs
from frontend.pages.profile import Profile # profile page
from frontend.pages.edit import Edit # edit page
from frontend.pages.history import History # history page
from frontend.pages.add import Add # edit page
from frontend.utilities.save_section import Save # save btn
from backend.transaction_manager import TransactionManager


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

ENTRY_W1 = int(1.3241*SCREEN_H)#1430
ENTRY_W2 = int(0.5556*SCREEN_H) #600
ENTRY_H = int(0.0556*SCREEN_H) #60

MENU_W1 = int(0.7407*SCREEN_H) #800
MENU_W2 = int(1.2593*SCREEN_H) #1360 
MENU_H = int(0.0556*SCREEN_H) #60

YEAR_MENU_W = int(0.4167*SCREEN_H) #450
MONTH_MENU_W = int(0.4630*SCREEN_H) #500 
DAY_MENU_W = int(0.4167*SCREEN_H) #450

PAD_1 = int(0.0093*SCREEN_H) #10
PAD_2 = int(0.0185*SCREEN_H) #20
PAD_3 = int(0.0278*SCREEN_H) #30
PAD_4 = int(0.0370*SCREEN_H) #40
PAD_5 = int(0.0463*SCREEN_H) #50

BTN_W1 = int(0.0648*SCREEN_H) #70
BTN_W2 = int(0.3241*SCREEN_H) #350

BTN_H1 = int(0.0648*SCREEN_H) #70
BTN_H2 = int(0.0556*SCREEN_H) #60

RAD_2 = int(0.0185*SCREEN_H) #20


class Home(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # initialize state
        self.isCurrentPage = False
        # edit nyo nlng dito inyo
        # pag mahaba gawa nyo, pede nyo sya gawin sa 
        # separate file tas import nyo nlng dito,
        # lalo na kung kailangan nyo gumawa ng ibang classes
        # (gaya nung edit page & sidebar)
        label = ctk.CTkLabel(self, text="Home page", text_color=DARK_GREY, font=("Arial", 24))
        label.pack(pady=50)


# main app class
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        db_path = Path(__file__).resolve().parent / "db/transactions.db"
        # user
        # create transaction manager
        self.user_id = 1
        self.tm = TransactionManager(db_path)
        # set app title
        self.title("Personal Finance Tracker")
        # initialize dimensions
        self.geometry(f"{SCREEN_W}x{SCREEN_H}")
        self.maxsize(SCREEN_W, SCREEN_H)
        self.minsize(SCREEN_W, SCREEN_H)
        self.resizable(width=True, height=True)
        # create scrollable screen (vertical)
        self.content = ctk.CTkScrollableFrame(self, orientation="vertical", corner_radius=0, fg_color=SKY_BLUE)
        # create app pages
        self.profilePage = Profile(self.user_id, tm=self.tm, master=self.content, fg_color=SKY_BLUE, corner_radius=0) 
        self.homePage = Home(self.content, fg_color=SKY_BLUE, corner_radius=0) 
        self.editPage = Edit(self.user_id, tm=self.tm, master=self.content, fg_color=SKY_BLUE, corner_radius=0) 
        self.historyPage = History(self.content, fg_color=SKY_BLUE, corner_radius=0) 
        self.addPage = Add(self.user_id, tm=self.tm, master=self.content, fg_color=SKY_BLUE, corner_radius=0) 
        self.pages = {
            "profile":self.profilePage, "home":self.homePage,
            "edit":self.editPage, "history":self.historyPage,
            "add":self.addPage
        }
        # create sidebar tabs
        self.sidebar = Sidebar(pages=self.pages, master=self, fg_color=WHITE, corner_radius=0)
        # create save btn
        self.editSaveBtn = Save(tm=self.tm, user_id=self.user_id, pages=self.pages,
                                master=self.editPage, fg_color=SKY_BLUE)
        self.addSaveBtn = Save(tm=self.tm, user_id=self.user_id, pages=self.pages,
                               master=self.addPage, fg_color=SKY_BLUE)
        # display sidebar/page-tabs and content[profile, home, edit, history, add]
        self.sidebar.pack(side="left", fill="y")
        self.content.pack(side="left", fill="both", expand=True)
        # display save buttons
        self.editSaveBtn.pack(pady=PAD_4)
        self.addSaveBtn.pack(pady=PAD_4)


if __name__ == "__main__":
    app = App()
    app.mainloop()
