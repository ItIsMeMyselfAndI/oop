# external/built-in modules/libs
import customtkinter as ctk
from PIL import Image
import os
import sys
# our modules/libs
from frontend.styles import BaseStyles, ProfileStyles # paddings, dimensions, colors, etc

from backend import TransactionManager, Finance # db manager

from models.base_model import Model
from controllers.base_controller import Controller


#--------------------------------------------------------------------------------------------------------


class ProfilePageModel(Model):
    def __init__(self, transaction_manager: TransactionManager, user_id_var: ctk.IntVar, username_var: ctk.StringVar):
        self.initialize_managers(transaction_manager)
        self.initialize_vars(user_id_var, username_var)        
        
        self.is_current_page = False
        self.finance = Finance(0, 0, 0, 0)
        self.balance = 0


    def initialize_managers(self, transaction_manager: TransactionManager):
        self.t_man = transaction_manager
    

    def initialize_vars(self, user_id_var: ctk.IntVar, username_var: ctk.StringVar):
        self.user_id_var = user_id_var
        self.username_var = username_var


    def load_amounts(self):
        self.finance = self.t_man.calculateOverallFinance(int(self.user_id_var.get()))
        self.balance = self.t_man.calculateOverallBalance(self.finance)


#--------------------------------------------------------------------------------------------------------
    

class ProfilePageView(ctk.CTkFrame):
    def __init__(self, model, master, **kwargs):
        super().__init__(master, **kwargs)
        self.model = model
        

    def create(self):
        print("\n[DEBUG] creating profile page...")
        self.model.load_amounts()
        self._load_icons()
        self._create_header()
        self._create_summaries()
        self.update_idletasks()
        print("[DEBUG] profile page created successfully")


    def _load_icons(self):
        print("[DEBUG] loading profile page icons...")
        # icon path
        if hasattr(sys, "_MEIPASS"): # for .py: memory resources
            _MEIPASS: str = getattr(sys, "_MEIPASS")
            ICONS_FOLDER = os.path.join(_MEIPASS, "assets/icons")
        else: # for .py: true path resources
            ICONS_FOLDER = "assets/icons"

        # load images
        self.profile_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "profile1.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "profile1.png")),
            size=(ProfileStyles.PROFILE_IMG_H, ProfileStyles.PROFILE_IMG_W)
        )
        self.income_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "income.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "income.png")),
            size=(ProfileStyles.SUMMARY_IMG_H, ProfileStyles.SUMMARY_IMG_W)
        )
        self.savings_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "savings.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "savings.png")),
            size=(ProfileStyles.SUMMARY_IMG_H, ProfileStyles.SUMMARY_IMG_W)
        )
        self.expense_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "expense.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "expense.png")),
            size=(ProfileStyles.SUMMARY_IMG_H, ProfileStyles.SUMMARY_IMG_W)
        )
        self.investment_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "investment.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "investment.png")),
            size=(ProfileStyles.SUMMARY_IMG_H, ProfileStyles.SUMMARY_IMG_W)
        )
        print("[DEBUG] profile page icons loaded successfully")


    def _create_header(self):
        print("[DEBUG] creating header...")
        self.header = Header(
            img=self.profile_icon,
            uname=self.model.username_var.get().title(), 
            summary_type="Total Balance:",
            amount=self.model.balance,
            master=self,
            fg_color=ProfileStyles.HEADER_SECTION_COLOR,
            corner_radius=BaseStyles.RAD_2
        )
        self.header.pack(pady=(BaseStyles.PAD_5+BaseStyles.PAD_5,0))
        self.update_idletasks()
        print("[DEBUG] header created successfully")


    def _create_summaries(self):
        print("[DEBUG] creating transaction summaries...")
        # summaries section
        self.summary_section = ctk.CTkFrame(
            master=self,
            fg_color=ProfileStyles.SUMMARY_SECTION_COLOR,
            corner_radius=BaseStyles.RAD_2
        )
        self.summary_section.pack(pady=(BaseStyles.PAD_2,0))

        # income summary
        self.income_frame = SummarySection(
            img=self.income_icon,
            img_bg_color=ProfileStyles.INCOME_IMG_BG_COLOR,
            summary_type="Total Income:",
            amount=self.model.finance.total_income,
            master=self.summary_section,
            fg_color=ProfileStyles.INCOME_FRAME_FG_COLOR,
            corner_radius=BaseStyles.RAD_2
        )
        self.income_frame.grid(row=0, column=0, padx=(BaseStyles.PAD_4,0), pady=(BaseStyles.PAD_4,0), sticky="nsew")

        # expense summary
        self.expense_frame = SummarySection(
            img=self.expense_icon,
            img_bg_color=ProfileStyles.EXPENSE_IMG_BG_COLOR,
            summary_type="Total Expenses:",
            amount=self.model.finance.total_expenses,
            master=self.summary_section,
            fg_color=ProfileStyles.EXPENSE_FRAME_FG_COLOR,
            corner_radius=BaseStyles.RAD_2
        )
        self.expense_frame.grid(row=0, column=1, padx=BaseStyles.PAD_4, pady=(BaseStyles.PAD_4,0), sticky="nsew")

        # savings summary
        self.savings_frame = SummarySection(
            img=self.savings_icon,
            img_bg_color=ProfileStyles.SAVINGS_IMG_BG_COLOR,
            summary_type="Total Savings:",
            amount=self.model.finance.total_savings,
            master=self.summary_section,
            fg_color=ProfileStyles.SAVINGS_FRAME_FG_COLOR,
            corner_radius=BaseStyles.RAD_2
        )
        self.savings_frame.grid(row=1, column=0, padx=(BaseStyles.PAD_4,0), pady=BaseStyles.PAD_4, sticky="nsew")

        # investment summary
        self.investment_frame = SummarySection(
            img=self.investment_icon,
            img_bg_color=ProfileStyles.INVESt_manENT_IMG_BG_COLOR, 
            summary_type="Total Investment:",
            amount=self.model.finance.total_investment,
            master=self.summary_section,
            fg_color=ProfileStyles.INVESt_manENT_FRAME_FG_COLOR,
            corner_radius=BaseStyles.RAD_2
        )
        self.investment_frame.grid(row=1, column=1, pady=BaseStyles.PAD_4, padx=BaseStyles.PAD_4, sticky="nsew")
        self.update_idletasks()
        print("[DEBUG] transaction summaries created successfully")


