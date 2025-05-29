# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from frontend.styles import Styles as s # paddings, dimensions, colors, etc


class HistoryHeader(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=s.FONT_SIZE_6, slant="italic", weight="normal")

        self.tile_label = ctk.CTkLabel(self, text="Transaction History", font=self.font1, text_color=s.WHITE,
                                       anchor="w", fg_color=s.BLUE, width=s.HISTORY_HEADER_LABEL_W, height=s.HISTORY_HEADER_LABEL_H)

        self.tile_label.grid(row=0, column=0, padx=s.PAD_4, pady=s.PAD_1)


class TableFilters(ctk.CTkFrame):
    def __init__(self, table, master, **kwargs):
        super().__init__(master, **kwargs)
        self.table = table
        # initialize fonts
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=s.FONT_SIZE_1, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=s.FONT_SIZE_4, slant="italic", weight="normal")
        self.font3 = ctk.CTkFont(family="Bodoni MT", size=s.FONT_SIZE_6, slant="italic", weight="normal")
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
        self.all_categories = ["All Categories"] + [c for categories in self.categories_by_type.values() for c in categories[1:]]
        self.current_categories = self.all_categories
        # create menus
        self.type_menu = ctk.CTkOptionMenu(self, values=self.t_type, font=self.font1, text_color=s.DARK_GREY,
                                           fg_color=s.WHITE, dropdown_font=self.font1,
                                           dropdown_fg_color=s.WHITE, dropdown_hover_color=s.BLUE,
                                           dropdown_text_color=s.DARK_GREY, button_color=s.WHITE,
                                           button_hover_color=s.LIGHT_GREY, corner_radius=s.RAD_2,
                                           width=s.TABLE_FILTER_MENU_W, height=s.TABLE_FILTER_MENU_H, command=self.onPickType)
        self.category_menu = ctk.CTkOptionMenu(self, values=self.current_categories, font=self.font1, text_color=s.DARK_GREY,
                                               fg_color=s.WHITE, dropdown_font=self.font1,
                                               dropdown_fg_color=s.WHITE, dropdown_hover_color=s.BLUE,
                                               dropdown_text_color=s.DARK_GREY, button_color=s.WHITE,
                                               button_hover_color=s.LIGHT_GREY, corner_radius=s.RAD_2,
                                               width=s.TABLE_FILTER_MENU_W, height=s.TABLE_FILTER_MENU_H, command=self.onPickCategories)
        # display menus 
        self.type_menu.grid(row=0, column=0, padx=(0,s.PAD_1))
        self.category_menu.grid(row=0, column=1)

    def _filterRows(self, filter_type):
        # set new table body base on type
        self.table.current_rows_per_page = self.table.all_rows_by_filter_per_page[filter_type]
        # reset page num
        self.table.current_page_num = 0
        # display current table page
        self.table.showRowsInCurrentPage()

    def _updateCategoryMenuByType(self, t_type):
        if t_type == "All Types":
            self.current_categories = self.all_categories
        else:
            self.current_categories = self.categories_by_type[t_type]
        self.category_menu.configure(values=self.current_categories)
        self.category_menu.set(self.current_categories[0])
    
    def onPickType(self, t_type):
        self._filterRows(filter_type=t_type)
        self._updateCategoryMenuByType(t_type=t_type)

    def onPickCategories(self, t_categories):
        # self._filterRows(filter_type=t_categories)
        pass


