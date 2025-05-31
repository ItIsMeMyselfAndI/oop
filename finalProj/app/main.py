# built-in/external modules/libs
import customtkinter as ctk
import os
# our modules/libs
from frontend.styles import BaseStyles # paddings, dimensions, colors, etc
from frontend.components import SidebarTabs # navigation page-tabs
from frontend.pages import ProfilePage # profile page
from frontend.pages import HomePage # home page
from frontend.pages import EditPage # edit page
from frontend.pages import HistoryPage # history page
from frontend.pages import AddPage # edit page
from frontend.components import SaveBTN # save btn
from frontend.components import PopUpWin # pop up win
from backend import TransactionManager # db manager


# main app class
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        db_path = os.path.abspath("db/transactions.db")
        # user
        self.user_id = 1
        # create transaction manager
        self.tm = TransactionManager(db_path)
        # set app title
        self.title("Personal Finance Tracker")
        # initialize dimensions
        x_pos, y_pos = 0, 0
        self.geometry(f"{BaseStyles.SCREEN_W}x{BaseStyles.SCREEN_H}+{x_pos}+{y_pos}")
        self.maxsize(BaseStyles.SCREEN_W, BaseStyles.SCREEN_H)
        self.minsize(BaseStyles.SCREEN_W, BaseStyles.SCREEN_H)
        self.resizable(width=True, height=True)
        # create scrollable screen (vertical)
        self.content = ctk.CTkScrollableFrame(self, orientation="vertical", corner_radius=0, fg_color=BaseStyles.SKY_BLUE)
        # create app pages
        self.profilePage = ProfilePage(user_id=self.user_id, tm=self.tm, master=self.content, fg_color=BaseStyles.SKY_BLUE, corner_radius=0) 
        self.homePage = HomePage(user_id=self.user_id, tm=self.tm, master=self.content, fg_color=BaseStyles.SKY_BLUE, corner_radius=0) 
        self.editPage = EditPage(user_id=self.user_id, tm=self.tm, master=self.content, fg_color=BaseStyles.SKY_BLUE, corner_radius=0) 
        self.historyPage = HistoryPage(user_id=self.user_id, tm=self.tm, master=self.content, fg_color=BaseStyles.SKY_BLUE, corner_radius=0) 
        self.addPage = AddPage(user_id=self.user_id, tm=self.tm, master=self.content, fg_color=BaseStyles.SKY_BLUE, corner_radius=0) 
        self.pages = {
            "profile":self.profilePage, "home":self.homePage,
            "edit":self.editPage, "history":self.historyPage,
            "add":self.addPage
        }
        # create sidebar tabs
        self.sidebar = SidebarTabs(pages=self.pages, master=self, fg_color=BaseStyles.WHITE, corner_radius=0)
        # create save btn
        self.editSaveBtn = SaveBTN(user_id=self.user_id, tm=self.tm, pages=self.pages, app=self,
                                master=self.editPage, fg_color=BaseStyles.SKY_BLUE)
        self.addSaveBtn = SaveBTN(user_id=self.user_id, tm=self.tm, pages=self.pages, app=self,
                               master=self.addPage, fg_color=BaseStyles.SKY_BLUE)
        # display sidebar/page-tabs and content[profile, home, edit, history, add]
        self.sidebar.pack(side="left", fill="y")
        self.content.pack(side="left", fill="both", expand=True)
        # display save buttons
        self.editSaveBtn.pack(pady=BaseStyles.PAD_4)
        self.addSaveBtn.pack(pady=BaseStyles.PAD_4)

        # create pop ups
        self.loadPopUp = PopUpWin(title="[Start] Loading App", msg="App pages are loading...\nPlease wait...",
                                  enable_close=False, master=self, fg_color=BaseStyles.WHITE)
        self.closePopUp = PopUpWin(title="[Exit] Closing App", msg="App pages is closing...\nPlease wait...",
                                  enable_close=False, master=self, fg_color=BaseStyles.WHITE)
        # load all pages
        print("App started...")
        print("\nLoading pages...")
        self.loadPopUp.showWin()
        self.loadPopUp.after(100, self.loadPages) # load all pages
        self.loadPopUp.hideWin()
        print("Pages loaded.")
        # close the app and db properly
        self.protocol("WM_DELETE_WINDOW", self.onCloseApp)

    def loadPages(self):
        for page in reversed(self.pages.values()):
            page.pack()
            page.pack_forget()
        # display default page
        self.sidebar.onClickProfilePage()

    def _closeAll(self):
        print("\nClosing DB connection...")
        self.tm.repo.connection.close()
        print("DB connection closed.")
        print("\nClosing app...")
        self.destroy()
        print("Closed app.")

    def onCloseApp(self):
        self.closePopUp.showWin()
        self.closePopUp.after(100, self._closeAll)
        self.closePopUp.hideWin()


if __name__ == "__main__":
    print("\nStarting app...")
    try:
        app = App()
    except KeyboardInterrupt:
        print("\nApp closed.")
        exit(0)
    # exit properly during keyboard interrupt
    try:
        app.mainloop()
    except KeyboardInterrupt:
        print("\nClosing DB connection...")
        app.tm.repo.connection.close()
        print("DB connection closed.")
        print("\nClosing app...")
        app.destroy()
        print("App closed.")
