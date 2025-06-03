# external/built-in modules/libs
import customtkinter as ctk
from PIL import Image
import os
# our modules/libs
from frontend.styles import BaseStyles # paddings, dimensions, colors, etc
from backend import Account
from frontend.components import PopUpWin

class LoginWin(ctk.CTk):
    def __init__(self, app_title, userRepo, fg_color, width, height):
        super().__init__()
        self.user_id = None
        self.username = None
        self.userRepo = userRepo
        # initialize login
        x_pos, y_pos = 0, 0
        self.geometry(f"{width}x{height}+{x_pos}+{y_pos}")
        self.configure(fg_color=fg_color)
        self.title(app_title)
        # initialize page state
        self.mask_id = None
        self.actual_password = ""
        self.isCurrentPage = False
        # load logo
        self.logo = self.loadImages()
        # create login frame
        self.frame = ctk.CTkFrame(master=self, fg_color=BaseStyles.WHITE, width=550, height=800, corner_radius=50)
        # create header
        self.logo_icon = ctk.CTkLabel(self.frame, text="", image=self.logo)
        self.title_label = ctk.CTkLabel(master=self.frame, text="Welcome!", font=("Arial", 35, "bold"),
                                            text_color="#333333", bg_color="#ffffff")
        # create entries
        self.outside_entry = ctk.CTkEntry(self)
        self.user_entry = ctk.CTkEntry(master=self.frame, font=("Arial", 17, "bold"), text_color="#292929",
                                   corner_radius=50, border_width=0, placeholder_text="Username",
                                   placeholder_text_color="#545454",
                                   fg_color="#d9d9d9", bg_color="#ffffff",
                                   width=350, height=60)
        self.pass_entry = ctk.CTkEntry(master=self.frame, font=("Arial", 17, "bold"), text_color="#292929",
                                   corner_radius=50, border_width=0, placeholder_text="Password",
                                   placeholder_text_color="#545454",
                                   width=350, height=60,
                                   fg_color="#d9d9d9", bg_color="#ffffff")
        # create buttons
        self.login_button = ctk.CTkButton(master=self.frame, text="LOGIN", font=("Arial", 20, "bold"), corner_radius=50,
                                          text_color="#ffffff", hover_color=BaseStyles.DARK_BLUE,
                                          fg_color=BaseStyles.BLUE, bg_color="#ffffff",
                                          width=350, height=60,
                                          command=self.onClickLogin)
        self.signup_button = ctk.CTkButton(master=self.frame, text="SIGN UP", font=("Arial", 20, "bold"), corner_radius=50,
                                           text_color="#ffffff", hover_color=BaseStyles.GREEN,
                                           fg_color="#7ed957", bg_color="#ffffff",
                                           width=350, height=60,
                                           command=self.onClickSignUp)
        # display main frame
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        # display header
        self.logo_icon.pack(pady=(80,10))
        self.title_label.pack(padx=80, pady=(0,50))
        # display entries
        self.outside_entry.place(x=-1000, y=-1000) # for redirecting entry focus when clicked outside
        self.user_entry.pack(padx=80, pady=(0,10))
        self.pass_entry.pack(padx=80, pady=(0,30))
        # display buttons
        self.login_button.pack(padx=80, pady=(0,10))
        self.signup_button.pack(padx=80, pady=(0,80))
        # bind keyboard and mouse events
        self.pass_entry.bind("<KeyRelease>", self.on_password_key_release)
        # unfocus entries if clicked outside
        self.bind("<Button-1>", self.unfocusEntries)
        # create invalid input pop up
        self.font2 = ("Bodoni MT", BaseStyles.FONT_SIZE_2, "italic")
        self.no_match_popup = PopUpWin(title="[DB] No Match", msg="Incorrect Username or Password",
                                      enable_close=True, font=self.font2, master=self,
                                      fg_color=BaseStyles.WHITE, enable_frame_blocker=False)
        self.already_taken_popup = PopUpWin(title="[Input] Invalid", msg="Username is already taken",
                                      enable_close=True, font=self.font2, master=self,
                                      fg_color=BaseStyles.WHITE, enable_frame_blocker=False)
        self.empty_field_popup = PopUpWin(title="[Input] Invalid", msg="Empty field is not allowed",
                                      enable_close=True, font=self.font2, master=self,
                                      fg_color=BaseStyles.WHITE, enable_frame_blocker=False)

    def loadImages(self):
        ICONS_FOLDER = os.path.abspath("assets/icons")
        logo = ctk.CTkImage(Image.open(f"{ICONS_FOLDER}/logo.png"), size=(119, 120))
        return logo

    def onClickLogin(self):
        print("\n[User] Login")
        username = self.user_entry.get()
        password = self.actual_password
        account = Account(username=username, password=password)
        user_id = self.userRepo.getAccountID(account)
        if not (account.username and account.password):
            self.empty_field_popup.showWin()
            print("[Input] Empty field is not allowed")
        elif user_id:
            self.user_id = user_id
            self.username = username
            print("\tUsername:", username)
            print("\tPassword:", password)
            self.destroy()
        else:
            self.no_match_popup.showWin()
            print("[DB] No Match Found")

    def onClickSignUp(self):
        print("\n[User] Sign Up")
        username = self.user_entry.get()
        password = self.actual_password
        account = Account(username=username, password=password)
        was_added = self.userRepo.addAccount(account)
        if not (account.username and account.password):
            self.empty_field_popup.showWin()
            print("[Input] Empty field is not allowed")
        elif was_added:
            self.user_id = self.userRepo.getAccountID(account)
            self.username = username
            print("\tUsername:", username)
            print("\tPassword:", password)
            self.destroy()
        else:
            self.already_taken_popup.showWin()
            print("[Input] Username is already taken")

    def on_password_key_release(self, event):
        # cancel masking
        if self.mask_id:
            self.after_cancel(self.mask_id)
            self.mask_id = None
        # update pass
        self.actual_password = self.pass_entry.get()
        # temporarily show the actual password
        self.pass_entry.delete(0, ctk.END)
        self.pass_entry.insert(0, self.actual_password)
        self.pass_entry.configure(show="")
        # mask pass after 1 secs
        self.mask_id = self.after(1000, self.mask_password)

    def mask_password(self):
        # hide pass display
        self.pass_entry.delete(0, ctk.END)
        self.pass_entry.insert(0, self.actual_password)
        self.pass_entry.configure(show="*")

    def unfocusEntries(self, event):
        print()
        print(event)
        print(f"{event.widget.winfo_class() == "Entry" = }")
        if not event.widget.winfo_class() == "Entry":
            self.outside_entry.focus_set()