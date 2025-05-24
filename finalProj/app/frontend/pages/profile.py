import customtkinter as ctk
from PIL import Image


ICONS_FOLDER = "./assets/icons"

# create global screen dimension
temp_root = ctk.CTk()
SCREEN_W = temp_root.winfo_screenwidth()
temp_root.destroy()
SCREEN_H = int(0.5625*SCREEN_W)
print(SCREEN_W, SCREEN_H)

FONT_SIZE_1 = int(0.0231*SCREEN_H) #25
FONT_SIZE_2 = int(0.0278*SCREEN_H) #30
FONT_SIZE_3 = int(0.0370*SCREEN_H) #40
FONT_SIZE_4 = int(0.0463*SCREEN_H) #50
FONT_SIZE_5 = int(0.0556*SCREEN_H) #60

WHITE= "white"

WHITE_RED = "#fdecec"
LIGHT_RED = "#ffc7c7"
RED = "#e14242"

WHITE_GREEN = "#dafbf0"
LIGHT_GREEN = "#b2fee3"
GREEN = "#28ab58"

WHITE_PURPLE = "#f3eefe"
LIGHT_PURPLE =  "#d6c5fb"
PURPLE = "#ceb9fe"

WHITE_BLUE = "#ebf2fe"
SKY_BLUE = "#cef2ff"
LIGHT_BLUE = "#bcd4fe"
BLUE = "#559eef"
DARK_BLUE = "#427cbd"

LIGHT_GREY = "#c4c4c4"
GREY = "grey"
DARK_GREY = "#545454"

ENTRY_W1 = int(1.3241*SCREEN_H) #1430
ENTRY_W2 = int(0.5556*SCREEN_H) #600
ENTRY_H = int(0.0556*SCREEN_H) #60

MENU_W1 = int(0.7407*SCREEN_H) #800
MENU_W2 = int(1.2593*SCREEN_H) #1360 
MENU_H = int(0.0556*SCREEN_H) #60

YEAR_MENU_W = int(0.4167*SCREEN_H) #450
MONTH_MENU_W = int(0.4630*SCREEN_H) #500 
DAY_MENU_W = int(0.4167*SCREEN_H) #450

PAD_X1 = int(0.0093*SCREEN_H) #10
PAD_X2 = int(0.0185*SCREEN_H) #20
PAD_X3 = int(0.0278*SCREEN_H) #30
PAD_X4 = int(0.0370*SCREEN_H) #40
PAD_X5 = int(0.0463*SCREEN_H) #50

PAD_Y1 = int(0.0093*SCREEN_H) #10
PAD_Y2 = int(0.0185*SCREEN_H) #20
PAD_Y3 = int(0.0278*SCREEN_H) #30
PAD_Y4 = int(0.0370*SCREEN_H) #40
PAD_Y5 = int(0.0463*SCREEN_H) #50

BTN_W1 = int(0.0648*SCREEN_H) #70
BTN_W2 = int(0.3241*SCREEN_H) #350

BTN_H1 = int(0.0648*SCREEN_H) #70
BTN_H2 = int(0.0556*SCREEN_H) #60

RAD = int(0.0185*SCREEN_H) #20

# ---- exclusive ----
HEADER_H = int(0.2593*SCREEN_H) #280
HEADER_W = int(1.5093*SCREEN_H) #1630

PROFILE_IMG_W = int(0.1852*SCREEN_H) #200
PROFILE_IMG_H = int(0.1852*SCREEN_H) #200

PROFILE_IMG_BG_W = int(0.2222*SCREEN_H) #240
PROFILE_IMG_BG_H = int(0.2222*SCREEN_H) #240

PROFILE_LABEL_W1 = int(0.4630*SCREEN_H) #500
PROFILE_LABEL_W2 = int(0.7222*SCREEN_H) #780

# SUMMARY_H = 560
# SUMMARY_W = 1630
SUMMARY_ELEM_H = int(0.2037*SCREEN_H) #220
SUMMARY_ELEM_W = int(0.6991*SCREEN_H) #755

SUMMARY_IMG_W = int(0.0463*SCREEN_H) #50
SUMMARY_IMG_H = int(0.0463*SCREEN_H) #50

SUMMARY_IMG_FRAME_W = int(0.1111*SCREEN_H) #120
SUMMARY_IMG_FRAME_H = int(0.1111*SCREEN_H) #120

SUMMARY_LABEL_W = int(0.4630*SCREEN_H) #500


