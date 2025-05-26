# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from frontend.utilities.styles import * # contains paddings, dimensions, colors, etc


class TableFilter(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_1, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_4, slant="italic", weight="normal")
        self.font3 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_6, slant="italic", weight="normal")
        # create options
        self.t_type = ["All Types", "Income", "Expenses", "Savings", "Investment"]
        self.categories_by_type = {
            "Income": ["All Categories", "Salary", "Bonus", "Side-hustles", "Tips"],
            "Expenses": ["All Categories", "Bills", "Education", "Entertainment", "Food & Drinks",
                        "Grocery", "Healthcare", "House", "Shopping",
                        "Transportation", "Wellness", "Other"],
            "Savings": ["All Categories", "Monthly Allowance", "Change", "Miscellaneous"],
            "Investment": ["All Categories", "Stocks", "Crypto", "Bonds", "Real Estate"]
        }
        self.all_categories = (self.categories_by_type["Income"]
                               + self.categories_by_type["Expenses"][1:]
                               + self.categories_by_type["Savings"][1:]
                               + self.categories_by_type["Investment"][1:])
        self.current_categories = self.all_categories
        # create menus

        self.type_menu = ctk.CTkOptionMenu(self, values=self.t_type, font=self.font1, text_color=DARK_GREY,
                                           fg_color=WHITE, dropdown_font=self.font1,
                                           dropdown_fg_color=WHITE, dropdown_hover_color=BLUE,
                                           dropdown_text_color=DARK_GREY, button_color=WHITE,
                                           button_hover_color=LIGHT_GREY, corner_radius=RAD_2,
                                           width=220, height=40, command=self.updateCurrentCategoriesAndTable)
        self.category_menu = ctk.CTkOptionMenu(self, values=self.current_categories, font=self.font1, text_color=DARK_GREY,
                                           fg_color=WHITE, dropdown_font=self.font1,
                                           dropdown_fg_color=WHITE, dropdown_hover_color=BLUE,
                                           dropdown_text_color=DARK_GREY, button_color=WHITE,
                                           button_hover_color=LIGHT_GREY, corner_radius=RAD_2,
                                           width=220, height=40, command=None)
        # display menus 
        self.type_menu.grid(row=0, column=0, padx=(0,PAD_1))
        self.category_menu.grid(row=0, column=1)
        
    def updateCurrentCategoriesAndTable(self, t_type):
        if t_type == "All Types":
            self.current_categories = self.all_categories
        else:
            self.current_categories = self.categories_by_type[t_type]
        self.category_menu.configure(values=self.current_categories)
        self.category_menu.set(self.current_categories[0])


# header section
class HistoryHeader(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_6, slant="italic", weight="normal")

        self.tile_label = ctk.CTkLabel(self, text="Transaction History", font=self.font1, text_color=WHITE,
                                       anchor="w", fg_color=GREEN, width=HEADER_LABEL_W, height=HEADER_LABEL_H)
        self.filter = TableFilter(self)


        self.tile_label.grid(row=0, column=0, padx=PAD_4, pady=PAD_1)
        self.filter.grid(row=0, column=1, padx=(0, PAD_3), pady=(0,PAD_3), sticky="s")


class TableRow(ctk.CTkFrame):
    def __init__(self, transaction, master, **kwargs):
        super().__init__(master, **kwargs)
        self.t = transaction
        # initialize font
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_3, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_4, slant="italic", weight="normal")
        
        self.date_label = ctk.CTkLabel(self, text=self.t.t_date, font=self.font1,
                                       text_color=DARK_GREY, fg_color="yellow", anchor="w",
                                       width=TABLE_COL_W1, wraplength=TABLE_COL_W1)
        self.type_label = ctk.CTkLabel(self, text=self.t.t_type, font=self.font1,
                                       text_color=DARK_GREY, fg_color="green", anchor="w",
                                       width=TABLE_COL_W2, wraplength=TABLE_COL_W2)
        self.category_label = ctk.CTkLabel(self, text=self.t.t_category, font=self.font1,
                                           text_color=DARK_GREY, fg_color="orange", anchor="w",
                                           width=TABLE_COL_W2, wraplength=TABLE_COL_W2)
        self.description_label = ctk.CTkLabel(self, text=self.t.t_description, font=self.font1,
                                              text_color=DARK_GREY, fg_color="red", anchor="w",
                                              width=TABLE_COL_W3, wraplength=TABLE_COL_W3)
        self.amount_label = ctk.CTkLabel(self, text=f"₱ {self.t.t_amount:,}", font=self.font1,
                                         text_color=DARK_GREY, fg_color="indigo", anchor="e",
                                         width=TABLE_COL_W3, wraplength=TABLE_COL_W3)
        

