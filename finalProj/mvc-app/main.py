# built-in/external modules/libs
import customtkinter as ctk
from customtkinter import StringVar
import os
import sys
from typing import List, Dict
# our modules/libs
from frontend.styles import BaseStyles, AppStyles # paddings, dimensions, colors, etc
from frontend.components import SidebarTabs # navigation page-tabs
from frontend.pages import LoginForm # login form
from frontend.components import SubmitBTN # save btn
from frontend.components import PopUpWin # pop up win
from backend import UserRepository, TransactionManager # db manager

from controllers.base_controller import Controller
from frontend.pages.profile import ProfilePageController
from frontend.pages.home import HomePageController
from frontend.pages.edit import EditPageController
from frontend.pages.history import HistoryPageController
from frontend.pages.add import AddPageController


class AppModel:
    def __init__(self, app_title: str, user_repository: UserRepository, transaction_manager: TransactionManager):
        self.app_title = app_title
        self.initialize_managers(user_repository, transaction_manager)


    def initialize_managers(self, user_repository: UserRepository, transaction_manager: TransactionManager):
        self.u_repo = user_repository
        self.t_man = transaction_manager


    def initialize_vars(self):
        print("\n[DEBUG] initializing strVars...")
        self.user_id_var = StringVar()
        self.username_var = StringVar()
        print("[DEBUG] strVars initialized successfully")


    def close_managers(self):
        print("[DEBUG] closing database managers...")
        self.t_man.repo.connection.close()
        self.u_repo.connection.close()
        print("[DEBUG] database managers closed successfully")