class ProfileHeader(ctk.CTkFrame):
    def __init__(self, img, uname, summary_type, amount, master, **kwargs):
        super().__init__(master, ** kwargs)
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_3, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_5, slant="italic", weight="normal")
        self.img = img
        # create guide frames
        self.img_bg = ctk.CTkLabel(self, corner_radius=RAD, fg_color="transparent", image=img,
                                   text="", width=PROFILE_IMG_BG_W, height=PROFILE_IMG_BG_H)
        self.uname_frame = ctk.CTkFrame(self, corner_radius=RAD, fg_color="transparent", width=SUMMARY_IMG_FRAME_W)
        self.balance_frame = ctk.CTkFrame(self, corner_radius=RAD, fg_color="transparent", width=SUMMARY_IMG_FRAME_W)
        # create label
        self.uname_label = ctk.CTkLabel(self.uname_frame, text=uname, font=self.font2, text_color=WHITE,
                                        anchor="w", width=PROFILE_LABEL_W1)
        self.summary_type_label = ctk.CTkLabel(self.balance_frame, text=summary_type, font=self.font1,
                                               text_color=WHITE, anchor="e")
        self.amount_label = ctk.CTkLabel(self.balance_frame, text=f"₱ {amount:,}", font=self.font2,
                                         text_color=WHITE, width=PROFILE_LABEL_W2, anchor="e")
        # display guide frames
        self.img_bg.grid(row=0, column=0, pady=PAD_X2, padx=PAD_Y2)
        self.uname_frame.grid(row=0, column=1, padx=(0,PAD_X2))
        self.balance_frame.grid(row=0, column=2, padx=(0,PAD_X4))
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
                                   corner_radius=RAD, fg_color=img_bg_color, image=img, text="")
        self.details_frame = ctk.CTkFrame(self, width=SUMMARY_IMG_FRAME_W, corner_radius=RAD, fg_color="transparent")
        # create labels
        self.summary_type_label = ctk.CTkLabel(self.details_frame, text=summary_type, font=self.font1, text_color=DARK_GREY, anchor="w")
        self.amount_label = ctk.CTkLabel(self.details_frame, text=f"₱ {amount:,}", font=self.font2, text_color=DARK_GREY,
                                         width=SUMMARY_LABEL_W, anchor="w")
        # display guide frames
        self.img_bg.grid(row=0, column=0, padx=(PAD_X5, 0), pady=PAD_Y5)
        self.details_frame.grid(row=0, column=1, padx=(PAD_X3, PAD_X5), pady=PAD_Y1)
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
        self.header_section = ProfileHeader(img=profile_icon, uname=f"User {self.user_id}", master=self,
                                            fg_color=BLUE, summary_type="Total Balance:", amount=0.0,
                                            corner_radius=RAD, height=HEADER_H, width=HEADER_W)
        self.summary_section = ctk.CTkFrame(self, fg_color=WHITE, corner_radius=RAD)
        # create summary sub-sections
        finance = self.tm.calculateOverallFinance(self.user_id)
        self.income = SummarySection(img=income_icon, master=self.summary_section, fg_color=WHITE_BLUE,
                                     summary_type="Total Income:", amount=finance.total_income,
                                     corner_radius=RAD, height=SUMMARY_ELEM_H,
                                     width=SUMMARY_ELEM_W, img_bg_color=LIGHT_BLUE)
        self.expense = SummarySection(img=expense_icon, master=self.summary_section, fg_color=WHITE_RED,
                                     summary_type="Total Expenses:", amount=finance.total_expenses,
                                     corner_radius=RAD, height=SUMMARY_ELEM_H,
                                     width=SUMMARY_ELEM_W, img_bg_color=LIGHT_RED)
        self.savings = SummarySection(img=savings_icon, master=self.summary_section, fg_color=WHITE_GREEN,
                                     summary_type="Total Savings:", amount=finance.total_savings,
                                     corner_radius=RAD, height=SUMMARY_ELEM_H,
                                     width=SUMMARY_ELEM_W, img_bg_color=LIGHT_GREEN)
        self.investment = SummarySection(img=investment_icon, master=self.summary_section, fg_color=WHITE_PURPLE,
                                     summary_type="Total Investment:", amount=finance.total_investment,
                                     corner_radius=RAD, height=SUMMARY_ELEM_H,
                                     width=SUMMARY_ELEM_W, img_bg_color=LIGHT_PURPLE)
        # display page sections
        self.header_section.pack(padx=PAD_X5+PAD_X5, pady=(PAD_Y5+PAD_Y5,0))
        self.summary_section.pack(padx=PAD_X5, pady=(PAD_Y4, PAD_Y5+PAD_Y5))
        # display summary sections
        self.income.grid(row=0, column=0, padx=(PAD_X4,0), pady=(PAD_Y4,0), sticky="nsew")
        self.expense.grid(row=0, column=1, padx=PAD_X4, pady=(PAD_Y4,0), sticky="nsew")
        self.savings.grid(row=1, column=0, padx=(PAD_Y4,0), pady=PAD_Y4, sticky="nsew")
        self.investment.grid(row=1, column=1, pady=PAD_Y4, padx=PAD_X4, sticky="nsew")

    def loadIcons(self):
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