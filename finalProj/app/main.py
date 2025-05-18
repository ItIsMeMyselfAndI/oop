# built-in/external modules/libs
import customtkinter as ctk
# our modules/libs
from frontend.utilities.sidebar import Sidebar # navigation page-tabs
from frontend.pages.profile import Profile # profile page
from frontend.pages.edit import Edit # edit page
from frontend.pages.history import History # history page
from frontend.pages.add import Add # edit page
from frontend.utilities.save_section import Save # save btn
from backend.transaction_manager import TransactionManager


FONT_SIZE_1 = 25
FONT_SIZE_2 = 30
FONT_SIZE_3 = 40
FONT_SIZE_4 = 50
FONT_SIZE_5 = 60

LIGHT_BLUE = "#cef2ff"
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

YEAR_MENU_W = 450
MONTH_MENU_W = 500 
DAY_MENU_W = 450

PAD_X1 = 10
PAD_X2 = 20
PAD_X3 = 20
PAD_X4 = 30
PAD_X5 = 40

PAD_Y5 = 40
PAD_Y4 = 30
PAD_Y3 = 20
PAD_Y2 = 20
PAD_Y1 = 10

BTN_W = 350
BTN_H = 60

RAD = 20


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
        # user
        self.user_id = 1
        # create transaction manager
        db_path = "db/transactions.db"
        self.tm = TransactionManager(db_path)
        # set app title
        self.title("Personal Finance Tracker")
        # initialize dimensions
        self.screen_w = self.winfo_screenwidth()
        self.screen_h = self.winfo_screenheight()
        print(self.screen_w, self.screen_h)
        self.geometry(f"{self.screen_w}x{self.screen_h}")
        # self.wm_maxsize(width, height) #max window size
        self.resizable(width=False, height=False) #disable resize window (temporary)
        # create scrollable screen (vertical)
        self.content = ctk.CTkScrollableFrame(self, orientation="vertical", corner_radius=0,fg_color=LIGHT_BLUE)
        # create app pages
        self.profilePage = Profile(self.content, fg_color=LIGHT_BLUE, corner_radius=0) 
        self.homePage = Home(self.content, fg_color=LIGHT_BLUE, corner_radius=0) 
        self.editPage = Edit(self.user_id, tm=self.tm, master=self.content, fg_color=LIGHT_BLUE, corner_radius=0) 
        self.historyPage = History(self.content, fg_color=LIGHT_BLUE, corner_radius=0) 
        self.addPage = Add(self.user_id, tm=self.tm, master=self.content, fg_color=LIGHT_BLUE, corner_radius=0) 
        self.pages = {
            "profile":self.profilePage, "home":self.homePage,
            "edit":self.editPage, "history":self.historyPage,
            "add":self.addPage
        }
        # create sidebar tabs
        self.sidebar = Sidebar(pages=self.pages, master=self, fg_color="#ffffff", corner_radius=0)
        # create save btn
        self.editSaveBtn = Save(tm=self.tm, user_id=self.user_id, pages=self.pages,
                                master=self.editPage, fg_color=LIGHT_BLUE)
        self.addSaveBtn = Save(tm=self.tm, user_id=self.user_id, pages=self.pages,
                               master=self.addPage, fg_color=LIGHT_BLUE)
        # display sidebar/page-tabs and content[profile, home, edit, history, add]
        self.sidebar.pack(side="left", fill="y")
        self.content.pack(side="left", fill="both", expand=True)
        # display save buttons
        self.editSaveBtn.pack(pady=PAD_Y5)
        self.addSaveBtn.pack(pady=PAD_Y5)



if __name__ == "__main__":
    app = App()
    app.mainloop()
