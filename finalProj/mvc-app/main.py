# built-in/external modules/libs
import customtkinter as ctk
from customtkinter import StringVar, IntVar
import os
import sys
from typing import List, Dict

# our modules/libs
from frontend.styles import BaseStyles, AppStyles # paddings, dimensions, colors, etc
from frontend.gui_components import PopUpWin ,SubmitBTN, SidebarTabs

from backend import UserRepository, TransactionManager # db manager
from models import Model
from controllers import Controller, ProfilePageController, EditPageController, AddPageController, HomePageController, HistoryPageController, LoginPageController


#--------------------------------------------------------------------------------------------------------


class AppModel:
    def __init__(self, app_title: str, user_repository: UserRepository, transaction_manager: TransactionManager):
        self.app_title = app_title
        self.initialize_managers(user_repository, transaction_manager)

    
    def initialize_managers(self, user_repository: UserRepository, transaction_manager: TransactionManager):
        self.u_repo = user_repository
        self.t_man = transaction_manager


    def initialize_vars(self):
        print("\n[DEBUG] initializing strVars...")
        self.user_id_var = IntVar()
        self.username_var = StringVar()
        print("[DEBUG] strVars initialized successfully")


    def close_managers(self):
        print("[DEBUG] closing database managers...")
        self.t_man.repo.connection.close()
        self.u_repo.connection.close()
        print("[DEBUG] database managers closed successfully")


#--------------------------------------------------------------------------------------------------------


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
                _MEIPASS: str = getattr(sys, "_MEIPASS")
                LOGO_FOLDER = os.path.join(_MEIPASS, "assets/logo")
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
            text_color=AppStyles.POPUP_TEXT_COLOR,
            width=AppStyles.POPUP_WIN_W,
            height=AppStyles.POPUP_WIN_H,
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
            text_color=AppStyles.POPUP_TEXT_COLOR,
            width=AppStyles.POPUP_WIN_W,
            height=AppStyles.POPUP_WIN_H,
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
            text_color=AppStyles.POPUP_TEXT_COLOR,
            width=AppStyles.POPUP_WIN_W,
            height=AppStyles.POPUP_WIN_H,
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
        self.login_controller = LoginPageController(
            user_repository=self.model.u_repo,
            user_id_var=self.model.user_id_var,
            username_var=self.model.username_var,
            page_fg_color=AppStyles.LOGIN_PAGE_FG_COLOR,
            form_fg_color=AppStyles.LOGIN_FORM_FG_COLOR,
            corner_radius=0,
            master=self
        )
        # self.login = LoginPage(
        #     model=self.model,
        #     master=self,
        #     page_fg_color=AppStyles.LOGIN_PAGE_FG_COLOR,
        #     form_fg_color=AppStyles.LOGIN_FORM_FG_COLOR,
        #     corner_radius=0
        # )
        self.login_controller.view.pack(fill="both", expand=True)
        # self.login.place(relx=0.5, rely=0.5, anchor="center")
        self.login_controller.view.update_idletasks()
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
        

    def create_submit_btns(self, controller_per_page: Dict[str, Controller], updating_popup: PopUpWin):
        # edit button
        self.edit_submit_btn = SubmitBTN(
            controller_per_page=controller_per_page,
            updating_popup=updating_popup,
            master=controller_per_page["edit"].view,
            text="Submit",
            font=self.font3,
            corner_radius=BaseStyles.RAD_2,
            width=AppStyles.SAVE_BTN_W,
            height=AppStyles.SAVE_BTN_H, 
            text_color=AppStyles.SAVE_BTN_TEXT_COLOR,
            fg_color=AppStyles.SAVE_BTN_FG_COLOR,
            hover_color=AppStyles.SAVE_BTN_HOVER_COLOR
        )
        self.edit_submit_btn.grid(row=3, column=0, pady=BaseStyles.PAD_4)
        
        # add button
        self.add_submit_btn = SubmitBTN(
            controller_per_page=controller_per_page,
            updating_popup=updating_popup,
            master=controller_per_page["add"].view,
            text="Submit",
            font=self.font3,
            corner_radius=BaseStyles.RAD_2,
            width=AppStyles.SAVE_BTN_W,
            height=AppStyles.SAVE_BTN_H, 
            text_color=AppStyles.SAVE_BTN_TEXT_COLOR,
            fg_color=AppStyles.SAVE_BTN_FG_COLOR,
            hover_color=AppStyles.SAVE_BTN_HOVER_COLOR
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


#--------------------------------------------------------------------------------------------------------


class AppController(Controller):
    def __init__(self, app_title: str, db_folder: str, db_name: str):
        self.initialize_db(db_folder=db_folder, db_name=db_name)
        self.model = AppModel(app_title=app_title, user_repository=self.u_repo, transaction_manager=self.t_man)
        self.view = AppView(model=self.model, fg_color="blue")


    @property
    def model(self) -> Model:
        return self.__model
    
    
    @model.setter
    def model(self, value: Model):
        self.__model = value


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
        self.view.create_login_form()
        self.view.login_controller.run()
        # self.view.after(500, lambda: self.model.user_id_var.set(2))
        # self.view.after(500, lambda: self.model.username_var.set("mirasol"))
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

        self.controller_per_page: Dict[str, ProfilePageController | HomePageController | EditPageController | HistoryPageController | AddPageController] = {
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
        self.view.after(1500, lambda: print("[DEBUG] app closed successfully"))


    def update_display(self):
        pass


# #--------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
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

