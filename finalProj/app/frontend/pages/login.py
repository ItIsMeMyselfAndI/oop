# external/built-in modules/libs
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import os
import sys
# our modules/libs
from frontend.styles import BaseStyles, LoginStyles # paddings, dimensions, colors, etc
from backend import Account
from frontend.components import PopUpWin


#--------------------------------------------------------------------------------------------------------


class LoginWin(ctk.CTk):
    def __init__(self, app_title, userRepo, fg_color, width, height):
        super().__init__()
        self.user_id = None
        self.username = None
        self.userRepo = userRepo

        # initialize login
        x_pos, y_pos = 0, 0
        self.geometry(f"{width}x{height}+{x_pos}+{y_pos}")
        self.maxsize(width, height)
        self.minsize(width, height)
        self.resizable(width=True, height=True)
        self.configure(fg_color=fg_color)
        self.title(app_title)

        # initialize page state
        self.mask_id = None
        self.actual_password = ""
        self.isCurrentPage = False

        # form frame
        self.form_frame = ctk.CTkFrame(
            master=self,
            fg_color=LoginStyles.LOGIN_FRAME_FG_COLOR,
            corner_radius=BaseStyles.RAD_5
        )
        self.form_frame.place(relx=0.5, rely=0.5, anchor="center")

        # logo
        self.logo_icon = self.loadImages()
        self.logo_img_bg = ctk.CTkLabel(
            master=self.form_frame, text="",
            image=self.logo_icon,
            fg_color=LoginStyles.LOGO_IMG_BG_COLOR,
            width=LoginStyles.LOGO_IMG_BG_W,
            height=LoginStyles.LOGO_IMG_BG_H
        )
        self.logo_img_bg.pack(pady=(BaseStyles.PAD_4*2,BaseStyles.PAD_1))
        
        # title
        self.title_label = ctk.CTkLabel(
            master=self.form_frame,
            text="Welcome!",
            font=LoginStyles.TITLE_LABEL_FONT,
            text_color=LoginStyles.TITLE_TEXT_COLOR,
            fg_color=LoginStyles.TITLE_LABEL_FG_COLOR
        )
        self.title_label.pack(padx=BaseStyles.PAD_4*2, pady=(0,BaseStyles.PAD_5))

        # username entry
        self.user_entry = ctk.CTkEntry(
            master=self.form_frame,
            fg_color=LoginStyles.USER_ENTRY_FG_COLOR,
            font=LoginStyles.USER_ENTRY_FONT,
            text_color=LoginStyles.USER_ENTRY_TEXT_COLOR,
            placeholder_text="Username",
            placeholder_text_color=LoginStyles.USER_PLACEHOLDER_TEXT_COLOR,
            width=LoginStyles.USER_ENTRY_W,
            height=LoginStyles.USER_ENTRY_H,
            corner_radius=BaseStyles.RAD_5,
            border_width=0 
        )
        self.user_entry.pack(padx=BaseStyles.PAD_4*2, pady=(0,BaseStyles.PAD_1))

        # password entry
        self.pass_entry = ctk.CTkEntry(
            master=self.form_frame,
            fg_color=LoginStyles.PASS_ENTRY_FG_COLOR,
            font=LoginStyles.PASS_ENTRY_FONT,
            text_color=LoginStyles.PASS_ENTRY_TEXT_COLOR,
            placeholder_text="Password",
            placeholder_text_color=LoginStyles.PASS_PLACEHOLDER_TEXT_COLOR,
            width=LoginStyles.PASS_ENTRY_W,
            height=LoginStyles.PASS_ENTRY_H,
            corner_radius=BaseStyles.RAD_5,
            border_width=0
        )
        self.pass_entry.pack( padx=BaseStyles.PAD_4*2, pady=(0,BaseStyles.PAD_3))
        self.pass_entry.bind("<KeyRelease>", self.on_password_key_release)

        # login button 
        self.login_button = ctk.CTkButton(
            master=self.form_frame,
            text="LOGIN",
            font=LoginStyles.LOGIN_BUTTON_FONT,
            corner_radius=BaseStyles.RAD_5,
            text_color=LoginStyles.LOGIN_BUTTON_TEXT_COLOR,
            hover_color=LoginStyles.LOGIN_BUTTON_HOVER_COLOR,
            fg_color=LoginStyles.LOGIN_BUTTON_FG_COLOR,
            width=LoginStyles.LOGIN_BUTTON_W,
            height=LoginStyles.LOGIN_BUTTON_H,
            command=self.onClickLogin
        )
        self.login_button.pack(padx=BaseStyles.PAD_4*2, pady=(0,BaseStyles.PAD_1))
        
        # signin button 
        self.signup_button = ctk.CTkButton(
            master=self.form_frame,
            text="SIGN UP",
            font=LoginStyles.SIGNUP_BUTTON_FONT,
            corner_radius=BaseStyles.RAD_5,
            text_color=LoginStyles.SIGNUP_BUTTON_TEXT_COLOR,
            hover_color=LoginStyles.SIGNUP_BUTTON_HOVER_COLOR,
            fg_color=LoginStyles.SIGNUP_BUTTON_FG_COLOR,
            width=LoginStyles.SIGNUP_BUTTON_W,
            height=LoginStyles.SIGNUP_BUTTON_H,
            command=self.onClickSignUp
        )
        self.signup_button.pack(padx=BaseStyles.PAD_4*2, pady=(0,BaseStyles.PAD_4*2))

        # dummy entry: for redirecting focus away from main entries
        self.outside_entry = ctk.CTkEntry(self)
        self.outside_entry.place(x=-1*BaseStyles.SCREEN_W, y=-1*BaseStyles.SCREEN_W)

        # mouse left click 
        self.bind("<Button-1>", self.onClickNonEntry)


    def loadImages(self):
        if hasattr(sys, "_MEIPASS"): # # for .exe: memory resources path
            ICONS_FOLDER = os.path.join(sys._MEIPASS, "assets/icons")
        else: # for .py: storage resources path
            ICONS_FOLDER = "assets/icons"
        print(ICONS_FOLDER)
        
        # load image
        logo_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "logo.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "logo.png")),
            size=(LoginStyles.LOGO_IMG_W, LoginStyles.LOGO_IMG_H)
        )
        return logo_icon


    def onClickLogin(self):
        print("\n[User] LoginStyles")
        username = self.user_entry.get()
        password = self.actual_password
        account = Account(username=username, password=password)
        user_id = self.userRepo.getAccountID(account)
        if not (account.username and account.password):
            # self.empty_field_popup.showWin()
            messagebox.showwarning(title="[Input] Invalid", message="Empty field is not allowed")
            print("[Input] Empty field is not allowed")
        elif user_id:
            self.user_id = user_id
            self.username = username
            print("\tUsername:", username)
            print("\tPassword:", password)
            self.destroy()
        else:
            messagebox.showwarning(title="[DB] No Match Found", message="Incorrect Username or Password")
            # self.no_match_popup.showWin()
            print("[DB] No Match Found")


    def onClickSignUp(self):
        print("\n[User] Sign Up")
        username = self.user_entry.get()
        password = self.actual_password
        account = Account(username=username, password=password)
        # verify action
        is_continue = messagebox.askyesno(title="[Sign Up] New Account",message="Do you want to create a new account?") 
        if not is_continue:
            return
        # create new account
        was_added = self.userRepo.addAccount(account)
        if not (account.username and account.password):
            # self.empty_field_popup.showWin()
            messagebox.showwarning(title="[Input] Invalid", message="Empty field is not allowed")
            print("[Input] Empty field is not allowed")
        elif was_added:
            self.user_id = self.userRepo.getAccountID(account)
            self.username = username
            print("\tUsername:", username)
            print("\tPassword:", password)
            self.destroy()
        else:
            # self.already_taken_popup.showWin()
            messagebox.showwarning(title="[Input] Invalid", message="Username is already taken")
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


    def _unfocusEntries(self, event):
        print()
        print(event)
        print(f"{event.widget.winfo_class() == "Entry" = }")
        if not event.widget.winfo_class() == "Entry":
            self.outside_entry.focus_set()


    def onClickNonEntry(self, event):
        self._unfocusEntries(event=event)