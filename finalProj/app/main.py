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
from backend import UserRepository # db manager
from backend import TransactionManager # db manager


#--------------------------------------------------------------------------------------------------------


# main app class
class App(ctk.CTk):
    def __init__(self, app_title, user_id, username, tm):
        super().__init__()
        self.user_id = user_id
        self.username = username
        self.tm = tm

        # initialize app 
        self.title(app_title)
        x_pos, y_pos = 0, 0
        self.geometry(f"{AppStyles.WIN_W}x{AppStyles.WIN_H}+{x_pos}+{y_pos}")
        self.maxsize(AppStyles.WIN_W, AppStyles.WIN_H)
        self.minsize(AppStyles.WIN_W, AppStyles.WIN_H)
        self.resizable(width=True, height=True)
        self.configure(fg_color=AppStyles.WIN_FG_COLOR)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # initialize fonts
        self.font2 = ("Bodoni MT", BaseStyles.FONT_SIZE_2, "italic")
        self.font3 = ("Bodoni MT", BaseStyles.FONT_SIZE_3, "italic")

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
        
        # loading
        self.loading_popup = PopUpWin(
            title="[App] Load",
            msg="Loading...",
            font=self.font2,
            enable_close=False,
            master=self,
            fg_color=AppStyles.LOAD_POP_UP_FG_COLOR,
            enable_frame_blocker=False
        )
        
        # closing
        self.closing_popup = PopUpWin(
            title="[App] Exit",
            msg="Exiting...",
            font=self.font2,
            enable_close=False,
            master=self,
            fg_color=AppStyles.CLOSE_APP_POP_UP_FG_COLOR,
            enable_frame_blocker=False
        )

        # load all pages
        print("[App] Started successfully")
        print("\n[Pages] Loading...")
        self.loading_popup.showWin()
        self.loading_popup.after(100, self.loadPages) # load all pages
        self.loading_popup.hideWin()
        print("\n[Pages] Loaded successfully")

        # for closing app and db properly
        self.protocol("WM_DELETE_WINDOW", self.onClickCloseApp)
        
        # dummy entry: for redirecting focus away from main entries
        self.outside_entry = ctk.CTkEntry(self)
        self.outside_entry.place(x=-1*BaseStyles.SCREEN_W, y=-1*BaseStyles.SCREEN_W)

        # mouse left click 
        self.bind("<Button-1>", self.onClickNonEntry)


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


    def _closeAll(self):
        print("\n[DB] Closing...")
        self.tm.repo.connection.close()
        print("[DB] Closed successfully")
        print("\n[App] Closing...")
        self.destroy()
        print("[App] Closed successfully.")


    def onClickCloseApp(self):
        self.closing_popup.showWin()
        self.closing_popup.after(100, self._closeAll)
        self.closing_popup.hideWin()


    def _unfocusEntries(self, event):
        print()
        print(event)
        print(f"{event.widget.winfo_class() == "Entry" = }")
        if not event.widget.winfo_class() == "Entry":
            self.outside_entry.focus_set()


    def onClickNonEntry(self, event):
        self._unfocusEntries(event=event)


if __name__ == "__main__":
    print("\n[App] Starting...")
    app_title = "Personal Finance Tracker"
    user_id = None
    username = None
    # user_id = 2

    try:
    # initialize db
        db_folder = os.path.abspath("db")
        db_name = "transactions.db"
        userRepo = UserRepository(db_folder, db_name)
        tm = TransactionManager(db_folder + "/" + "transactions.db")
    except Exception as e:
        print(f"{e = }")

    try:
        # login win
        login = LoginWin(app_title=app_title, userRepo=userRepo, fg_color=AppStyles.WIN_FG_COLOR, width=AppStyles.WIN_W, height=AppStyles.WIN_H)
        login.mainloop()
        user_id = login.user_id
        username = login.username
    except KeyboardInterrupt:
        print("\n[DB] Closing connection...")
        tm.repo.connection.close()
        print("[DB] Connection closed successfully")
        print("\n[LoginStyles] Closing...")
        login.destroy()
        print("[LoginStyles] Closed successfully")
        exit(0)


    # app win
    if user_id and username:
        try:
            app = App(app_title=app_title, user_id=user_id, username=username, tm=tm)
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

    else:
        print("[App] Closed successfully")