#--------------------------------------------------------------------------------------------------------


class ProfilePageController(Controller):
    def __init__(self, transaction_manager: TransactionManager, user_id_var: ctk.IntVar, username_var: ctk.StringVar, master):
        self.model = ProfilePageModel(transaction_manager=transaction_manager, user_id_var=user_id_var, username_var=username_var)
        self.view = ProfilePageView(model=self.model, master=master, fg_color=ProfileStyles.MAIN_FRAME_FG_COLOR)


    def run(self):
        pass


    def update_display(self):
        print("[DEBUG] updating profile page display...")
        self.model.load_amounts()
        self.view.header.balance_amount_label.configure(text=f"₱ {self.model.balance:,}")
        self.view.income_frame.summary_amount_label.configure(text=f"₱ {self.model.finance.total_income:,}")
        self.view.expense_frame.summary_amount_label.configure(text=f"₱ {self.model.finance.total_expenses:,}")
        self.view.savings_frame.summary_amount_label.configure(text=f"₱ {self.model.finance.total_savings:,}")
        self.view.investment_frame.summary_amount_label.configure(text=f"₱ {self.model.finance.total_investment:,}")
        self.view.update_idletasks()
        print("[DEBUG] profile page display updated successfully")


#--------------------------------------------------------------------------------------------------------


class Header(ctk.CTkFrame):
    def __init__(self, img: ctk.CTkImage, uname: str, summary_type: str, amount: float, master, **kwargs):
        super().__init__(master, ** kwargs)
        self.font4 = ("Arial", BaseStyles.FONT_SIZE_4, "normal")
        self.font6 = ("Arial", BaseStyles.FONT_SIZE_6, "normal")

        self.create(img, uname, summary_type, amount)


    def create(self, img: ctk.CTkImage, uname: str, summary_type: str, amount: float):
        self._create_icon(img)
        self._create_username(uname)
        self._create_balance(summary_type, amount)
        

    def _create_icon(self, img: ctk.CTkImage):
        print("[DEBUG] creating icon...")
        self.img = img
        self.img_bg = ctk.CTkLabel(
            master=self,
            corner_radius=BaseStyles.RAD_2,
            fg_color=ProfileStyles.PROFILE_IMG_BG_COLOR,
            image=img,
            text="",
            width=ProfileStyles.PROFILE_IMG_BG_W,
            height=ProfileStyles.PROFILE_IMG_BG_H
        )
        self.img_bg.grid(row=0, column=0, pady=BaseStyles.PAD_2, padx=BaseStyles.PAD_2)
        self.update_idletasks()
        print("[DEBUG] icon created successfully")

    
    def _create_username(self, uname: str):
        print("[DEBUG] creating username...")
        self.uname_frame = ctk.CTkFrame(
            master=self,
            corner_radius=BaseStyles.RAD_2,
            fg_color=ProfileStyles.UNAME_FRAME_FG_COLOR
        )
        self.uname_label = ctk.CTkLabel(
            master=self.uname_frame,
            text=f"Hi there,\n{uname}!",
            font=self.font6,
            text_color=ProfileStyles.UNAME_TEXT_COLOR,
            width=ProfileStyles.UNAME_LABEL_W,
            wraplength=ProfileStyles.UNAME_LABEL_W,
            fg_color=ProfileStyles.UNAME_LABEL_FG_COLOR,
            anchor="w",
            justify="left"
        ) 
        self.uname_frame.grid(row=0, column=1, padx=(0,BaseStyles.PAD_2))
        self.uname_label.pack(anchor="w")
        self.update_idletasks()
        print("[DEBUG] username created successfully")


    def _create_balance(self, summary_type: str, amount: float):
        print("[DEBUG] creating balance...")
        self.balance_frame = ctk.CTkFrame(
            master=self,
            corner_radius=BaseStyles.RAD_2,
            fg_color=ProfileStyles.BALANCE_FRAME_FG_COLOR
        )
        self.balance_title_label = ctk.CTkLabel(
            master=self.balance_frame,
            text=summary_type,
            font=self.font4,
            text_color=ProfileStyles.BALANCE_TITLE_TEXT_COLOR,
            fg_color=ProfileStyles.BALANCE_TITLE_LABEL_FG_COLOR,
            anchor="e"
        )
        self.balance_amount_label = ctk.CTkLabel(
            master=self.balance_frame,
            text=f"₱ {amount:,}",
            font=self.font6,
            text_color=ProfileStyles.BALANCE_AMOUNT_TEXT_COLOR,
            width=ProfileStyles.BALANCE_AMOUNT_LABEL_W,
            wraplength=ProfileStyles.BALANCE_AMOUNT_LABEL_W, 
            fg_color=ProfileStyles.BALANCE_AMOUNT_LABEL_FG_COLOR,
            anchor="e",
            justify="right"
        )
        self.balance_frame.grid(row=0, column=2, padx=(0,BaseStyles.PAD_4))
        self.balance_title_label.pack(anchor="e")
        self.balance_amount_label.pack(anchor="e")
        self.update_idletasks()
        print("[DEBUG] balance created successfully")


