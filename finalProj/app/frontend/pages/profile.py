# external/built-in modules/libs
import customtkinter as ctk
from PIL import Image
from pathlib import Path
# our modules/libs
from frontend.utilities.styles import * # contains paddings, dimensions, colors, etc


class ProfileHeader(ctk.CTkFrame):
    def __init__(self, img, uname, summary_type, amount, master, **kwargs):
        super().__init__(master, ** kwargs)
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_3, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_5, slant="italic", weight="normal")
        self.img = img
        # create guide frames
        self.img_bg = ctk.CTkLabel(self, corner_radius=RAD_2, fg_color="transparent", image=img,
                                   text="", width=PROFILE_IMG_BG_W, height=PROFILE_IMG_BG_H)
        self.uname_frame = ctk.CTkFrame(self, corner_radius=RAD_2, fg_color="transparent", width=SUMMARY_IMG_FRAME_W)
        self.balance_frame = ctk.CTkFrame(self, corner_radius=RAD_2, fg_color="transparent", width=SUMMARY_IMG_FRAME_W)
        # create label
        self.uname_label = ctk.CTkLabel(self.uname_frame, text=uname, font=self.font2, text_color=WHITE,
                                        anchor="w", width=PROFILE_LABEL_W1)
        self.summary_type_label = ctk.CTkLabel(self.balance_frame, text=summary_type, font=self.font1,
                                               text_color=WHITE, anchor="e")
        self.amount_label = ctk.CTkLabel(self.balance_frame, text=f"₱ {amount:,}", font=self.font2,
                                         text_color=WHITE, width=PROFILE_LABEL_W2, anchor="e")
        # display guide frames
        self.img_bg.grid(row=0, column=0, pady=PAD_2, padx=PAD_2)
        self.uname_frame.grid(row=0, column=1, padx=(0,PAD_2))
        self.balance_frame.grid(row=0, column=2, padx=(0,PAD_4))
        # display labels
        self.uname_label.pack(anchor="w")
        self.summary_type_label.pack(anchor="e")
        self.amount_label.pack(anchor="e")



class SummarySection(ctk.CTkFrame):
    def __init__(self, img, img_bg_color, summary_type, amount, master, **kwargs):
        super().__init__(master, ** kwargs)
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_3, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_5, slant="italic", weight="normal")
        self.img = img
        # create guide frames
        self.img_bg = ctk.CTkLabel(self, height=SUMMARY_IMG_FRAME_H, width=SUMMARY_IMG_FRAME_W,
                                   corner_radius=RAD_2, fg_color=img_bg_color, image=img, text="")
        self.details_frame = ctk.CTkFrame(self, width=SUMMARY_IMG_FRAME_W, corner_radius=RAD_2, fg_color="transparent")
        # create labels
        self.summary_type_label = ctk.CTkLabel(self.details_frame, text=summary_type, font=self.font1, text_color=DARK_GREY, anchor="w")
        self.amount_label = ctk.CTkLabel(self.details_frame, text=f"₱ {amount:,}", font=self.font2, text_color=DARK_GREY,
                                         width=SUMMARY_LABEL_W, anchor="w")
        # display guide frames
        self.img_bg.grid(row=0, column=0, padx=(PAD_5, 0), pady=PAD_5)
        self.details_frame.grid(row=0, column=1, padx=(PAD_3, PAD_5), pady=PAD_1)
        # display labels
        self.summary_type_label.pack(anchor="w")
        self.amount_label.pack(anchor="w")


