# built-in/external modules/libs
import customtkinter as ctk
import os
# our modules/libs
from frontend.styles import Styles as s # paddings, dimensions, colors, etc
from frontend.components import Sidebar # navigation page-tabs
from frontend.pages import Profile # profile page
from frontend.pages import Home # home page
from frontend.pages import Edit # edit page
from frontend.pages import History # history page
from frontend.pages import Add # edit page
from frontend.components import Save # save btn
from backend import TransactionManager # db manager


# main app class
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        db_path = os.path.abspath("db/transactions.db")
        # user
        # create transaction manager
        self.user_id = 1
        self.tm = TransactionManager(db_path)
        # set app title
        self.title("Personal Finance Tracker")
        # initialize dimensions
        self.geometry(f"{s.SCREEN_W}x{s.SCREEN_H}")
        self.maxsize(s.SCREEN_W, s.SCREEN_H)
        self.minsize(s.SCREEN_W, s.SCREEN_H)
        self.resizable(width=True, height=True)
        # create scrollable screen (vertical)
        self.content = ctk.CTkScrollableFrame(self, orientation="vertical", corner_radius=0, fg_color=s.SKY_BLUE)
        # create app pages
        self.profilePage = Profile(user_id=self.user_id, tm=self.tm, master=self.content, fg_color=s.SKY_BLUE, corner_radius=0) 
        self.homePage = Home(user_id=self.user_id, tm=self.tm, master=self.content, fg_color=s.SKY_BLUE, corner_radius=0) 
        self.editPage = Edit(user_id=self.user_id, tm=self.tm, master=self.content, fg_color=s.SKY_BLUE, corner_radius=0) 
        self.historyPage = History(user_id=self.user_id, tm=self.tm, master=self.content, fg_color=s.SKY_BLUE, corner_radius=0) 
        self.addPage = Add(user_id=self.user_id, tm=self.tm, master=self.content, fg_color=s.SKY_BLUE, corner_radius=0) 
        self.pages = {
            "profile":self.profilePage, "home":self.homePage,
            "edit":self.editPage, "history":self.historyPage,
            "add":self.addPage
        }
        # create sidebar tabs
        self.sidebar = Sidebar(pages=self.pages, master=self, fg_color=s.WHITE, corner_radius=0)
        # create save btn
        self.editSaveBtn = Save(user_id=self.user_id, tm=self.tm, pages=self.pages, app=self,
                                master=self.editPage, fg_color=s.SKY_BLUE)
        self.addSaveBtn = Save(user_id=self.user_id, tm=self.tm, pages=self.pages, app=self,
                               master=self.addPage, fg_color=s.SKY_BLUE)
        # display sidebar/page-tabs and content[profile, home, edit, history, add]
        self.sidebar.pack(side="left", fill="y")
        self.content.pack(side="left", fill="both", expand=True)
        # display save buttons
        self.editSaveBtn.pack(pady=s.PAD_4)
        self.addSaveBtn.pack(pady=s.PAD_4)

        self.protocol("WM_DELETE_WINDOW", self.onCloseApp) # close the app and db properly

    def onCloseApp(self):
        self.tm.repo.connection.close()
        print("\nClosed DB connection.")
        print("Closing the app...")
        self.destroy()
        print("Closed app.")


if __name__ == "__main__":
    try:
        app = App()
    except KeyboardInterrupt:
        print("\nClosed app.")
        exit(0)

    try:
        app.mainloop()
    except KeyboardInterrupt:
        app.tm.repo.connection.close()
        print("\nClosed DB connection.")
        print("Closing the app...")
        app.destroy()
        print("Closed app.")
