# built-in/external modules/libs
import customtkinter as ctk
import os
import sys
# our modules/libs
from frontend.styles import BaseStyles, AppStyles # paddings, dimensions, colors, etc
from frontend.components import SidebarTabs # navigation page-tabs
from frontend.pages import LoginForm # login form
from frontend.pages import ProfilePage # profile page
from frontend.pages import HomePage # home page
from frontend.pages import EditPage # edit page
from frontend.pages import HistoryPage # history page
from frontend.pages import AddPage # edit page
from frontend.components import SubmitBTN # save btn
from frontend.components import PopUpWin # pop up win
from backend import UserRepository # db manager
from backend import TransactionManager # db manager


#--------------------------------------------------------------------------------------------------------


def prematureClose(tm):
    tm.repo.connection.close()
    os._exit(0)


#--------------------------------------------------------------------------------------------------------


# main app class
class App(ctk.CTk):
    def __init__(self, app_title, tm, userRepo):
        super().__init__()
        self.tm = tm
        self.userRepo = userRepo
        self.user_id = ctk.StringVar()
        self.username = ctk.StringVar()
        

        # initialize fonts
        self.font2 = ("Bodoni MT", BaseStyles.FONT_SIZE_2, "italic")
        self.font3 = ("Bodoni MT", BaseStyles.FONT_SIZE_3, "italic")
        
        # initialize app
        self.initializeApp(app_title=app_title)
        self.createPopUps()
        self.protocol("WM_DELETE_WINDOW", self.onPrematureAppClose)

        # start app
        self.createLoginForm()
        self.authenticateUser()
        self.startLoadingPopUp()
        self.createAppPages()
        self.createSidebar()
        self.createSubmitBTNs()
        self.loadPages()
        self.after_idle(self.endLoadingPopUp)

        # close app and db properly
        self.protocol("WM_DELETE_WINDOW", self.onClickAppClose)
        
        # for redirecting focus away from main entries
        self.createDummyEntry()
        # mouse left click 
        self.bind("<Button-1>", self.onClickNonEntry)


    def onPrematureAppClose(self):
        self.closing_popup.showWin()
        self.after(500, print, "\n[DB] Closing...")
        self.after(1000, self.tm.repo.connection.close)
        self.after(1500, print, "[DB] Closed successfully")
        self.after(2000, print, "\n[App] Premature close")
        self.after(2500, os._exit, 0)


    def _setupLogo(self):
        # icon path
        if hasattr(sys, "_MEIPASS"): # # for .exe: memory resources path
            LOGO_FOLDER = os.path.join(sys._MEIPASS, "assets/logo")
        else: # for .py: storage resources path
            LOGO_FOLDER = "assets/logo"
        logo_path = os.path.join(LOGO_FOLDER, "app.ico")
        self.iconbitmap(logo_path)

    
    def initializeApp(self, app_title):
        x_pos, y_pos = 0, 0
        self.after(100, self._setupLogo)
        self.title(app_title)
        self.geometry(f"{AppStyles.WIN_W}x{AppStyles.WIN_H}+{x_pos}+{y_pos}")
        self.maxsize(AppStyles.WIN_W, AppStyles.WIN_H)
        self.minsize(AppStyles.WIN_W, AppStyles.WIN_H)
        self.resizable(width=True, height=True)
        self.configure(fg_color=AppStyles.WIN_FG_COLOR)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


    def createPopUps(self):
        # loading
        self.loading_popup = PopUpWin(
            title="[App] Start",
            msg="Loading...",
            font=self.font2,
            enable_close=False,
            master=self,
            fg_color=AppStyles.LOAD_POP_UP_FG_COLOR,
            enable_frame_blocker=False
        )
        
        # closing popup
        self.closing_popup = PopUpWin(
            title="[App] Exit",
            msg="Exiting...",
            font=self.font2,
            enable_close=False,
            master=self,
            fg_color=AppStyles.CLOSE_APP_POP_UP_FG_COLOR,
            enable_frame_blocker=False
        )


    def createLoginForm(self):
        self.login = LoginForm(
            user_id=self.user_id,
            username=self.username,
            userRepo=self.userRepo,
            master=self,
            fg_color=AppStyles.LOGIN_FORM_FG_COLOR,
            corner_radius=BaseStyles.RAD_5
        )
        self.login.place(relx=0.5, rely=0.5, anchor="center")


    def authenticateUser(self):
        self.update()
        self.wait_variable(self.user_id) # w8 till user_id is modified
        
        # convert StringVar to normal str
        self.user_id = self.user_id.get()
        self.username = self.username.get()


    def startLoadingPopUp(self):
        self.loading_popup.showWin()
        self.update()
        self.after_idle(print, "[App] Started successfully")
        self.after_idle(print, "\n[Pages] Loading...")


    def createAppPages(self):
        self.page_frame = ctk.CTkFrame(
            master=self,
            corner_radius=0, 
            fg_color=AppStyles.WIN_FG_COLOR,
            width=1830,
            height=1080
        )
        self.profile_page = ProfilePage(
            app=self,
            tm=self.tm,
            master=self.page_frame,
            fg_color=AppStyles.WIN_FG_COLOR,
            corner_radius=0
        ) 
        self.home_page = HomePage(
            app=self,
            tm=self.tm,
            master=self.page_frame,
            fg_color=AppStyles.WIN_FG_COLOR,
            corner_radius=0
        ) 
        self.edit_page = EditPage(
            app=self,
            tm=self.tm,
            master=self.page_frame,
            fg_color=AppStyles.WIN_FG_COLOR,
            corner_radius=0
        ) 
        self.history_page = HistoryPage(
            app=self,
            tm=self.tm,
            master=self.page_frame,
            fg_color=AppStyles.WIN_FG_COLOR,
            corner_radius=0
        ) 
        self.add_page = AddPage(
            app=self,
            tm=self.tm,
            master=self.page_frame,
            fg_color=AppStyles.WIN_FG_COLOR,
            corner_radius=0
        ) 
        self.page_frame.grid(row=0, column=1, sticky="nesw")

    
    def createSidebar(self):
        self.pages = {
            "profile":self.profile_page, "home":self.home_page,
            "edit":self.edit_page, "history":self.history_page,
            "add":self.add_page
        }
        self.sidebar = SidebarTabs(
            pages=self.pages,
            master=self,
            fg_color=AppStyles.SIDEBAR_FG_COLOR,
            corner_radius=0,
            height=AppStyles.SIDEBAR_H
        )
        self.sidebar.grid(row=0, column=0, sticky="ns")


    def createSubmitBTNs(self):
        # edit button
        self.edit_submit_btn = SubmitBTN(
            user_id=self.user_id,
            tm=self.tm,
            pages=self.pages,
            master=self.edit_page,
            text="Submit",
            font=self.font3,
            text_color=BaseStyles.WHITE,
            corner_radius=BaseStyles.RAD_2,
            width=AppStyles.SAVE_BTN_W,
            height=AppStyles.SAVE_BTN_H, 
            fg_color=BaseStyles.BLUE,
            hover_color=BaseStyles.DARK_BLUE,
            app=self,
            popup_title="[DB] Update",
            popup_text="Updating...",
            popup_font=self.font2
        )
        self.edit_submit_btn.grid(row=3, column=0, pady=BaseStyles.PAD_4)
        
        # add button
        self.add_submit_btn = SubmitBTN(
            user_id=self.user_id,
            tm=self.tm,
            pages=self.pages,
            master=self.add_page,
            text="Submit",
            font=self.font3,
            text_color=BaseStyles.WHITE,
            corner_radius=BaseStyles.RAD_2,
            width=AppStyles.SAVE_BTN_W,
            height=AppStyles.SAVE_BTN_H, 
            fg_color=BaseStyles.BLUE,
            hover_color=BaseStyles.DARK_BLUE,
            app=self,
            popup_title="[DB] Update",
            popup_text="Updating...",
            popup_font=self.font2
        )
        self.add_submit_btn.grid(row=3, column=0, pady=BaseStyles.PAD_4)


    def loadPages(self):
        for page in reversed(self.pages.values()):
            self.after_idle(page.pack)
            self.after_idle(page.pack_forget)
        # display default page
        self.after_idle(self.sidebar.onClickProfilePage)


    def endLoadingPopUp(self):
        self.after_idle(self.loading_popup.hideWin)
        self.after_idle(print, "\n[Pages] Loaded successfully")


    def onClickAppClose(self):
        self.closing_popup.showWin()
        self.after(500, print, "\n[DB] Closing...")
        self.after(1000, self.tm.repo.connection.close)
        self.after(1500, print, "[DB] Closed successfully")
        self.after(2000, print, "\n[App] Closing...")
        self.after(2500, self.quit)
        self.after(3000, self.destroy)
        self.after(3500, print, "[App] Closed successfully.")


    def createDummyEntry(self):
        self.dummy_entry = ctk.CTkEntry(self)
        self.dummy_entry.place(x=-1*BaseStyles.SCREEN_W, y=-1*BaseStyles.SCREEN_W)


    def _unfocusEntries(self, event):
        print()
        print(event)
        print(f"{event.widget.winfo_class() == "Entry" = }")
        if not event.widget.winfo_class() == "Entry":
            self.dummy_entry.focus_set()


    def onClickNonEntry(self, event):
        self._unfocusEntries(event=event)


#--------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    print("\n[App] Starting...")
    app_title = "Personal Finance Tracker"

    try: # initialize db
        db_folder = os.path.abspath("db")
        db_name = "transactions.db"
        userRepo = UserRepository(db_folder, db_name)
        tm = TransactionManager(db_folder + "/" + "transactions.db")
    except Exception as e:
        print(f"{e = }")
        os._exit(0)

    try:
        app = App(app_title=app_title, tm=tm, userRepo=userRepo)
    except KeyboardInterrupt:
        print("\n[App] Closed successfully")
        os._exit(0)

    try:
        app.mainloop()
    # exit properly during keyboard interrupt
    except KeyboardInterrupt:
        print("\n[DB] Closing connection...")
        tm.repo.connection.close()
        print("[DB] Connection closed successfully")
        print("\n[App] Closing...")
        app.destroy()
        print("[App] Closed successfully")
        os._exit(0)
