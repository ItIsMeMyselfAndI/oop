# external/built-in modules/libs
import customtkinter as ctk
from PIL import Image
import os
# our modules/libs
from frontend.styles import BaseStyles, ProfileStyles # paddings, dimensions, colors, etc



class ProfileHeader(ctk.CTkFrame):
    def __init__(self, img, uname, summary_type, amount, master, **kwargs):
        super().__init__(master, ** kwargs)
        self.font4 = ("Bodoni MT", BaseStyles.FONT_SIZE_4, "italic")
        self.font6 = ("Bodoni MT", BaseStyles.FONT_SIZE_6, "italic")
        self.img = img
        # create guide frames
        self.img_bg = ctk.CTkLabel(self, corner_radius=BaseStyles.RAD_2, fg_color=ProfileStyles.PROFILE_IMG_BG_COLOR, image=img,
                                   text="", width=ProfileStyles.PROFILE_IMG_BG_W, height=ProfileStyles.PROFILE_IMG_BG_H)
        self.uname_frame = ctk.CTkFrame(self, corner_radius=BaseStyles.RAD_2, fg_color=ProfileStyles.UNAME_FRAME_FG_COLOR)
        self.balance_frame = ctk.CTkFrame(self, corner_radius=BaseStyles.RAD_2, fg_color=ProfileStyles.BALANCE_FRAME_FG_COLOR)
        # create label
        self.uname_label = ctk.CTkLabel(self.uname_frame, text=uname, font=self.font6, text_color=ProfileStyles.UNAME_TEXT_COLOR,
                                        width=ProfileStyles.UNAME_LABEL_W, wraplength=ProfileStyles.UNAME_LABEL_W,
                                        fg_color=ProfileStyles.UNAME_LABEL_FG_COLOR, anchor="w", justify="left") 
        self.balance_title_label = ctk.CTkLabel(self.balance_frame, text=summary_type, font=self.font4, text_color=ProfileStyles.BALANCE_TITLE_TEXT_COLOR,
                                               fg_color=ProfileStyles.BALANCE_TITLE_LABEL_FG_COLOR, anchor="e")
        self.amount_label = ctk.CTkLabel(self.balance_frame, text=f"₱ {amount:,}", font=self.font6, text_color=ProfileStyles.BALANCE_AMOUNT_TEXT_COLOR,
                                         width=ProfileStyles.BALANCE_AMOUNT_LABEL_W, wraplength=ProfileStyles.BALANCE_AMOUNT_LABEL_W, 
                                         fg_color=ProfileStyles.BALANCE_AMOUNT_LABEL_FG_COLOR, anchor="e", justify="right")
        # display guide frames
        self.img_bg.grid(row=0, column=0, pady=BaseStyles.PAD_2, padx=BaseStyles.PAD_2)
        self.uname_frame.grid(row=0, column=1, padx=(0,BaseStyles.PAD_2))
        self.balance_frame.grid(row=0, column=2, padx=(0,BaseStyles.PAD_4))
        # display labels
        self.uname_label.pack(anchor="w")
        self.balance_title_label.pack(anchor="e")
        self.amount_label.pack(anchor="e")


class SummarySection(ctk.CTkFrame):
    def __init__(self, img, img_bg_color, summary_type, amount, master, **kwargs):
        super().__init__(master, ** kwargs)
        self.font4 = ("Bodoni MT", BaseStyles.FONT_SIZE_4, "italic")
        self.font6 = ("Bodoni MT", BaseStyles.FONT_SIZE_6, "italic")
        self.img = img
        # create guide frames
        self.img_bg = ctk.CTkLabel(self, height=ProfileStyles.SUMMARY_IMG_FRAME_H, width=ProfileStyles.SUMMARY_IMG_FRAME_W,
                                   corner_radius=BaseStyles.RAD_2, fg_color=img_bg_color, image=img, text="")
        self.details_frame = ctk.CTkFrame(self, width=ProfileStyles.SUMMARY_IMG_FRAME_W, corner_radius=BaseStyles.RAD_2,
                                          fg_color=ProfileStyles.SUMMARY_DETAILS_FRAME_FG_COLOR)
        # create labels
        self.summary_title_label = ctk.CTkLabel(self.details_frame, text=summary_type, font=self.font4, text_color=ProfileStyles.SUMMARY_TITLE_TEXT_COLOR, 
                                               fg_color=ProfileStyles.SUMMARY_TITLE_LABEL_FG_COLOR, anchor="w")
        self.amount_label = ctk.CTkLabel(self.details_frame, text=f"₱ {amount:,}", font=self.font6, text_color=ProfileStyles.SUMMARY_AMOUNT_TEXT_COLOR,
                                         width=ProfileStyles.SUMMARY_AMOUNT_LABEL_W, wraplength=ProfileStyles.SUMMARY_AMOUNT_LABEL_W,
                                         fg_color=ProfileStyles.SUMMARY_AMOUNT_LABEL_FG_COLOR, anchor="w")
        # display guide frames
        self.img_bg.grid(row=0, column=0, padx=(BaseStyles.PAD_5, 0), pady=BaseStyles.PAD_5)
        self.details_frame.grid(row=0, column=1, padx=(BaseStyles.PAD_3, BaseStyles.PAD_5), pady=BaseStyles.PAD_1)
        # display labels
        self.summary_title_label.pack(anchor="w")
        self.amount_label.pack(anchor="w")