class TableRow(ctk.CTkFrame):
    def __init__(self, transaction, master, **kwargs):
        super().__init__(master, **kwargs)
        self.t = transaction
        # initialize font
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=s.FONT_SIZE_2, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=s.FONT_SIZE_4, slant="italic", weight="normal")
        
        self.date_label = ctk.CTkLabel(self, text=self.t.t_date, font=self.font1,
                                       text_color=s.DARK_GREY, fg_color=s.WHITE, anchor="w",
                                       width=s.TABLE_COL_W1, wraplength=s.TABLE_COL_W1, justify="left")
        self.type_label = ctk.CTkLabel(self, text=self.t.t_type, font=self.font1,
                                       text_color=s.DARK_GREY, fg_color=s.WHITE, anchor="w",
                                       width=s.TABLE_COL_W2, wraplength=s.TABLE_COL_W2, justify="left")
        self.category_label = ctk.CTkLabel(self, text=self.t.t_category, font=self.font1,
                                           text_color=s.DARK_GREY, fg_color=s.WHITE, anchor="w",
                                           width=s.TABLE_COL_W2, wraplength=s.TABLE_COL_W2, justify="left")
        self.description_label = ctk.CTkLabel(self, text=self.t.t_description, font=self.font1,
                                              text_color=s.DARK_GREY, fg_color=s.WHITE, anchor="w",
                                              width=s.TABLE_COL_W3, wraplength=s.TABLE_COL_W3, justify="left")
        self.amount_label = ctk.CTkLabel(self, text=f"₱ {self.t.t_amount:,}", font=self.font1,
                                         text_color=s.DARK_GREY, fg_color=s.WHITE, anchor="e",
                                         width=s.TABLE_COL_W3, wraplength=s.TABLE_COL_W3, justify="right")
        
        
class TableNavigation(ctk.CTkFrame):
    def __init__(self, table, master, **kwargs):
        super().__init__(master, **kwargs)
        self.table = table
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=s.FONT_SIZE_1, slant="italic", weight="normal")
        # create nav btns
        self.prevBTN = ctk.CTkButton(self, text="Prev", text_color=s.WHITE, fg_color=s.BLUE, hover_color=s.DARK_BLUE,
                                     font=self.font1, corner_radius=s.RAD_2, width=s.TABLE_NAV_BTN_W, height=s.TABLE_NAV_BTN_H,
                                     command=self.onClickPrev)
        self.nextBTN = ctk.CTkButton(self, text="Next", text_color=s.WHITE, fg_color=s.BLUE, hover_color=s.DARK_BLUE,
                                     font=self.font1, corner_radius=s.RAD_2, width=s.TABLE_NAV_BTN_W, height=s.TABLE_NAV_BTN_H,
                                     command=self.onClickNext)
        # display nav btns
        self.prevBTN.grid(row=0, column=0, padx=(0,s.PAD_1))
        self.nextBTN.grid(row=0, column=1)

    def onClickPrev(self):
        if self.table.current_page_num > 0:
            self.table.current_page_num -= 1
            # print("table prev")
            self.table.showRowsInCurrentPage()
        
    def onClickNext(self):
        if self.table.current_page_num < len(self.table.current_rows_per_page) - 1:
            self.table.current_page_num += 1
            # print("table next")
            self.table.showRowsInCurrentPage()


