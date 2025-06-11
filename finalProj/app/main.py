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
        self.user_id = ctk.StringVar()
        self.username = ctk.StringVar()

        # initialize fonts
        self.font2 = ("Bodoni MT", BaseStyles.FONT_SIZE_2, "italic")
        self.font3 = ("Bodoni MT", BaseStyles.FONT_SIZE_3, "italic")
        
        # initialize app
        self.after(100, self.setupLogo)
        self.title(app_title)
        x_pos, y_pos = 0, 0
        self.geometry(f"{AppStyles.WIN_W}x{AppStyles.WIN_H}+{x_pos}+{y_pos}")
        self.maxsize(AppStyles.WIN_W, AppStyles.WIN_H)
        self.minsize(AppStyles.WIN_W, AppStyles.WIN_H)
        self.resizable(width=True, height=True)
        self.configure(fg_color=AppStyles.WIN_FG_COLOR)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # loading popup
        self.loading_popup = PopUpWin(
            title="[App] Start",
            msg="Loading...",
            font=self.font2,
            enable_close=False,
            master=self,
            fg_color=AppStyles.LOAD_POP_UP_FG_COLOR,
            enable_frame_blocker=False
        )
        
        # for closing db properly while app not ready
        self.protocol("WM_DELETE_WINDOW", lambda: prematureClose(tm=tm))

        # login page
        self.login = LoginForm(
            user_id=self.user_id,
            username=self.username,
            userRepo=userRepo,
            master=self,
            fg_color=AppStyles.LOGIN_FORM_FG_COLOR,
            corner_radius=BaseStyles.RAD_5
        )
        self.login.place(relx=0.5, rely=0.5, anchor="center")
        
        # block code bellow till user_id is not empty
        self.update()
        self.wait_variable(self.user_id)

        # load app
        print("[App] Started successfully")
        print("\n[Pages] Loading...")
        self.loading_popup.showWin()
        self.update()

        # convert StringVar to normal str
        self.user_id = self.user_id.get()
        self.username = self.username.get()

        # pages
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

        # sidebar tabs
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
        
        # edit save button
        self.edit_save_btn = self.createSubmitBTN(
            master=self.edit_page,
            text="Update Transaction",
            font=self.font3,
            popup_font=self.font2
        )
        self.edit_save_btn.grid(row=3, column=0, pady=BaseStyles.PAD_4)
        
        # add save button
        self.add_save_btn = self.createSubmitBTN(
            master=self.add_page,
            text="Add Transaction",
            font=self.font3,
            popup_font=self.font2
        )
        self.add_save_btn.grid(row=3, column=0, pady=BaseStyles.PAD_4)

        # load all pages
        self.loading_popup.after(100, self.loadPages)
        self.loading_popup.hideWin()
        print("\n[Pages] Loaded successfully")

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
        # for closing app and db properly
        self.protocol("WM_DELETE_WINDOW", self.onClickCloseApp)
        
        # dummy entry: for redirecting focus away from main entries
        self.outside_entry = ctk.CTkEntry(self)
        self.outside_entry.place(x=-1*BaseStyles.SCREEN_W, y=-1*BaseStyles.SCREEN_W)

        # mouse left click 
        self.bind("<Button-1>", self.onClickNonEntry)


    def setupLogo(self):
        # icon path
        if hasattr(sys, "_MEIPASS"): # # for .exe: memory resources path
            LOGO_FOLDER = os.path.join(sys._MEIPASS, "assets/logo")
        else: # for .py: storage resources path
            LOGO_FOLDER = "assets/logo"
        logo_path = os.path.join(LOGO_FOLDER, "app.ico")
        self.iconbitmap(logo_path)


    def createSubmitBTN(self, master, text, font, popup_font):
        submitBTN = SubmitBTN(
            user_id=self.user_id,
            tm=self.tm,
            pages=self.pages,
            master=master,
            text=text,
            font=font,
            text_color=BaseStyles.WHITE,
            corner_radius=BaseStyles.RAD_2,
            width=AppStyles.SAVE_BTN_W,
            height=AppStyles.SAVE_BTN_H, 
            fg_color=BaseStyles.BLUE,
            hover_color=BaseStyles.DARK_BLUE,
            app=self,
            popup_title="[DB] Update",
            popup_text="Updating...",
            popup_font=popup_font)
        return submitBTN


    def loadPages(self):
        for page in reversed(self.pages.values()):
            self.after_idle(page.pack)
            self.after_idle(page.pack_forget)
        # display default page
        self.after_idle(self.sidebar.onClickProfilePage)


    def onClickCloseApp(self):
        self.closing_popup.showWin()
        self.update()
        self.after_idle(print, "\n[DB] Closing...")
        self.after_idle(self.tm.repo.connection.close)
        self.after_idle(print, "[DB] Closed successfully")
        self.after_idle(print, "\n[App] Closing...")
        self.after_idle(self.quit)
        self.after_idle(self.destroy)
        self.after_idle(print, "[App] Closed successfully.")


    def _unfocusEntries(self, event):
        print()
        print(event)
        print(f"{event.widget.winfo_class() == "Entry" = }")
        if not event.widget.winfo_class() == "Entry":
            self.outside_entry.focus_set()


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