class ProfilePage(ctk.CTkFrame):
    def __init__(self, app, tm, master, **kwargs):
        super().__init__(master, ** kwargs)
        self.app = app
        self.tm = tm
        # initialize state
        self.is_current_page = False
        # load imgs
        self.profile_icon, self.income_icon, self.savings_icon, self.expense_icon, self.investment_icon = self.loadIcons()
        # calculate summaries
        finance = self.tm.calculateOverallFinance(self.app.user_id)
        balance = self.tm.calculateOverallBalance(finance)
        # create page sections
        self.header_section = ProfileHeader(img=self.profile_icon, uname=f"User {self.app.user_id}", 
                                            summary_type="Total Balance:", amount=balance,
                                            master=self, fg_color=BaseStyles.BLUE, corner_radius=BaseStyles.RAD_2)
        self.summary_section = ctk.CTkFrame(self, fg_color=BaseStyles.WHITE, corner_radius=BaseStyles.RAD_2)
        # create summary frames
        self.income_frame = SummarySection(img=self.income_icon, img_bg_color=ProfileStyles.INCOME_IMG_BG_COLOR,
                                           summary_type="Total Income:", amount=finance.total_income,
                                           master=self.summary_section, fg_color=ProfileStyles.INCOME_FRAME_FG_COLOR,
                                           corner_radius=BaseStyles.RAD_2)
        self.expense_frame = SummarySection(img=self.expense_icon, img_bg_color=ProfileStyles.EXPENSE_IMG_BG_COLOR,
                                            summary_type="Total Expenses:", amount=finance.total_expenses,
                                            master=self.summary_section, fg_color=ProfileStyles.EXPENSE_FRAME_FG_COLOR,
                                            corner_radius=BaseStyles.RAD_2)
        self.savings_frame = SummarySection(img=self.savings_icon, img_bg_color=ProfileStyles.SAVINGS_IMG_BG_COLOR,
                                            summary_type="Total Savings:", amount=finance.total_savings,
                                            master=self.summary_section, fg_color=ProfileStyles.SAVINGS_FRAME_FG_COLOR,
                                            corner_radius=BaseStyles.RAD_2)
        self.investment_frame = SummarySection(img=self.investment_icon, img_bg_color=ProfileStyles.INVESTMENT_IMG_BG_COLOR, 
                                               summary_type="Total Investment:", amount=finance.total_investment,
                                               master=self.summary_section, fg_color=ProfileStyles.INVESTMENT_FRAME_FG_COLOR,
                                               corner_radius=BaseStyles.RAD_2)
        # display page sections
        self.header_section.pack(pady=(BaseStyles.PAD_5+BaseStyles.PAD_5,0))
        self.summary_section.pack(pady=(BaseStyles.PAD_2,0))
        # display summary sections
        self.income_frame.grid(row=0, column=0, padx=(BaseStyles.PAD_4,0), pady=(BaseStyles.PAD_4,0), sticky="nsew")
        self.expense_frame.grid(row=0, column=1, padx=BaseStyles.PAD_4, pady=(BaseStyles.PAD_4,0), sticky="nsew")
        self.savings_frame.grid(row=1, column=0, padx=(BaseStyles.PAD_4,0), pady=BaseStyles.PAD_4, sticky="nsew")
        self.investment_frame.grid(row=1, column=1, pady=BaseStyles.PAD_4, padx=BaseStyles.PAD_4, sticky="nsew")

    def loadIcons(self):
        # icon path
        ICONS_FOLDER = os.path.abspath("assets/icons")
        # load images
        profile_icon = ctk.CTkImage(Image.open(f"{ICONS_FOLDER}/profile1.png"), size=(ProfileStyles.PROFILE_IMG_H, ProfileStyles.PROFILE_IMG_W))
        income_icon = ctk.CTkImage(Image.open(f"{ICONS_FOLDER}/income.png"), size=(ProfileStyles.SUMMARY_IMG_H, ProfileStyles.SUMMARY_IMG_W))
        savings_icon = ctk.CTkImage(Image.open(f"{ICONS_FOLDER}/savings.png"), size=(ProfileStyles.SUMMARY_IMG_H, ProfileStyles.SUMMARY_IMG_W))
        expense_icon = ctk.CTkImage(Image.open(f"{ICONS_FOLDER}/expense.png"), size=(ProfileStyles.SUMMARY_IMG_H, ProfileStyles.SUMMARY_IMG_W))
        investment_icon = ctk.CTkImage(Image.open(f"{ICONS_FOLDER}/investment.png"), size=(ProfileStyles.SUMMARY_IMG_H, ProfileStyles.SUMMARY_IMG_W))
        return profile_icon, income_icon, savings_icon, expense_icon, investment_icon
    
    def updatePageDisplay(self):
        finance = self.tm.calculateOverallFinance(self.app.user_id)
        balance = self.tm.calculateOverallBalance(finance)
        self.header_section.amount_label.configure(text=f"₱ {balance:,}")
        self.income_frame.amount_label.configure(text=f"₱ {finance.total_income:,}")
        self.expense_frame.amount_label.configure(text=f"₱ {finance.total_expenses:,}")
        self.savings_frame.amount_label.configure(text=f"₱ {finance.total_savings:,}")
        self.investment_frame.amount_label.configure(text=f"₱ {finance.total_investment:,}")