class Table(ctk.CTkFrame):
    def __init__(self, user_id, tm, header_section, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize font
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=s.FONT_SIZE_3, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=s.FONT_SIZE_4, slant="italic", weight="normal")
        # table sections
        self.filters = TableFilters(table=self, master=header_section, fg_color=s.BLUE)
        self.table_header = ctk.CTkFrame(self, fg_color=s.WHITE, corner_radius=s.RAD_2)
        self.table_body = ctk.CTkScrollableFrame(self, fg_color=s.WHITE, orientation="vertical",
                                                 corner_radius=s.RAD_2, height=s.TABLE_BODY_H, width=s.TABLE_BODY_W)
        self.table_nav = TableNavigation(table=self, master=self, fg_color=s.SKY_BLUE)
        # table header
        self.date_header = ctk.CTkLabel(self.table_header, text="Date", font=self.font1,
                                       text_color=s.DARK_GREY, fg_color="transparent", anchor="w",
                                       width=s.TABLE_COL_W1, height=s.TABLE_ROW_H)
        self.type_header = ctk.CTkLabel(self.table_header, text="Type", font=self.font1,
                                       text_color=s.DARK_GREY, fg_color="transparent", anchor="w",
                                       width=s.TABLE_COL_W2, height=s.TABLE_ROW_H)
        self.category_header = ctk.CTkLabel(self.table_header, text="Category", font=self.font1,
                                       text_color=s.DARK_GREY, fg_color="transparent", anchor="w",
                                       width=s.TABLE_COL_W2, height=s.TABLE_ROW_H)
        self.description_header = ctk.CTkLabel(self.table_header, text="Description", font=self.font1,
                                       text_color=s.DARK_GREY, fg_color="transparent", anchor="w",
                                       width=s.TABLE_COL_W3, height=s.TABLE_ROW_H)
        self.amount_header = ctk.CTkLabel(self.table_header, text="Amount", font=self.font1,
                                       text_color=s.DARK_GREY, fg_color="transparent", anchor="e",
                                       width=s.TABLE_COL_W3, height=s.TABLE_ROW_H)
        # initialize table body
        self.all_rows_by_filter_per_page = self.loadAllRowsByFilterPerTablePage()
        self.current_rows_per_page = self.all_rows_by_filter_per_page["All Types"]
        self.current_page_num = 0
        # display table sections
        self.filters.grid(row=0, column=1, padx=(0, s.PAD_2), pady=(0,s.PAD_2), sticky="s")
        self.table_header.pack(pady=(0,s.PAD_1))
        self.table_body.pack()
        self.table_nav.pack(pady=(s.PAD_1,0))
        # display table header
        self.date_header.grid(row=0, column=0, padx=(s.PAD_2,s.PAD_2), pady=s.PAD_1)
        self.type_header.grid(row=0, column=1, padx=(0,s.PAD_2), pady=s.PAD_1)
        self.category_header.grid(row=0, column=2, padx=(0,s.PAD_2), pady=s.PAD_1)
        self.description_header.grid(row=0, column=3, padx=(0,s.PAD_2), pady=s.PAD_1)
        self.amount_header.grid(row=0, column=4, padx=(0,s.PAD_2), pady=s.PAD_1)
        # display default table body
        self.showRowsInCurrentPage()

    def _groupTransactionsPerTablePage(self, transactions):
        # get number of pages
        num_of_pages = len(transactions) / 20 # 20 transactions per page
        if num_of_pages.is_integer():
            num_of_pages = int(num_of_pages)
        else:
            num_of_pages = int(num_of_pages) + 1 # plus one page for excess transactions
        # group transactions by page
        transactions_by_page = {}
        for i in range(num_of_pages):
            start = i * 20
            end = start + 20
            transactions_by_page[i] = transactions[start:end]
        return transactions_by_page

    def _convertTransactionsToRowsPerTablePage(self, transactions_per_page):
        rows_per_page = {}
        for transactions in transactions_per_page.values():
            page_frame = ctk.CTkFrame(self.table_body, fg_color=s.WHITE)
            rows = []
            for t in transactions:
                row = TableRow(transaction=t, master=page_frame, fg_color=s.WHITE)
                rows.append(row)
            rows_per_page[page_frame] = rows
        return rows_per_page

    def loadAllRowsByFilterPerTablePage(self):
        # retrieve all transactions from db base on filter
        all_transactions_by_filter = {
            "All Types": self.tm.repo.getAllTransactions(self.user_id),
            "Income": self.tm.repo.getTransactionsByType(self.user_id, "income"),
            "Savings": self.tm.repo.getTransactionsByType(self.user_id, "savings"),
            "Expenses": self.tm.repo.getTransactionsByType(self.user_id, "expense"),
            "Investment": self.tm.repo.getTransactionsByType(self.user_id, "investment"),
            # # income
            # "Salary":self.tm.repo.getTransactionsByCategory(self.user_id, "Salary"),
            # "Bonus":self.tm.repo.getTransactionsByCategory(self.user_id, "Bonus"),
            # "Side-hustles":self.tm.repo.getTransactionsByCategory(self.user_id, "Side-hustles"),
            # "Tips":self.tm.repo.getTransactionsByCategory(self.user_id, "Tips"),
            # # expenses
            # "Bills":self.tm.repo.getTransactionsByCategory(self.user_id, "Bills"),
            # "Education":self.tm.repo.getTransactionsByCategory(self.user_id, "Education"),
            # "Entertainment":self.tm.repo.getTransactionsByCategory(self.user_id, "Entertainment"),
            # "Food & Drinks":self.tm.repo.getTransactionsByCategory(self.user_id, "Food & Drinks"),
            # "Grocery":self.tm.repo.getTransactionsByCategory(self.user_id, "Grocery"),
            # "Healthcare":self.tm.repo.getTransactionsByCategory(self.user_id, "Healthcare"),
            # "House":self.tm.repo.getTransactionsByCategory(self.user_id, "House"),
            # "Shopping":self.tm.repo.getTransactionsByCategory(self.user_id, "Shopping"),
            # "Transportation":self.tm.repo.getTransactionsByCategory(self.user_id, "Transportation"),
            # "Wellness":self.tm.repo.getTransactionsByCategory(self.user_id, "Wellness"),
            # "Other":self.tm.repo.getTransactionsByCategory(self.user_id, "Other"),
            # # savings
            # "Monthly Allowance":self.tm.repo.getTransactionsByCategory(self.user_id, "Monthly Allowance"),
            # "Change":self.tm.repo.getTransactionsByCategory(self.user_id, "Change"),
            # "Miscellaneous":self.tm.repo.getTransactionsByCategory(self.user_id, "Miscellaneous"),
            # # investment
            # "Stocks":self.tm.repo.getTransactionsByCategory(self.user_id, "Stocks"),
            # "Crypto":self.tm.repo.getTransactionsByCategory(self.user_id, "Crypto"),
            # "Bonds":self.tm.repo.getTransactionsByCategory(self.user_id, "Bonds"),
            # "Real Estate":self.tm.repo.getTransactionsByCategory(self.user_id, "Real Estate")
        }
        # for each filtered transactions, group the transactions base on table page
        all_transactions_by_filter_per_page = {}
        for t_type, transactions in all_transactions_by_filter.items():
            all_transactions_by_filter_per_page[t_type] = self._groupTransactionsPerTablePage(transactions)
        # convert transactions to rows
        all_rows_by_filter_per_page = {}
        for t_type, transactions_per_page in all_transactions_by_filter_per_page.items():
            all_rows_by_filter_per_page[t_type] = self._convertTransactionsToRowsPerTablePage(transactions_per_page)
        # return the rows
        return all_rows_by_filter_per_page

    def showRowsInCurrentPage(self):
        # hide rows for all filters
        for rows_per_page in self.all_rows_by_filter_per_page.values():
            for page_frame, rows in rows_per_page.items():
                page_frame.pack_forget()
                for row in rows:
                    row.pack_forget()
        # show rows in current page
        page_frame = list(self.current_rows_per_page.keys())[self.current_page_num]
        page_frame.pack()
        # print("\n[Table Page]")
        # i = 0
        for row in self.current_rows_per_page[page_frame]:
            row.pack(pady=(0,s.PAD_1))
            row.date_label.grid(row=0, column=0, padx=(0,s.PAD_2), pady=0, sticky="n")
            row.type_label.grid(row=0, column=1, padx=(0,s.PAD_2), pady=0, sticky="n")
            row.category_label.grid(row=0, column=2, padx=(0,s.PAD_2), pady=0, sticky="n")
            row.description_label.grid(row=0, column=3, padx=(0,s.PAD_2), pady=0, sticky="n")
            row.amount_label.grid(row=0, column=4, padx=(0,s.PAD_2), pady=0, sticky="n")
            # print(f"\t{row.date_label._text} | {row.type_label._text} | {row.category_label._text} | {row.description_label._text} | {row.amount_label._text}")
        #     i += 1
        # print(f"\t{i = }")

class History(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize state
        self.isCurrentPage = False
        # create page sections
        self.header_section = HistoryHeader(master=self, fg_color=s.BLUE, corner_radius=s.RAD_2)
        self.table_section = Table(user_id=self.user_id, tm=self.tm, header_section=self.header_section,
                                   master=self, fg_color=s.SKY_BLUE, corner_radius=0)
        # display page sections
        self.header_section.pack(pady=(s.PAD_5+s.PAD_5,0))
        self.table_section.pack(padx=s.PAD_3, pady=(s.PAD_2,0))
    
    def updatePageDisplay(self):
        # destroy prev ver of the history
        for page in self.table_section.table_body.winfo_children():
            page.destroy()
        # replace destroyed widgets with updated ones
        self.table_section.all_rows_by_filter_per_page = self.table_section.loadAllRowsByFilterPerTablePage()
        self.table_section.current_rows_per_page = self.table_section.all_rows_by_filter_per_page[self.table_section.filters.type_menu.get()]
        self.table_section.current_page_num = 0
        self.table_section.showRowsInCurrentPage()
