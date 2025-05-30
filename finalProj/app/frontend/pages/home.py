# external/built-in modules/libs
import customtkinter as ctk
from PIL import Image
import os
# our modules/libs
from frontend.styles import Styles as s # paddings, dimensions, colors, etc


class HomeHeader(ctk.CTkFrame):
    def __init__(self, img, summary_type, amount, master, **kwargs):
        super().__init__(master, ** kwargs)
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=s.FONT_SIZE_4, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=s.FONT_SIZE_6, slant="italic", weight="normal")
        self.img = img
        # create guide frames
        self.balance_frame = ctk.CTkFrame(self, fg_color="red", corner_radius=0)
        self.img_bg = ctk.CTkLabel(self, corner_radius=0, image=img, text="",
                                   width=s.HOME_IMG_BG_W, height=s.HOME_IMG_BG_H, fg_color="yellow")
        # create label
        self.summary_type_label = ctk.CTkLabel(self.balance_frame, text=summary_type, font=self.font1,
                                               text_color=s.WHITE, anchor="w", fg_color="green")
        self.amount_label = ctk.CTkLabel(self.balance_frame, text=f"₱ {amount:,}", font=self.font2,
                                         text_color=s.WHITE, width=s.HOME_LABEL_W, anchor="w", justify="left", fg_color="orange")
        # display guide frames
        self.balance_frame.grid(row=0, column=0, padx=(s.PAD_4,0))
        self.img_bg.grid(row=0, column=1, pady=s.PAD_3, padx=s.PAD_3, sticky="e")
        # display labels
        self.summary_type_label.pack(anchor="w")
        self.amount_label.pack(anchor="w")


class TableRow(ctk.CTkFrame):
    def __init__(self, transaction, master, **kwargs):
        super().__init__(master, **kwargs)
        self.t = transaction
        # initialize font
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=s.FONT_SIZE_2, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=s.FONT_SIZE_4, slant="italic", weight="normal")
        
        self.date_label = ctk.CTkLabel(self, text=self.t.t_date, font=self.font1,
                                       text_color=s.DARK_GREY, fg_color=s.WHITE, anchor="w",
                                       width=s.HOME_TABLE_COL_W1, wraplength=s.HOME_TABLE_COL_W1, justify="left")
        self.type_label = ctk.CTkLabel(self, text=self.t.t_type, font=self.font1,
                                       text_color=s.DARK_GREY, fg_color=s.WHITE, anchor="w",
                                       width=s.HOME_TABLE_COL_W2, wraplength=s.HOME_TABLE_COL_W2, justify="left")
        self.category_label = ctk.CTkLabel(self, text=self.t.t_category, font=self.font1,
                                           text_color=s.DARK_GREY, fg_color=s.WHITE, anchor="w",
                                           width=s.HOME_TABLE_COL_W2, wraplength=s.HOME_TABLE_COL_W2, justify="left")
        self.description_label = ctk.CTkLabel(self, text=self.t.t_description, font=self.font1,
                                              text_color=s.DARK_GREY, fg_color=s.WHITE, anchor="w",
                                              width=s.HOME_TABLE_COL_W3, wraplength=s.HOME_TABLE_COL_W3, justify="left")
        self.amount_label = ctk.CTkLabel(self, text=f"₱ {self.t.t_amount:,}", font=self.font1,
                                         text_color=s.DARK_GREY, fg_color=s.WHITE, anchor="e",
                                         width=s.HOME_TABLE_COL_W3, wraplength=s.HOME_TABLE_COL_W3, justify="right")
        

