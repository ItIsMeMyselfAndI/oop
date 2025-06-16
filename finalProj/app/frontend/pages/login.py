# external/built-in modules/libs
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import os
import sys
# our modules/libs
from frontend.styles import BaseStyles, LoginStyles # paddings, dimensions, colors, etc
from backend import Account


#--------------------------------------------------------------------------------------------------------


class LoginForm(ctk.CTkFrame):
    def __init__(self, userRepo, user_id, username, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id: ctk.StringVar = user_id
        self.username: ctk.StringVar = username
        self.userRepo = userRepo

        self.initializePageState()

        self.createHeader()
        self.createEntries()
        self.createBTNs()
        self.bindKey()


    def initializePageState(self):
        self.mask_id = None
        self.actual_password = ""
        self.isCurrentPage = False


    def _loadIcon(self):
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


    def createHeader(self):
        # logo
        self.logo_icon = self._loadIcon()
        self.logo_img_bg = ctk.CTkLabel(
            master=self, text="",
            image=self.logo_icon,
            fg_color=LoginStyles.LOGO_IMG_BG_COLOR,
            width=LoginStyles.LOGO_IMG_BG_W,
            height=LoginStyles.LOGO_IMG_BG_H
        )
        self.logo_img_bg.pack(pady=(BaseStyles.PAD_4*2,BaseStyles.PAD_1))
        
        # title
        self.title_label = ctk.CTkLabel(
            master=self,
            text="Welcome!",
            font=LoginStyles.TITLE_LABEL_FONT,
            text_color=LoginStyles.TITLE_TEXT_COLOR,
            fg_color=LoginStyles.TITLE_LABEL_FG_COLOR
        )
        self.title_label.pack(padx=BaseStyles.PAD_4*2, pady=(0,BaseStyles.PAD_5))


    def createEntries(self):
        # username entry
        self.uname_entry = ctk.CTkEntry(
            master=self,
            fg_color=LoginStyles.uname_entry_FG_COLOR,
            font=LoginStyles.uname_entry_FONT,
            text_color=LoginStyles.uname_entry_TEXT_COLOR,
            placeholder_text="Username",
            placeholder_text_color=LoginStyles.USER_PLACEHOLDER_TEXT_COLOR,
            width=LoginStyles.uname_entry_W,
            height=LoginStyles.uname_entry_H,
            corner_radius=BaseStyles.RAD_5,
            border_width=0 
        )
        self.uname_entry.pack(padx=BaseStyles.PAD_4*2, pady=(0,BaseStyles.PAD_1))

        # password entry
        self.pass_entry = ctk.CTkEntry(
            master=self,
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


    def createBTNs(self):
        # login button 
        self.login_button = ctk.CTkButton(
            master=self,
            text="LOGIN",
            font=LoginStyles.LOGIN_BTN_FONT,
            corner_radius=BaseStyles.RAD_5,
            text_color=LoginStyles.LOGIN_BTN_TEXT_COLOR,
            hover_color=LoginStyles.LOGIN_BTN_HOVER_COLOR,
            fg_color=LoginStyles.LOGIN_BTN_FG_COLOR,
            width=LoginStyles.LOGIN_BTN_W,
            height=LoginStyles.LOGIN_BTN_H,
            command=self.onClickLogin
        )
        self.login_button.pack(padx=BaseStyles.PAD_4*2, pady=(0,BaseStyles.PAD_1))
        
        # signin button 
        self.signup_button = ctk.CTkButton(
            master=self,
            text="SIGN UP",
            font=LoginStyles.SIGNUP_BTN_FONT,
            corner_radius=BaseStyles.RAD_5,
            text_color=LoginStyles.SIGNUP_BTN_TEXT_COLOR,
            hover_color=LoginStyles.SIGNUP_BTN_HOVER_COLOR,
            fg_color=LoginStyles.SIGNUP_BTN_FG_COLOR,
            width=LoginStyles.SIGNUP_BTN_W,
            height=LoginStyles.SIGNUP_BTN_H,
            command=self.onClickSignUp
        )
        self.signup_button.pack(padx=BaseStyles.PAD_4*2, pady=(0,BaseStyles.PAD_4*2))

        
    def onClickLogin(self):
        print("\n[User] LoginStyles")
        username = self.uname_entry.get()
        password = self.actual_password

        account = Account(username=username, password=password)
        user_id = self.userRepo.getAccountID(account)
        if not (account.username and account.password):
            messagebox.showwarning(title="[Invalid] Input", message="Empty field is not allowed")
            print("[Input] Empty field is not allowed")

        elif user_id:
            self.user_id.set(user_id)
            self.username.set(username)
            print("\tUsername:", username)
            print("\tPassword:", password)
            self.place_forget()
            self.update_idletasks()

        else:
            messagebox.showwarning(title="[DB] No Match Found", message="Incorrect Username or Password")
            print("[DB] No Match Found")


    def onClickSignUp(self):
        print("\n[User] Sign Up")
        username = self.uname_entry.get()
        password = self.actual_password
        account = Account(username=username, password=password)

        # verify action
        is_continue = messagebox.askyesno(title="[Sign Up] New Account",message="Do you want to create a new account?") 
        if not is_continue:
            return
        
        # create new account
        was_added = self.userRepo.addAccount(account)
        if not (account.username and account.password):
            messagebox.showwarning(title="[Invalid] Input", message="Empty field is not allowed")
            print("[Input] Empty field is not allowed")

        elif was_added:
            user_id = self.userRepo.getAccountID(account)
            self.user_id.set(user_id)
            self.username.set(username)
            print("\tUsername:", username)
            print("\tPassword:", password)
            self.place_forget()
            self.update_idletasks()

        else:
            messagebox.showwarning(title="[Invalid] Input", message="Username is already taken")
            print("[Input] Username is already taken")


    def _maskPassword(self):
        # hide pass display
        self.pass_entry.delete(0, ctk.END)
        self.pass_entry.insert(0, self.actual_password)
        self.pass_entry.configure(show="*")


    def onPasswordKeyRelease(self, event):
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
        self.mask_id = self.after(1000, self._maskPassword)
    
    
    def bindKey(self):
        self.pass_entry.bind("<KeyRelease>", self.onPasswordKeyRelease)

