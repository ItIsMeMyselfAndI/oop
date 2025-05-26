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
        self.profilePage = Profile(user_id=self.user_id, tm=self.tm, master=self.content, fg_color=SKY_BLUE, corner_radius=0) 
        self.homePage = Home(master=self.content, fg_color=SKY_BLUE, corner_radius=0) 
        self.editPage = Edit(user_id=self.user_id, tm=self.tm, master=self.content, fg_color=SKY_BLUE, corner_radius=0) 
        self.historyPage = History(user_id=self.user_id, tm=self.tm, master=self.content, fg_color=SKY_BLUE, corner_radius=0) 
        self.addPage = Add(user_id=self.user_id, tm=self.tm, master=self.content, fg_color=SKY_BLUE, corner_radius=0) 
        self.pages = {
            "profile":self.profilePage, "home":self.homePage,
            "edit":self.editPage, "history":self.historyPage,
            "add":self.addPage
        }
        # create sidebar tabs
        self.sidebar = Sidebar(pages=self.pages, master=self, fg_color=WHITE, corner_radius=0)
        # create save btn
        self.editSaveBtn = Save(user_id=self.user_id, tm=self.tm, pages=self.pages,
                                master=self.editPage, fg_color=SKY_BLUE)
        self.addSaveBtn = Save(user_id=self.user_id, tm=self.tm, pages=self.pages,
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