class Table(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize font
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=s.FONT_SIZE_3, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=s.FONT_SIZE_4, slant="italic", weight="normal")
        # table sections
        self.table_header = ctk.CTkFrame(self, fg_color=s.WHITE, corner_radius=s.RAD_2)
        self.table_body = ctk.CTkScrollableFrame(self, fg_color=s.WHITE, orientation="vertical",
                                                 corner_radius=s.RAD_2, height=s.HOME_TABLE_BODY_H, width=s.HOME_TABLE_BODY_W)
        # table header
        self.date_header = ctk.CTkLabel(self.table_header, text="Date", font=self.font1,
                                       text_color=s.DARK_GREY, fg_color="transparent", anchor="w",
                                       width=s.HOME_TABLE_COL_W1, height=s.HOME_TABLE_ROW_H)
        self.type_header = ctk.CTkLabel(self.table_header, text="Type", font=self.font1,
                                       text_color=s.DARK_GREY, fg_color="transparent", anchor="w",
                                       width=s.HOME_TABLE_COL_W2, height=s.HOME_TABLE_ROW_H)
        self.category_header = ctk.CTkLabel(self.table_header, text="Category", font=self.font1,
                                       text_color=s.DARK_GREY, fg_color="transparent", anchor="w",
                                       width=s.HOME_TABLE_COL_W2, height=s.HOME_TABLE_ROW_H)
        self.description_header = ctk.CTkLabel(self.table_header, text="Description", font=self.font1,
                                       text_color=s.DARK_GREY, fg_color="transparent", anchor="w",
                                       width=s.HOME_TABLE_COL_W3, height=s.HOME_TABLE_ROW_H)
        self.amount_header = ctk.CTkLabel(self.table_header, text="Amount", font=self.font1,
                                       text_color=s.DARK_GREY, fg_color="transparent", anchor="e",
                                       width=s.HOME_TABLE_COL_W3, height=s.HOME_TABLE_ROW_H)
        # initialize table content
        self.recent_rows = self.loadRecentRows()
        # display table sections
        self.table_header.pack(pady=(0,s.PAD_1))
        self.table_body.pack()
        # display table header
        self.date_header.grid(row=0, column=0, padx=(s.PAD_2,s.PAD_2), pady=s.PAD_1)
        self.type_header.grid(row=0, column=1, padx=(0,s.PAD_2), pady=s.PAD_1)
        self.category_header.grid(row=0, column=2, padx=(0,s.PAD_2), pady=s.PAD_1)
        self.description_header.grid(row=0, column=3, padx=(0,s.PAD_2), pady=s.PAD_1)
        self.amount_header.grid(row=0, column=4, padx=(0,s.PAD_2), pady=s.PAD_1)
        # display table content
        self.showRows()

    def _convertTransactionsToRows(self, transactions):
        rows = []
        for t in transactions:
            row = TableRow(transaction=t, master=self.table_body, fg_color=s.WHITE)
            rows.append(row)
        return rows
    
    def loadRecentRows(self):
        # retrieve 5 recent transactions
        # recent_transactions = self.tm.repo.getRecentTransactions(user_id=self.user_id, t_count=5)
        recent_transactions = []
        # convert transactions to rows
        recent_rows = self._convertTransactionsToRows(transactions=recent_transactions)
        return recent_rows

    def showRows(self):
        # show rows
        for row in self.recent_rows:
            row.pack(pady=(0,s.PAD_1))
            row.date_label.grid(row=0, column=0, padx=(0,s.PAD_2), pady=0, sticky="n")
            row.type_label.grid(row=0, column=1, padx=(0,s.PAD_2), pady=0, sticky="n")
            row.category_label.grid(row=0, column=2, padx=(0,s.PAD_2), pady=0, sticky="n")
            row.description_label.grid(row=0, column=3, padx=(0,s.PAD_2), pady=0, sticky="n")
            row.amount_label.grid(row=0, column=4, padx=(0,s.PAD_2), pady=0, sticky="n")


class Home(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize state
        self.isCurrentPage = False
        # load imgs
        home_icon = self.loadIcons()
        # calculate balance 
        finance = self.tm.calculateOverallFinance(self.user_id)
        balance = self.tm.calculateOverallBalance(finance)
        self.header_section = HomeHeader(img=home_icon, summary_type="Total Balance:", amount=balance,
                                         master=self, fg_color=s.BLUE, corner_radius=s.RAD_2)
        self.table_section = Table(user_id=self.user_id, tm=self.tm, master=self, fg_color=s.SKY_BLUE, corner_radius=0)
        # display sections
        self.header_section.pack(pady=(s.PAD_5+s.PAD_5,0))
        self.table_section.pack(pady=(s.PAD_2,0))

    def loadIcons(self):
        # icon path
        ICONS_FOLDER = os.path.abspath("assets/icons")
        # load images
        home_icon = ctk.CTkImage(Image.open(f"{ICONS_FOLDER}/home1.png"), size=(s.HOME_IMG_H, s.HOME_IMG_W))
        return home_icon
