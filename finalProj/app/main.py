# built-in/external modules/libs
import customtkinter as ctk
# our modules/libs
from frontend.utilities.sidebar import Sidebar # navigation page-tabs
from frontend.pages.profile import Profile # profile page
from frontend.pages.edit import Edit # edit page
from frontend.pages.history import History # history page
from frontend.pages.add import Add # edit page
from backend.transaction_manager import TransactionManager

ctk.set_window_scaling(1.0)
ctk.set_widget_scaling(1.0)

LIGHT_BLUE = "#cef2ff"
BLUE = "#559eef"
DARK_BLUE = "#427cbd"
LIGHT_GREY = "#c4c4c4"
GREY = "grey"
DARK_GREY = "#545454"
WHITE= "white"


class Home(ctk.CTkFrame): #nicolas
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # edit nyo nlng dito inyo
        # pag mahaba gawa nyo, pede nyo sya gawin sa 
        # separate file tas import nyo nlng dito,
        # lalo na kung kailangan nyo gumawa ng ibang classes
        # (gaya nung edit page & sidebar)
        label = ctk.CTkLabel(self, text="Home page", text_color=DARK_GREY, font=("Arial", 24))
        label.pack(pady=50)


# main app class
class App(ctk.CTk): #mirasol
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
        self.content = ctk.CTkScrollableFrame(self, orientation="vertical",
                                              corner_radius=0,fg_color=LIGHT_BLUE)
        # create app pages
        self.profilePage = Profile(self.content, fg_color=LIGHT_BLUE, corner_radius=0) 
        self.homePage = Home(self.content, fg_color=LIGHT_BLUE, corner_radius=0) 
        self.editPage = Edit(self.user_id, tm=self.tm, master=self.content, fg_color=LIGHT_BLUE, corner_radius=0) 
        self.historyPage = History(self.content, fg_color=LIGHT_BLUE, corner_radius=0) 
        self.addPage = Add(self.content, fg_color=LIGHT_BLUE, corner_radius=0) 
        self.pages = {
            "profile":self.profilePage, "home":self.homePage,
            "edit":self.editPage, "history":self.historyPage,
            "add":self.addPage
        }
        # create sidebar tabs
        self.sidebar = Sidebar(pages=self.pages, master=self, fg_color="#ffffff", corner_radius=0)
        # display sidebar/page-tabs and content[profile, home, edit, history, add]
        self.sidebar.pack(side="left", fill="y")
        self.content.pack(side="left", fill="both", expand=True)



if __name__ == "__main__":
    app = App()
    app.mainloop()