class Profile(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, ** kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize state
        self.isCurrentPage = False
        # load imgs
        profile_icon, income_icon, savings_icon, expense_icon, investment_icon = self.loadIcons()
        # create page sections
        self.header_section = ProfileHeader(img=profile_icon, uname=f"User {self.user_id}", 
                                            summary_type="Total Balance:", amount=0.0, master=self,
                                            fg_color=BLUE, corner_radius=RAD_2, height=HEADER_H,
                                            width=HEADER_W)
        self.summary_section = ctk.CTkFrame(self, fg_color=WHITE, corner_radius=RAD_2)
        # create summary sub-sections
        finance = self.tm.calculateOverallFinance(self.user_id)
        self.income = SummarySection(img=income_icon, summary_type="Total Income:",
                                     amount=finance.total_income, master=self.summary_section,
                                     fg_color=WHITE_BLUE, corner_radius=RAD_2, height=SUMMARY_ELEM_H,
                                     width=SUMMARY_ELEM_W, img_bg_color=LIGHT_BLUE)
        self.expense = SummarySection(img=expense_icon, summary_type="Total Expenses:",
                                      amount=finance.total_expenses, master=self.summary_section,
                                      fg_color=WHITE_RED, corner_radius=RAD_2, height=SUMMARY_ELEM_H,
                                      width=SUMMARY_ELEM_W, img_bg_color=LIGHT_RED)
        self.savings = SummarySection(img=savings_icon, summary_type="Total Savings:",
                                      amount=finance.total_savings, master=self.summary_section,
                                      fg_color=WHITE_GREEN, corner_radius=RAD_2, height=SUMMARY_ELEM_H,
                                      width=SUMMARY_ELEM_W, img_bg_color=LIGHT_GREEN)
        self.investment = SummarySection(img=investment_icon, summary_type="Total Investment:",
                                         amount=finance.total_investment, master=self.summary_section,
                                         fg_color=WHITE_PURPLE, corner_radius=RAD_2, height=SUMMARY_ELEM_H,
                                         width=SUMMARY_ELEM_W, img_bg_color=LIGHT_PURPLE)
        # display page sections
        self.header_section.pack(padx=PAD_5+PAD_5, pady=(PAD_5+PAD_5,0))
        self.summary_section.pack(padx=PAD_5, pady=(PAD_4, PAD_5+PAD_5))
        # display summary sections
        self.income.grid(row=0, column=0, padx=(PAD_4,0), pady=(PAD_4,0), sticky="nsew")
        self.expense.grid(row=0, column=1, padx=PAD_4, pady=(PAD_4,0), sticky="nsew")
        self.savings.grid(row=1, column=0, padx=(PAD_4,0), pady=PAD_4, sticky="nsew")
        self.investment.grid(row=1, column=1, pady=PAD_4, padx=PAD_4, sticky="nsew")

    def loadIcons(self):
        # icon path
        ICONS_FOLDER = Path(__file__).resolve().parent.parent.parent / "assets" / "icons"
        # load images
        profile_icon = ctk.CTkImage(Image.open(f"{ICONS_FOLDER}/profile1.png"), size=(PROFILE_IMG_H, PROFILE_IMG_W))
        income_icon = ctk.CTkImage(Image.open(f"{ICONS_FOLDER}/income.png"), size=(SUMMARY_IMG_H, SUMMARY_IMG_W))
        savings_icon = ctk.CTkImage(Image.open(f"{ICONS_FOLDER}/savings.png"), size=(SUMMARY_IMG_H, SUMMARY_IMG_W))
        expense_icon = ctk.CTkImage(Image.open(f"{ICONS_FOLDER}/expense.png"), size=(SUMMARY_IMG_H, SUMMARY_IMG_W))
        investment_icon = ctk.CTkImage(Image.open(f"{ICONS_FOLDER}/investment.png"), size=(SUMMARY_IMG_H, SUMMARY_IMG_W))
        return profile_icon, income_icon, savings_icon, expense_icon, investment_icon
    
    def updatePageDisplay(self):
        finance = self.tm.calculateOverallFinance(self.user_id)
        self.income.amount_label.configure(text=f"₱ {finance.total_income:,}")
        self.expense.amount_label.configure(text=f"₱ {finance.total_expenses:,}")
        self.savings.amount_label.configure(text=f"₱ {finance.total_savings:,}")
        self.investment.amount_label.configure(text=f"₱ {finance.total_investment:,}")