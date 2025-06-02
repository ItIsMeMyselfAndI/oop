# built-in/external modules/libs
import customtkinter as ctk
import os
# our modules/libs
from frontend.styles import BaseStyles, AppStyles # paddings, dimensions, colors, etc
from frontend.components import SidebarTabs # navigation page-tabs
from frontend.pages import LoginWin
from frontend.pages import ProfilePage # profile page
from frontend.pages import HomePage # home page
from frontend.pages import EditPage # edit page
from frontend.pages import HistoryPage # history page
from frontend.pages import AddPage # edit page
from frontend.components import SubmitBTN # save btn
from frontend.components import PopUpWin # pop up win
from backend import TransactionManager # db manager


# main app class
class App(ctk.CTk):
    def __init__(self, app_title, user_id, tm):
        super().__init__()
        self.user_id = user_id
        self.tm = tm
        # initialize app 
        x_pos, y_pos = 0, 0
        self.geometry(f"{AppStyles.WIN_W}x{AppStyles.WIN_H}+{x_pos}+{y_pos}")
        self.maxsize(AppStyles.WIN_W, AppStyles.WIN_H)
        self.minsize(AppStyles.WIN_W, AppStyles.WIN_H)
        self.resizable(width=True, height=True)
        self.configure(fg_color=AppStyles.WIN_FG_COLOR)
        # self.configure()
        # initialize fonts
        self.font2 = ("Bodoni MT", BaseStyles.FONT_SIZE_2, "italic")
        self.font3 = ("Bodoni MT", BaseStyles.FONT_SIZE_3, "italic")
        # set app title
        self.title(app_title)
        # create scrollable screen (vertical)
        self.content = ctk.CTkFrame(self, corner_radius=0, fg_color=AppStyles.WIN_FG_COLOR)
        # proceed once user_id is not empty
        # print(f"{self.user_id = }")
        # if self.user_id:
        # create app pages
        self.profilePage = ProfilePage(app=self, tm=self.tm, master=self.content, fg_color=AppStyles.WIN_FG_COLOR, corner_radius=0) 
        self.homePage = HomePage(app=self, tm=self.tm, master=self.content, fg_color=AppStyles.WIN_FG_COLOR, corner_radius=0) 
        self.editPage = EditPage(app=self, tm=self.tm, master=self.content, fg_color=AppStyles.WIN_FG_COLOR, corner_radius=0) 
        self.historyPage = HistoryPage(app=self, tm=self.tm, master=self.content, fg_color=AppStyles.WIN_FG_COLOR, corner_radius=0) 
        self.addPage = AddPage(app=self, tm=self.tm, master=self.content, fg_color=AppStyles.WIN_FG_COLOR, corner_radius=0) 
        self.pages = {
            "profile":self.profilePage, "home":self.homePage,
            "edit":self.editPage, "history":self.historyPage,
            "add":self.addPage
        }
        # create sidebar tabs
        self.sidebar = SidebarTabs(pages=self.pages, master=self, fg_color=AppStyles.SIDEBAR_FG_COLOR, corner_radius=0)
        # create save btn
        self.editSaveBtn = self.createSubmitBTN(master=self.editPage, text="Update Transaction", font=self.font3, popup_font=self.font2)
        self.addSaveBtn = self.createSubmitBTN(master=self.addPage, text="Add Transaction", font=self.font3, popup_font=self.font2)
        # display sidebar/page-tabs and content[profile, home, edit, history, add]
        self.sidebar.pack(side="left", fill="y")
        self.content.pack()
        # display save buttons
        self.editSaveBtn.pack(pady=BaseStyles.PAD_4)
        self.addSaveBtn.pack(pady=BaseStyles.PAD_4)
        # create pop ups
        self.loadPopUp = PopUpWin(title="[App] Load", msg="Loading...", font=self.font2, enable_close=False, master=self,
                                  fg_color=AppStyles.LOAD_POP_UP_FG_COLOR, enable_frame_blocker=False)
        self.closeAppPopUp = PopUpWin(title="[App] Exit", msg="Exiting...", font=self.font2, enable_close=False,master=self,
                                      fg_color=AppStyles.CLOSE_APP_POP_UP_FG_COLOR, enable_frame_blocker=False)
        # load all pages
        print("[App] Started successfully")
        print("\n[Pages] Loading...")
        self.loadPopUp.showWin()
        self.loadPopUp.after(100, self.loadPages) # load all pages
        self.loadPopUp.hideWin()
        print("\n[Pages] Loaded successfully")
        # close the app and db properly
        self.protocol("WM_DELETE_WINDOW", self.onCloseApp)

    def createSubmitBTN(self, master, text, font, popup_font):
        submitBTN = SubmitBTN(user_id=self.user_id, tm=self.tm, pages=self.pages, master=master,
                              text=text, font=font, text_color=BaseStyles.WHITE, corner_radius=BaseStyles.RAD_2,
                              width=AppStyles.SAVE_BTN_W, height=AppStyles.SAVE_BTN_H, 
                              fg_color=BaseStyles.BLUE, hover_color=BaseStyles.DARK_BLUE,
                              app=self, popup_title="[DB] Update", popup_text="Updating...", popup_font=popup_font)
        return submitBTN

    def loadPages(self):
        for page in reversed(self.pages.values()):
            self.after_idle(page.pack)
            self.after_idle(page.pack_forget)
        # display default page
        self.after_idle(self.sidebar.onClickProfilePage)

    def _closeAll(self):
        print("\n[DB] Closing...")
        self.tm.repo.connection.close()
        print("[DB] Closed successfully")
        print("\n[App] Closing...")
        self.destroy()
        print("[App] Closed successfully.")

    def onCloseApp(self):
        self.closeAppPopUp.showWin()
        self.closeAppPopUp.after(100, self._closeAll)
        self.closeAppPopUp.hideWin()


if __name__ == "__main__":
    print("\n[App] Starting...")
    app_title = "Personal Finance Tracker"
    user_id = None
    # user_id = 2
    try:
        # db
        db_path = os.path.abspath("db/transactions.db")
        tm = TransactionManager(db_path)
    except Exception as e:
        print(f"{e = }")

    try:
        # login win
        login = LoginWin(app_title=app_title, tm=tm, fg_color=AppStyles.WIN_FG_COLOR, width=AppStyles.WIN_W, height=AppStyles.WIN_H)
        login.mainloop()
        user_id = login.user_id
    except KeyboardInterrupt:
        print("\n[DB] Closing connection...")
        tm.repo.connection.close()
        print("[DB] Connection closed successfully")
        print("\n[Login] Closing...")
        login.destroy()
        print("[Login] Closed successfully")
        exit(0)

    print(f"{user_id = }")
    # app win
    try:
        app = App(app_title=app_title, user_id=user_id, tm=tm)
    except KeyboardInterrupt:
        print("\n[App] Closed successfully")
        exit(0)

    # exit properly during keyboard interrupt
    try:
        app.mainloop()
    except KeyboardInterrupt:
        print("\n[DB] Closing connection...")
        tm.repo.connection.close()
        print("[DB] Connection closed successfully")
        print("\n[App] Closing...")
        app.destroy()
        print("[App] Closed successfully")