#--------------------------------------------------------------------------------------------------------


class SummarySection(ctk.CTkFrame):
    def __init__(self, img: ctk.CTkImage, img_bg_color: str, summary_type: str, amount: float, master, **kwargs):
        super().__init__(master, ** kwargs)
        self.font4 = ("Arial", BaseStyles.FONT_SIZE_4, "normal")
        self.font6 = ("Arial", BaseStyles.FONT_SIZE_6, "normal")

        self.create(img, img_bg_color, summary_type, amount)


    def create(self, img: ctk.CTkImage, img_bg_color: str, summary_type: str, amount: float):
        self._create_icon(img, img_bg_color)
        self._create_summary(summary_type, amount)
        
        
    def _create_icon(self, img: ctk.CTkImage, img_bg_color: str):
        print("[DEBUG] creating icon...")
        self.img = img
        self.img_bg = ctk.CTkLabel(
            master=self,
            height=ProfileStyles.SUMMARY_IMG_FRAME_H,
            width=ProfileStyles.SUMMARY_IMG_FRAME_W,
            corner_radius=BaseStyles.RAD_2,
            fg_color=img_bg_color,
            image=img,
            text=""
        )
        self.img_bg.grid(row=0, column=0, padx=(BaseStyles.PAD_5, 0), pady=BaseStyles.PAD_5)
        self.update_idletasks()
        print("[DEBUG] icon created successfully")


    def _create_summary(self, summary_type: str, amount: float):
        print(f"[DEBUG] creating {summary_type}...")
        self.summary_frame = ctk.CTkFrame(
            master=self,
            width=ProfileStyles.SUMMARY_IMG_FRAME_W,
            corner_radius=BaseStyles.RAD_2,
            fg_color=ProfileStyles.SUMMARY_DETAILS_FRAME_FG_COLOR
        )
        self.summary_title_label = ctk.CTkLabel(
            master=self.summary_frame,
            text=summary_type,
            font=self.font4,
            text_color=ProfileStyles.SUMMARY_TITLE_TEXT_COLOR, 
            fg_color=ProfileStyles.SUMMARY_TITLE_LABEL_FG_COLOR,
            anchor="w"
        )
        self.summary_amount_label = ctk.CTkLabel(
            master=self.summary_frame,
            text=f"₱ {amount:,}",
            font=self.font6,
            text_color=ProfileStyles.SUMMARY_AMOUNT_TEXT_COLOR,
            width=ProfileStyles.SUMMARY_AMOUNT_LABEL_W,
            wraplength=ProfileStyles.SUMMARY_AMOUNT_LABEL_W,
            fg_color=ProfileStyles.SUMMARY_AMOUNT_LABEL_FG_COLOR,
            anchor="w"
        )
        self.summary_frame.grid(row=0, column=1, padx=(BaseStyles.PAD_3, BaseStyles.PAD_5), pady=BaseStyles.PAD_1)
        self.summary_title_label.pack(anchor="w")
        self.summary_amount_label.pack(anchor="w")
        self.update_idletasks()
        print(f"[DEBUG] {summary_type} created successfully")