class Table(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize font
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_3, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_4, slant="italic", weight="normal")
        # table sections
        self.table_header = ctk.CTkFrame(self, fg_color=WHITE, corner_radius=RAD_2)
        self.table_body = ctk.CTkScrollableFrame(self, fg_color=WHITE, orientation="vertical", corner_radius=RAD_2,
                                                 height=TABLE_H, width=TABLE_W)
        # table header content
        self.date_header = ctk.CTkLabel(self.table_header, text="Date", font=self.font1,
                                       text_color=DARK_GREY, fg_color="yellow", anchor="w",
                                       width=TABLE_COL_W1, height=40)
        self.type_header = ctk.CTkLabel(self.table_header, text="Type", font=self.font1,
                                       text_color=DARK_GREY, fg_color="blue", anchor="w",
                                       width=TABLE_COL_W2, height=40)
        self.category_header = ctk.CTkLabel(self.table_header, text="Category", font=self.font1,
                                       text_color=DARK_GREY, fg_color="orange", anchor="w",
                                       width=TABLE_COL_W2, height=40)
        self.description_header = ctk.CTkLabel(self.table_header, text="Description", font=self.font1,
                                       text_color=DARK_GREY, fg_color="red", anchor="w",
                                       width=TABLE_COL_W3, height=40)
        self.amount_header = ctk.CTkLabel(self.table_header, text="Amount", font=self.font1,
                                       text_color=DARK_GREY, fg_color="indigo", anchor="e",
                                       width=TABLE_COL_W3, height=40)
        # table body content
        self.all_transactions = self.tm.repo.getAllTransactions(self.user_id)
        self.all_transactions_by_type = {
            "income": self.tm.repo.getTransactionsByType(self.user_id, "income"),
            "savings": self.tm.repo.getTransactionsByType(self.user_id, "savings"),
            "expense": self.tm.repo.getTransactionsByType(self.user_id, "expense"),
            "investment": self.tm.repo.getTransactionsByType(self.user_id, "investment")
        }
        self.all_rows = [TableRow(transaction=t, master=self.table_body) for t in self.all_transactions]
        self.all_rows_by_type = {}
        for t_type, transactions in self.all_transactions_by_type.items():
            self.all_rows_by_type[t_type] = [TableRow(transaction=t, master=self.table_body) for t in transactions]

        # display table sections
        self.table_header.pack(pady=(0,PAD_1))
        self.table_body.pack()
        # display table header
        self.date_header.grid(row=0, column=0, padx=(PAD_2,PAD_2), pady=PAD_1)
        self.type_header.grid(row=0, column=1, padx=(0,PAD_2), pady=PAD_1)
        self.category_header.grid(row=0, column=2, padx=(0,PAD_2), pady=PAD_1)
        self.description_header.grid(row=0, column=3, padx=(0,PAD_2), pady=PAD_1)
        self.amount_header.grid(row=0, column=4, padx=(0,PAD_2), pady=PAD_1)
        # display table body
        for row in self.all_rows:
            row.pack(pady=(0,PAD_1))
            row.date_label.grid(row=0, column=0, padx=(0,PAD_2), pady=0)
            row.type_label.grid(row=0, column=1, padx=(0,PAD_2), pady=0)
            row.category_label.grid(row=0, column=2, padx=(0,PAD_2), pady=0)
            row.description_label.grid(row=0, column=3, padx=(0,PAD_2), pady=0)
            row.amount_label.grid(row=0, column=4, padx=(0,PAD_2), pady=0)


    def filterRowsByType(self, t_type):
        # hide previous rows
        for row in self.all_rows:
            row.pack_ignore()
        for rows in self.all_rows_by_type.keys():
            for row in rows:
                row.pack_ignore()
        # show selected rows
        if t_type == "All Types":
            for row in self.all_rows:
                row.pack()
        else:
            for row in self.all_rows_by_type[t_type]:
                row.pack()
        




class History(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize state
        self.isCurrentPage = False
        # create page sections
        self.header_section = HistoryHeader(master=self, fg_color=BLUE, corner_radius=RAD_2,
                                            height=HEADER_H, width=HEADER_W)
        self.table = Table(user_id=self.user_id, tm=self.tm, master=self, fg_color=RED, corner_radius=0)
        # display page sections
        self.header_section.pack(fill="y", expand=True, pady=(PAD_5+PAD_5,0))
        self.table.pack(padx=PAD_3, pady=(PAD_4,0))