class AppView(ctk.CTk):
    def __init__(self, model: AppModel, fg_color=None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.model = model

        self.initialize_app_settings()


    def initialize_app_settings(self):
        print("\n[DEBUG] initializing app...")
        self.font2 = ("Arial", BaseStyles.FONT_SIZE_2, "normal")
        self.font3 = ("Arial", BaseStyles.FONT_SIZE_3, "normal")

        x_pos, y_pos = 0, 0
        self._setup_logo()
        self.title(self.model.app_title)
        self.geometry(f"{AppStyles.WIN_W}x{AppStyles.WIN_H}+{x_pos}+{y_pos}")
        self.maxsize(AppStyles.WIN_W, AppStyles.WIN_H)
        self.minsize(AppStyles.WIN_W, AppStyles.WIN_H)
        self.resizable(width=True, height=True)
        self.configure(fg_color=AppStyles.WIN_FG_COLOR)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.update_idletasks()
        print("[DEBUG] app initialized successfully")


    def _setup_logo(self):
        print("[DEBUG] setting up logo...")
        # icon path
        try:
            if hasattr(sys, "_MEIPASS"): # # for .exe: memory resources path
                LOGO_FOLDER = os.path.join(sys._MEIPASS, "assets/logo")
            else: # for .py: storage resources path
                LOGO_FOLDER = "assets/logo"
            logo_path = os.path.join(LOGO_FOLDER, "app.ico")
            self.iconbitmap(logo_path)
            self.update_idletasks()
            print("[DEBUG] logo setup completed successfully")

        except Exception as e:
            print(f"[DEBUG] logo setup failed: {e}")


    def create_popups(self):
        print("\n[DEBUG] creating popups...")
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
        
        # updating
        self.updating_popup = PopUpWin(
            title="[App] Update",
            msg="Updating...",
            font=self.font2,
            enable_close=False,
            master=self,
            fg_color=AppStyles.UPDATE_POP_UP_FG_COLOR,
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

        self.update_idletasks()
        print("[DEBUG] popups created successfully")


    def create_dummy_entry(self):
        print("\n[DEBUG] creating dummy entry...")
        self.dummy_entry = ctk.CTkEntry(self)
        self.dummy_entry.place(x=-1*BaseStyles.SCREEN_W, y=-1*BaseStyles.SCREEN_W)
        self.update_idletasks()
        print("[DEBUG] dummy entry created successfully")


    def create_login_form(self):
        print("\n[DEBUG] creating login form...")
        self.login = LoginForm(
            model=self.model,
            master=self,
            fg_color=AppStyles.LOGIN_FORM_FG_COLOR,
            corner_radius=BaseStyles.RAD_5
        )
        self.login.place(relx=0.5, rely=0.5, anchor="center")
        self.update_idletasks()
        print("[DEBUG] login form created successfully")


    def show_loading_popup(self):
        self.loading_popup.showWin()
        self.update()
        print("[DEBUG] show loading popup")


    def hide_loading_popup(self):
        self.loading_popup.hideWin()
        self.after_idle(lambda: print("[DEBUG] hide loading popup"))


    def show_closing_popup(self):
        self.closing_popup.showWin()
        self.update()
        print("\n[DEBUG] show closing popup")


    def create_main_page_frame(self):
        print("[DEBUG] creating main page frame...")
        self.page_frame = ctk.CTkFrame(
            master=self,
            corner_radius=0, 
            fg_color=AppStyles.WIN_FG_COLOR,
            width=AppStyles.MAIN_PAGE_FRAME_W,
            height=AppStyles.MAIN_PAGE_FRAME_H
        )
        self.page_frame.grid(row=0, column=1, sticky="nesw")
        self.update_idletasks()
        print("[DEBUG] main page frame created successfully")


    def create_main_pages(self, controller_per_page: Dict[str, Controller]):
        print("[DEBUG] creating main pages...")
        for controller in controller_per_page.values():
            controller.view.create()
        print("[DEBUG] main pages created successfully")
        

    def create_submit_btns(self, controller_per_page: Dict[str, Controller], updating_popup: ctk.CTkFrame):
        # edit button
        self.edit_submit_btn = SubmitBTN(
            controller_per_page=controller_per_page,
            updating_popup=updating_popup,
            master=controller_per_page["edit"].view,
            text="Submit",
            font=self.font3,
            text_color=BaseStyles.WHITE,
            corner_radius=BaseStyles.RAD_2,
            width=AppStyles.SAVE_BTN_W,
            height=AppStyles.SAVE_BTN_H, 
            fg_color=BaseStyles.BLUE,
            hover_color=BaseStyles.DARK_BLUE
        )
        self.edit_submit_btn.grid(row=3, column=0, pady=BaseStyles.PAD_4)
        
        # add button
        self.add_submit_btn = SubmitBTN(
            controller_per_page=controller_per_page,
            updating_popup=updating_popup,
            master=controller_per_page["add"].view,
            text="Submit",
            font=self.font3,
            text_color=BaseStyles.WHITE,
            corner_radius=BaseStyles.RAD_2,
            width=AppStyles.SAVE_BTN_W,
            height=AppStyles.SAVE_BTN_H, 
            fg_color=BaseStyles.BLUE,
            hover_color=BaseStyles.DARK_BLUE
        )
        self.add_submit_btn.grid(row=3, column=0, pady=BaseStyles.PAD_4)


    def load_pages_gui_to_memory(self, controller_per_page: Dict[str, Controller]):
        for controller in reversed(controller_per_page.values()):
            controller.view.pack()
            controller.view.pack_forget()
        self.update_idletasks()

    
    def create_sidebar(self, controller_per_page: Dict[str, Controller]):
        self.sidebar = SidebarTabs(
            controller_per_page=controller_per_page,
            master=self,
            fg_color=AppStyles.SIDEBAR_FG_COLOR,
            corner_radius=0,
            height=AppStyles.SIDEBAR_H
        )
        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.update_idletasks() 
        # display default page
        self.after_idle(self.sidebar.on_click_profile_page)
        self.update_idletasks() 


class AppController(Controller):
    def __init__(self, app_title: str, db_folder: str, db_name: str):
        self.initialize_db(db_folder=db_folder, db_name=db_name)
        self.model = AppModel(app_title=app_title, user_repository=self.u_repo, transaction_manager=self.t_man)
        self.view = AppView(model=self.model, fg_color="blue")


    def initialize_db(self, db_folder: str, db_name: str):
        print("\n[DEBUG] initializing database...")
        try:
            self.u_repo = UserRepository(db_folder, db_name)
            self.t_man = TransactionManager(f"{db_folder}/{db_name}")
            print("[DEBUG] database initialized successfully")

        except Exception as e:
            print(f"[DEBUG] database initialization failed: {e}")
            raise


    def run(self):
        print("\n[DEBUG] running app...")
        self.model.initialize_vars()
        self._initialize_gui()
        self.view.bind("<Button-1>", self.on_click_non_entry)
        self.view.protocol("WM_DELETE_WINDOW", self.on_premature_app_close)
        self._authenticate_user()
        self.view.create_main_page_frame()
        self._initialize_controller_per_page()
        self._setup_main_gui()
        self.view.protocol("WM_DELETE_WINDOW", self.on_click_app_close)
        self.view.mainloop()


    def _initialize_gui(self):
        print("[DEBUG] initializing gui...")
        self.view.create_popups()
        self.view.create_dummy_entry()
        # self.view.create_login_form()
        self.view.after(500, lambda: self.model.user_id_var.set(2))
        self.view.after(500, lambda: self.model.username_var.set("mirasol"))
        print("[DEBUG] gui initialized successfully")


    def _authenticate_user(self):
        print("[DEBUG] authenticating user...")
        self.view.update()
        self.view.wait_variable(self.model.user_id_var) # gets modified only when valid user
        print("[DEBUG] user authenticated successfully")


    def _initialize_controller_per_page(self):
        self.profile_controller = ProfilePageController(
            transaction_manager=self.t_man,
            user_id_var=self.model.user_id_var,
            username_var=self.model.username_var,
            master=self.view.page_frame
        )
        self.home_controller = HomePageController(
            transaction_manager=self.t_man,
            user_id_var=self.model.user_id_var,
            master=self.view.page_frame
        )
        self.edit_controller = EditPageController(
            transaction_manager=self.t_man,
            user_id_var=self.model.user_id_var,
            master=self.view.page_frame
        )
        self.history_controller = HistoryPageController(
            transaction_manager=self.t_man,
            user_id_var=self.model.user_id_var,
            master=self.view.page_frame
        )
        self.add_controller = AddPageController(
            transaction_manager=self.t_man,
            user_id_var=self.model.user_id_var,
            master=self.view.page_frame
        )

        self.controller_per_page = {
            "profile": self.profile_controller,
            "home": self.home_controller,
            "edit": self.edit_controller,
            "history": self.history_controller,
            "add": self.add_controller
        }


    def _setup_main_gui(self):
        print("[DEBUG] setting up main gui...")
        self.view.show_loading_popup()
        self.view.create_main_pages(self.controller_per_page)
        self.view.create_submit_btns(self.controller_per_page, self.view.updating_popup)
        self.view.load_pages_gui_to_memory(self.controller_per_page)
        self.view.create_sidebar(self.controller_per_page)
        self.view.after_idle(self.view.hide_loading_popup)
        self.view.update_idletasks()
        print("[DEBUG] main gui setup completed successfully")


    def on_click_non_entry(self, event: ctk.ctk_tk.tkinter.Event):
        # print(f"[DEBUG] {event.widget.winfo_class() = }")
        if not event.widget.winfo_class() == "Entry":
            self.view.dummy_entry.focus_set() # unfocus entries
            print("\n[DEBUG] unfocused entries")


    def on_premature_app_close(self):
        print("\n[DEBUG] closing app prematurely w/o user...")
        self.view.show_closing_popup()
        self.view.after_idle(self.model.close_managers)
        self.view.after_idle(lambda: print("[DEBUG] app closed successfully"))
        self.view.after_idle(lambda: os._exit(0))


    def on_click_app_close(self):
        print("\n[DEBUG] closing app...")
        self.view.show_closing_popup()
        self.view.after(300, self.model.close_managers)
        self.view.after(900, self.view.quit)
        self.view.after(1200, self.view.destroy)
        self.view.after(1500, print("[DEBUG] app closed successfully"))


    def update_display(self):
        pass
        
        
#--------------------------------------------------------------------------------------------------------


# # main app class
# class App(ctk.CTk):
#     def __init__(self, app_title, t_man, u_repo):
#         super().__init__()
#         self.t_man = t_man
#         self.u_repo = u_repo
#         self.user_id = ctk.StringVar()
#         self.username = ctk.StringVar()
        
#         # initialize fonts
#         self.font2 = ("Arial", BaseStyles.FONT_SIZE_2, "normal")
#         self.font3 = ("Arial", BaseStyles.FONT_SIZE_3, "normal")
        
#         # initialize app
#         self.initializeAppSettings(app_title=app_title)
#         self.createPopUps()
#         self.protocol("WM_DELETE_WINDOW", self.onPrematureAppClose)
#         self.createDummyEntry() # for redirecting focus away from main entries
#         self.bind("<Button-1>", self.onClickNonEntry) # mouse left click 

#         # get user
#         self.createLoginForm()
#         self.authenticateUser() # blocks code till login is complete
#         print(f"[DEBUG] {self.user_id = }")
#         print(f"[DEBUG] {self.username = }")


#         # start app
#         self.startLoadingPopUp()
#         self.createAppPages()
#         self.createSidebar()
#         self.createSubmitBTNs()
#         self.loadPagesToMemory()
#         self.endLoadingPopUp()

#         # close app and db properly
#         self.protocol("WM_DELETE_WINDOW", self.onClickAppClose)


#     def onPrematureAppClose(self):
#         self.closing_popup.showWin()
#         self.after_idle(print, "\n[DB] Closing...")
#         self.after_idle(self.t_man.repo.connection.close)
#         self.after_idle(print, "[DB] Closed successfully")
#         self.after_idle(print, "\n[App] Premature close")
#         self.after_idle(os._exit, 0)


#     def _setupLogo(self):
#         # icon path
#         if hasattr(sys, "_MEIPASS"): # # for .exe: memory resources path
#             LOGO_FOLDER = os.path.join(sys._MEIPASS, "assets/logo")
#         else: # for .py: storage resources path
#             LOGO_FOLDER = "assets/logo"
#         logo_path = os.path.join(LOGO_FOLDER, "app.ico")
#         self.iconbitmap(logo_path)


#     def initializeAppSettings(self, app_title):
#         x_pos, y_pos = 0, 0
#         self._setupLogo()
#         self.title(app_title)
#         self.geometry(f"{AppStyles.WIN_W}x{AppStyles.WIN_H}+{x_pos}+{y_pos}")
#         self.maxsize(AppStyles.WIN_W, AppStyles.WIN_H)
#         self.minsize(AppStyles.WIN_W, AppStyles.WIN_H)
#         self.resizable(width=True, height=True)
#         self.configure(fg_color=AppStyles.WIN_FG_COLOR)
#         self.grid_rowconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)


#     def createPopUps(self):
#         # loading
#         self.loading_popup = PopUpWin(
#             title="[App] Start",
#             msg="Loading...",
#             font=self.font2,
#             enable_close=False,
#             master=self,
#             fg_color=AppStyles.LOAD_POP_UP_FG_COLOR,
#             enable_frame_blocker=False
#         )
        
#         # closing popup
#         self.closing_popup = PopUpWin(
#             title="[App] Exit",
#             msg="Exiting...",
#             font=self.font2,
#             enable_close=False,
#             master=self,
#             fg_color=AppStyles.CLOSE_APP_POP_UP_FG_COLOR,
#             enable_frame_blocker=False
#         )


#     def createDummyEntry(self):
#         self.dummy_entry = ctk.CTkEntry(self)
#         self.after_idle(lambda: self.dummy_entry.place(x=-1*BaseStyles.SCREEN_W, y=-1*BaseStyles.SCREEN_W))


#     def _unfocusEntries(self, event):
#         print()
#         print(event)
#         print(f"{event.widget.winfo_class() = }")
#         if not event.widget.winfo_class() == "Entry":
#             self.dummy_entry.focus_set()


#     def onClickNonEntry(self, event):
#         self._unfocusEntries(event=event)


#     def createLoginForm(self):
#         self.login = LoginForm(
#             user_id=self.user_id,
#             username=self.username,
#             u_repo=self.u_repo,
#             master=self,
#             fg_color=AppStyles.LOGIN_FORM_FG_COLOR,
#             corner_radius=BaseStyles.RAD_5
#         )
#         self.after_idle(lambda: self.login.place(relx=0.5, rely=0.5, anchor="center"))


#     def authenticateUser(self):
#         self.update()
#         self.wait_variable(self.user_id) # w8 till user_id is modified
        
#         # convert StringVar to normal str
#         self.user_id = self.user_id.get()
#         self.username = self.username.get()


#     def startLoadingPopUp(self):
#         self.after_idle(self.loading_popup.showWin)
#         self.after_idle(self.update)
#         self.after_idle(print, "[App] Started successfully")
#         self.after_idle(print, "\n[Pages] Loading...")


#     def createAppPages(self):
#         self.page_frame = ctk.CTkFrame(
#             master=self,
#             corner_radius=0, 
#             fg_color=AppStyles.WIN_FG_COLOR,
#             width=1830,
#             height=1080
#         )
#         self.profile_page = ProfilePage(
#             app=self,
#             t_man=self.t_man,
#             master=self.page_frame,
#             fg_color=AppStyles.WIN_FG_COLOR,
#             corner_radius=0
#         ) 
#         self.home_page = HomePage(
#             app=self,
#             t_man=self.t_man,
#             master=self.page_frame,
#             fg_color=AppStyles.WIN_FG_COLOR,
#             corner_radius=0
#         ) 
#         self.edit_page = EditPage(
#             app=self,
#             t_man=self.t_man,
#             master=self.page_frame,
#             fg_color=AppStyles.WIN_FG_COLOR,
#             corner_radius=0
#         ) 
#         self.history_page = HistoryPage(
#             app=self,
#             t_man=self.t_man,
#             master=self.page_frame,
#             fg_color=AppStyles.WIN_FG_COLOR,
#             corner_radius=0
#         ) 
#         self.add_page = AddPage(
#             app=self,
#             t_man=self.t_man,
#             master=self.page_frame,
#             fg_color=AppStyles.WIN_FG_COLOR,
#             corner_radius=0
#         ) 
#         self.after_idle(lambda: self.page_frame.grid(row=0, column=1, sticky="nesw"))

    
#     def createSidebar(self):
#         self.pages = {
#             "profile":self.profile_page, "home":self.home_page,
#             "edit":self.edit_page, "history":self.history_page,
#             "add":self.add_page
#         }
#         self.sidebar = SidebarTabs(
#             pages=self.pages,
#             master=self,
#             fg_color=AppStyles.SIDEBAR_FG_COLOR,
#             corner_radius=0,
#             height=AppStyles.SIDEBAR_H
#         )
#         self.after_idle(lambda: self.sidebar.grid(row=0, column=0, sticky="ns"))
        
#         # display default page
#         self.after_idle(self.sidebar.onClickProfilePage)


#     def createSubmitBTNs(self):
#         # edit button
#         self.edit_submit_btn = SubmitBTN(
#             user_id=self.user_id,
#             t_man=self.t_man,
#             pages=self.pages,
#             master=self.edit_page,
#             text="Submit",
#             font=self.font3,
#             text_color=BaseStyles.WHITE,
#             corner_radius=BaseStyles.RAD_2,
#             width=AppStyles.SAVE_BTN_W,
#             height=AppStyles.SAVE_BTN_H, 
#             fg_color=BaseStyles.BLUE,
#             hover_color=BaseStyles.DARK_BLUE,
#             app=self,
#             popup_title="[DB] Update",
#             popup_text="Updating...",
#             popup_font=self.font2
#         )
#         self.after_idle(lambda: self.edit_submit_btn.grid(row=3, column=0, pady=BaseStyles.PAD_4))
        
#         # add button
#         self.add_submit_btn = SubmitBTN(
#             user_id=self.user_id,
#             t_man=self.t_man,
#             pages=self.pages,
#             master=self.add_page,
#             text="Submit",
#             font=self.font3,
#             text_color=BaseStyles.WHITE,
#             corner_radius=BaseStyles.RAD_2,
#             width=AppStyles.SAVE_BTN_W,
#             height=AppStyles.SAVE_BTN_H, 
#             fg_color=BaseStyles.BLUE,
#             hover_color=BaseStyles.DARK_BLUE,
#             app=self,
#             popup_title="[DB] Update",
#             popup_text="Updating...",
#             popup_font=self.font2
#         )
#         self.after_idle(lambda: self.add_submit_btn.grid(row=3, column=0, pady=BaseStyles.PAD_4))


#     def loadPagesToMemory(self):
#         for name in reversed(self.pages.keys()):
#             self.after_idle(lambda: self.sidebar._hideOtherPages(name))
#             self.after_idle(lambda: self.sidebar._showPage(name))


#     def endLoadingPopUp(self):
#         self.after_idle(self.loading_popup.hideWin)
#         self.after_idle(print, "\n[Pages] Loaded successfully")


#     def onClickAppClose(self):
#         self.closing_popup.showWin()
#         self.after(300, print, "\n[DB] Closing...")
#         self.after(600, self.t_man.repo.connection.close)
#         self.after(900, print, "[DB] Closed successfully")
#         self.after(1200, print, "\n[App] Closing...")
#         self.after(1500, self.quit)
#         self.after(1800, self.destroy)
#         self.after(2100, print, "[App] Closed successfully.")


# #--------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    # print("\n[App] Starting...")
    # app_title = "Finance Tracker"

    # try: # initialize db
    #     db_folder = os.path.abspath("db")
    #     db_name = "transactions.db"
    #     u_repo = UserRepository(db_folder, db_name)
    #     t_man = TransactionManager(db_folder + "/" + "transactions.db")
    # except Exception as e:
    #     print(f"{e = }")
    #     os._exit(0)

    # try:
    #     app = App(app_title=app_title, t_man=t_man, u_repo=u_repo)
    # except KeyboardInterrupt:
    #     print("\n[App] Closed successfully")
    #     os._exit(0)

    # try:
    #     app.mainloop()
    # # exit properly during keyboard interrupt
    # except KeyboardInterrupt:
    #     print("\n[DB] Closing connection...")
    #     t_man.repo.connection.close()
    #     print("[DB] Connection closed successfully")
    #     print("\n[App] Closing...")
    #     app.destroy()
    #     print("[App] Closed successfully")
    #     os._exit(0)
    print("\n[App] Starting...")
    app_title = "Finance Tracker"
    try:
        db_folder = os.path.abspath("db")
        db_name = "transactions.db"
        app_controller = AppController(app_title=app_title, db_folder=db_folder, db_name=db_name)
        app_controller.run()

    except KeyboardInterrupt:
        app_controller.on_click_app_close()
    
    # except Exception as e:
    #     print(f"[ERROR] app: {e}")

