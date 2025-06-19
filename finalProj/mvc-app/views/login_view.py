# external/built-in modules/libs
import customtkinter as ctk
from PIL import Image
import os
import sys
# our modules/libs
from frontend.styles import BaseStyles, LoginStyles # paddings, dimensions, colors, etc


#--------------------------------------------------------------------------------------------------------


class LoginPageView(ctk.CTkFrame):
    def __init__(self, model, page_fg_color, form_fg_color, master, **kwargs):
        super().__init__(master, **kwargs)
        self.model = model
        self.initialize_page_state()
        self.page_fg_color = page_fg_color
        self.form_fg_color = form_fg_color
        self.create() 


    def initialize_page_state(self):
        self.mask_id = None
        self.actual_password = ""


    def create(self):
        self._load_icon()
        self._create_form_frame()
        self._create_header()
        self._create_entries()
        self._create_btns()


    def _load_icon(self) -> ctk.CTkImage:
        if hasattr(sys, "_MEIPASS"): # # for .exe: memory resources path
            _MEIPASS: str = getattr(sys, "_MEIPASS")
            ICONS_FOLDER: str = os.path.join(_MEIPASS, "assets/icons")
        else: # for .py: storage resources path
            ICONS_FOLDER = "assets/icons"
        
        # load image
        self.logo_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "logo.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "logo.png")),
            size=(LoginStyles.LOGO_IMG_W, LoginStyles.LOGO_IMG_H)
        )


    def _create_form_frame(self):
        self.configure(fg_color=self.page_fg_color)
        self.form = ctk.CTkFrame(master=self, fg_color=self.form_fg_color, corner_radius=BaseStyles.RAD_5)
        self.form.place(relx=0.5, rely=0.5, anchor="center")


    def _create_header(self):
        # logo
        self.logo_img_bg = ctk.CTkLabel(
            master=self.form, text="",
            image=self.logo_icon,
            fg_color=LoginStyles.LOGO_IMG_BG_COLOR,
            width=LoginStyles.LOGO_IMG_BG_W,
            height=LoginStyles.LOGO_IMG_BG_H
        )
        self.logo_img_bg.pack(pady=(BaseStyles.PAD_4*2,BaseStyles.PAD_2))
        
        # title
        self.title_label = ctk.CTkLabel(
            master=self.form,
            text="Welcome!",
            font=LoginStyles.TITLE_LABEL_FONT,
            text_color=LoginStyles.TITLE_TEXT_COLOR,
            fg_color=LoginStyles.TITLE_LABEL_FG_COLOR
        )
        self.title_label.pack(padx=BaseStyles.PAD_4*2, pady=(0,BaseStyles.PAD_3))


    def _create_entries(self):
        # username entry
        self.uname_entry = ctk.CTkEntry(
            master=self.form,
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
            master=self.form,
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


    def _create_btns(self):
        # login button 
        self.login_button = ctk.CTkButton(
            master=self.form,
            text="LOGIN",
            font=LoginStyles.LOGIN_BTN_FONT,
            corner_radius=BaseStyles.RAD_5,
            text_color=LoginStyles.LOGIN_BTN_TEXT_COLOR,
            hover_color=LoginStyles.LOGIN_BTN_HOVER_COLOR,
            fg_color=LoginStyles.LOGIN_BTN_FG_COLOR,
            width=LoginStyles.LOGIN_BTN_W,
            height=LoginStyles.LOGIN_BTN_H,
        )
        self.login_button.pack(padx=BaseStyles.PAD_4*2, pady=(0,BaseStyles.PAD_1))
        
        # signin button 
        self.signup_button = ctk.CTkButton(
            master=self.form,
            text="SIGN UP",
            font=LoginStyles.SIGNUP_BTN_FONT,
            corner_radius=BaseStyles.RAD_5,
            text_color=LoginStyles.SIGNUP_BTN_TEXT_COLOR,
            hover_color=LoginStyles.SIGNUP_BTN_HOVER_COLOR,
            fg_color=LoginStyles.SIGNUP_BTN_FG_COLOR,
            width=LoginStyles.SIGNUP_BTN_W,
            height=LoginStyles.SIGNUP_BTN_H,
        )
        self.signup_button.pack(padx=BaseStyles.PAD_4*2, pady=(0,BaseStyles.PAD_4*2))
