# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from frontend.styles import BaseStyles, HistoryStyles # paddings, dimensions, colors, etc


#--------------------------------------------------------------------------------------------------------


class HistoryHeader(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font6 = ("Bodoni MT", BaseStyles.FONT_SIZE_6, "italic")
        # title
        self.title_label = ctk.CTkLabel(
            master=self,
            text="Transaction History",
            font=self.font6,
            text_color=HistoryStyles.HEADER_TITLE_TEXT_COLOR,
            width=HistoryStyles.HEADER_TITLE_LABEL_W,
            height=HistoryStyles.HEADER_TITLE_LABEL_H, 
            fg_color=HistoryStyles.HEADER_TITLE_LABEL_FG_COLOR,
            anchor="w"
        )
        self.title_label.grid(row=0, column=0, padx=BaseStyles.PAD_4, pady=BaseStyles.PAD_1)


#--------------------------------------------------------------------------------------------------------


class TableFilters(ctk.CTkFrame):
    def __init__(self, table, master, **kwargs):
        super().__init__(master, **kwargs)
        self.table = table

        # initialize fonts
        self.font1 = ("Bodoni MT", BaseStyles.FONT_SIZE_1, "italic")

        # options
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
        
        # type filter
        self.type_menu = ctk.CTkOptionMenu(
            master=self,
            values=self.t_type,
            font=self.font1,
            dropdown_font=self.font1,
            text_color=HistoryStyles.FILTER_TYPE_MENU_TEXT_COLOR,
            fg_color=HistoryStyles.FILTER_TYPE_MENU_FG_COLOR,
            dropdown_fg_color=HistoryStyles.FILTER_TYPE_DROPDOWN_FG_COLOR,
            dropdown_hover_color=HistoryStyles.FILTER_TYPE_DROPDOWN_HOVER_COLOR,
            dropdown_text_color=HistoryStyles.FILTER_TYPE_DROPDOWN_TEXT_COLOR,
            button_color=HistoryStyles.FILTER_TYPE_BUTTON_FG_COLOR,
            button_hover_color=HistoryStyles.FILTER_TYPE_BUTTON_HOVER_COLOR,
            width=HistoryStyles.FILTER_MENU_W,
            height=HistoryStyles.FILTER_MENU_H,
            corner_radius=BaseStyles.RAD_2,
            command=self.onPickType
        )
        self.type_menu.grid(row=0, column=0, padx=(0,BaseStyles.PAD_1))
        
        # category filter
        self.current_categories = self.all_categories
        self.category_menu = ctk.CTkOptionMenu(
            master=self,
            values=self.current_categories,
            font=self.font1,
            dropdown_font=self.font1,
            text_color=HistoryStyles.FILTER_CATEGORY_MENU_TEXT_COLOR,
            fg_color=HistoryStyles.FILTER_CATEGORY_MENU_FG_COLOR,
            dropdown_fg_color=HistoryStyles.FILTER_CATEGORY_DROPDOWN_FG_COLOR,
            dropdown_hover_color=HistoryStyles.FILTER_CATEGORY_DROPDOWN_HOVER_COLOR,
            dropdown_text_color=HistoryStyles.FILTER_CATEGORY_DROPDOWN_TEXT_COLOR,
            button_color=HistoryStyles.FILTER_CATEGORY_BUTTON_FG_COLOR,
            button_hover_color=HistoryStyles.FILTER_CATEGORY_BUTTON_HOVER_COLOR,
            width=HistoryStyles.FILTER_MENU_W,
            height=HistoryStyles.FILTER_MENU_H,
            corner_radius=BaseStyles.RAD_2,
            command=self.onPickCategories
        )
        self.category_menu.grid(row=0, column=1)


    def _filterRows(self, filter_type):
        # set new table body base on type
        self.table.current_rows_per_page = self.table.all_rows_by_filter_per_page[filter_type]
        # reset page num
        self.table.current_page_num = 0
        # display current table page
        self.table.displayCurrentTablePage()


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


#--------------------------------------------------------------------------------------------------------


class TableHeader(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font3 = ("Bodoni MT", BaseStyles.FONT_SIZE_3, "italic")
        self.font4 = ("Bodoni MT", BaseStyles.FONT_SIZE_4, "italic")
        
        # date
        self.date_header = ctk.CTkLabel(
            master=self,
            text="Date",
            font=self.font3,
            text_color=HistoryStyles.DATE_COL_TEXT_COLOR,
            fg_color=HistoryStyles.DATE_COL_FG_COLOR,
            width=HistoryStyles.DATE_COL_W,
            height=HistoryStyles.TABLE_ROW_H,
            anchor="w"
        )
        self.date_header.grid(row=0, column=0, padx=(BaseStyles.PAD_2,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        
        # type
        self.type_header = ctk.CTkLabel(
            master=self,
            text="Type",
            font=self.font3,
            text_color=HistoryStyles.TYPE_COL_TEXT_COLOR,
            fg_color=HistoryStyles.TYPE_COL_FG_COLOR,
            width=HistoryStyles.TYPE_COL_W,
            height=HistoryStyles.TABLE_ROW_H,
            anchor="w"
        )
        self.type_header.grid(row=0, column=1, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        
        # category
        self.category_header = ctk.CTkLabel(
            master=self,
            text="Category",
            font=self.font3,
            text_color=HistoryStyles.CATEGORY_COL_TEXT_COLOR,
            fg_color=HistoryStyles.CATEGORY_COL_FG_COLOR,
            width=HistoryStyles.CATEGORY_COL_W,
            height=HistoryStyles.TABLE_ROW_H,
            anchor="w"
        )
        self.category_header.grid(row=0, column=2, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        
        # description
        self.description_header = ctk.CTkLabel(
            master=self,
            text="Description",
            font=self.font3,
            text_color=HistoryStyles.DESCRIPTION_COL_TEXT_COLOR,
            fg_color=HistoryStyles.DESCRIPTION_COL_FG_COLOR,
            width=HistoryStyles.DESCRIPTION_COL_W,
            height=HistoryStyles.TABLE_ROW_H,
            anchor="w"
        )
        self.description_header.grid(row=0, column=3, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        
        # amount
        self.amount_header = ctk.CTkLabel(
            master=self,
            text="Amount",
            font=self.font3,
            text_color=HistoryStyles.AMOUNT_COL_TEXT_COLOR,
            fg_color=HistoryStyles.AMOUNT_COL_FG_COLOR,
            width=HistoryStyles.AMOUNT_COL_W,
            height=HistoryStyles.TABLE_ROW_H,
            anchor="e"
        )
        self.amount_header.grid(row=0, column=4, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)


#--------------------------------------------------------------------------------------------------------


class TableRow(ctk.CTkFrame):
    def __init__(self, transaction, master, **kwargs):
        super().__init__(master, **kwargs)
        self.t = transaction
        
        # initialize font
        self.font2 = ("Bodoni MT", BaseStyles.FONT_SIZE_2, "italic")
        self.font4 = ("Bodoni MT", BaseStyles.FONT_SIZE_4, "italic")
        
        # date
        self.date_col = ctk.CTkLabel(
            master=self,
            text=self.t.t_date,
            font=self.font2,
            text_color=HistoryStyles.DATE_COL_TEXT_COLOR,
            fg_color=HistoryStyles.DATE_COL_FG_COLOR,
            width=HistoryStyles.DATE_COL_W,
            height=HistoryStyles.TABLE_ROW_H,
            wraplength=HistoryStyles.DATE_COL_W,
            anchor="w",
            justify="left"
        )
        
        # type
        self.type_col = ctk.CTkLabel(
            master=self,
            text=self.t.t_type,
            font=self.font2,
            text_color=HistoryStyles.TYPE_COL_TEXT_COLOR,
            fg_color=HistoryStyles.TYPE_COL_FG_COLOR,
            width=HistoryStyles.TYPE_COL_W,
            height=HistoryStyles.TABLE_ROW_H,
            wraplength=HistoryStyles.TYPE_COL_W,
            anchor="w",
            justify="left"
        )
        
        # category
        self.category_col = ctk.CTkLabel(
            master=self,
            text=self.t.t_category,
            font=self.font2,
            text_color=HistoryStyles.CATEGORY_COL_TEXT_COLOR,
            fg_color=HistoryStyles.CATEGORY_COL_FG_COLOR,
            width=HistoryStyles.CATEGORY_COL_W,
            height=HistoryStyles.TABLE_ROW_H,
            wraplength=HistoryStyles.CATEGORY_COL_W,
            anchor="w",
            justify="left"
        )
        
        # description
        self.description_col = ctk.CTkLabel(
            master=self,
            text=self.t.t_description,
            font=self.font2,
            text_color=HistoryStyles.DESCRIPTION_COL_TEXT_COLOR,
            fg_color=HistoryStyles.DESCRIPTION_COL_FG_COLOR,
            width=HistoryStyles.DESCRIPTION_COL_W,
            height=HistoryStyles.TABLE_ROW_H,
            wraplength=HistoryStyles.DESCRIPTION_COL_W,
            anchor="w",
            justify="left"
        )
        
        # amount
        if self.t.t_type == "income":
            amount = f"₱ +{self.t.t_amount}"
        elif self.t.t_type == "expense":
            amount = f"₱ -{self.t.t_amount}"
        else:
            amount = f"₱ {self.t.t_amount}"
        self.amount_col = ctk.CTkLabel(
            master=self,
            text=amount,
            font=self.font2,
            text_color=HistoryStyles.AMOUNT_COL_TEXT_COLOR,
            fg_color=HistoryStyles.AMOUNT_COL_FG_COLOR,
            width=HistoryStyles.AMOUNT_COL_W-BaseStyles.PAD_1,
            height=HistoryStyles.TABLE_ROW_H,
            wraplength=HistoryStyles.AMOUNT_COL_W,
            anchor="e",
            justify="right"
        )
        
        
#--------------------------------------------------------------------------------------------------------


class TableNavigation(ctk.CTkFrame):
    def __init__(self, table, master, **kwargs):
        super().__init__(master, **kwargs)
        self.table = table
        self.font1 = ("Bodoni MT", BaseStyles.FONT_SIZE_1, "italic")
        
        # previous button
        self.prevBTN = ctk.CTkButton(
            master=self,
            text="Prev",
            text_color=HistoryStyles.NAV_PREV_BUTTON_TEXT_COLOR,
            fg_color=HistoryStyles.NAV_PREV_BUTTON_FG_COLOR,
            hover_color=HistoryStyles.NAV_PREV_BUTTON_HOVER_COLOR,
            width=HistoryStyles.TABLE_NAV_BTN_W,
            height=HistoryStyles.TABLE_NAV_BTN_H,
            font=self.font1,
            corner_radius=BaseStyles.RAD_2,
            command=self.onClickPrev
        )
        self.prevBTN.grid(row=0, column=0, padx=(0,BaseStyles.PAD_1))

        # next button
        self.nextBTN = ctk.CTkButton(
            master=self,
            text="Next",
            text_color=HistoryStyles.NAV_NEXT_BUTTON_TEXT_COLOR,
            fg_color=HistoryStyles.NAV_NEXT_BUTTON_FG_COLOR,
            hover_color=HistoryStyles.NAV_NEXT_BUTTON_HOVER_COLOR,
            width=HistoryStyles.TABLE_NAV_BTN_W,
            height=HistoryStyles.TABLE_NAV_BTN_H,
            font=self.font1,
            corner_radius=BaseStyles.RAD_2,
            command=self.onClickNext
        )
        self.nextBTN.grid(row=0, column=1)


    def onClickPrev(self):
        if self.table.current_page_num > 0:
            self.table.current_page_num -= 1
            # print("table prev")
            self.after_idle(self.table.displayCurrentTablePage)
            self.table.displayCurrentTable()
        

    def onClickNext(self):
        if self.table.current_page_num < len(self.table.current_rows_per_page) - 1:
            self.table.current_page_num += 1
            # print("table next")
            self.after_idle(self.table.displayCurrentTablePage)


#--------------------------------------------------------------------------------------------------------


class Table(ctk.CTkFrame):
    def __init__(self, app, tm, header_section, master, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app
        self.tm = tm

        # initialize font
        self.font3 = ("Bodoni MT", BaseStyles.FONT_SIZE_3, "italic")
        self.font4 = ("Bodoni MT", BaseStyles.FONT_SIZE_4, "italic")
        
        # table filter
        self.filters = TableFilters(
            table=self,
            master=header_section,
            fg_color=HistoryStyles.FILTERS_FRAME_FG_COLOR
        )
        self.filters.grid(row=0, column=1, padx=(0, BaseStyles.PAD_2), pady=(0,BaseStyles.PAD_2), sticky="s")
        
        # table header
        self.table_header = TableHeader(
            master=self,
            corner_radius=BaseStyles.RAD_2,
            fg_color=HistoryStyles.TABLE_HEADER_FG_COLOR
        )
        self.table_header.pack(pady=(0,BaseStyles.PAD_1))
        
        # table body
        self.table_body = ctk.CTkScrollableFrame(
            master=self,
            fg_color=HistoryStyles.TABLE_BODY_FG_COLOR,
            orientation="vertical",
            corner_radius=BaseStyles.RAD_2,
            height=HistoryStyles.TABLE_BODY_H,
            width=HistoryStyles.TABLE_BODY_W
        )
        self.table_body.pack()
        
        # table navigation tabs
        self.table_nav = TableNavigation(
            table=self,
            master=self,
            fg_color=HistoryStyles.TABLE_NAV_FG_COLOR
        )
        self.table_nav.pack(pady=(BaseStyles.PAD_1,0))
        
        # initialize table content
        self.all_rows_by_filter_per_page = self.loadAllRowsByFilterPerTablePage()
        self.current_rows_per_page = self.all_rows_by_filter_per_page["All Types"]
        self.current_page_num = 0
        
        # display default table page
        self.displayCurrentTablePage()


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
            page_frame = ctk.CTkFrame(self.table_body, fg_color=HistoryStyles.TABLE_PAGE_FRAME_FG_COLOR)
            rows = []
            for t in transactions:
                row = TableRow(transaction=t, master=page_frame, fg_color=HistoryStyles.TABLE_ROW_FG_COLOR)
                rows.append(row)
            rows_per_page[page_frame] = rows
        return rows_per_page


    def loadAllRowsByFilterPerTablePage(self):
        # retrieve all transactions from db base on filter
        all_transactions_by_filter = {
            "All Types": self.tm.repo.getAllTransactions(self.app.user_id),
            "Income": self.tm.repo.getTransactionsByType(self.app.user_id, "income"),
            "Savings": self.tm.repo.getTransactionsByType(self.app.user_id, "savings"),
            "Expenses": self.tm.repo.getTransactionsByType(self.app.user_id, "expense"),
            "Investment": self.tm.repo.getTransactionsByType(self.app.user_id, "investment"),
            # # income
            # "Salary":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Salary"),
            # "Bonus":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Bonus"),
            # "Side-hustles":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Side-hustles"),
            # "Tips":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Tips"),
            # # expenses
            # "Bills":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Bills"),
            # "Education":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Education"),
            # "Entertainment":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Entertainment"),
            # "Food & Drinks":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Food & Drinks"),
            # "Grocery":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Grocery"),
            # "Healthcare":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Healthcare"),
            # "House":self.tm.repo.getTransactionsByCategory(self.app.user_id, "House"),
            # "Shopping":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Shopping"),
            # "Transportation":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Transportation"),
            # "Wellness":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Wellness"),
            # "Other":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Other"),
            # # savings
            # "Monthly Allowance":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Monthly Allowance"),
            # "Change":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Change"),
            # "Miscellaneous":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Miscellaneous"),
            # # investment
            # "Stocks":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Stocks"),
            # "Crypto":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Crypto"),
            # "Bonds":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Bonds"),
            # "Real Estate":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Real Estate")
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


    def _hideRowsOfOtherPages(self):
        # hide rows for all filters
        for rows_per_page in self.all_rows_by_filter_per_page.values():
            for page_frame, rows in rows_per_page.items():
                page_frame.pack_forget()
                for row in rows:
                    row.pack_forget()


    def _showRowsOfCurrentPage(self):
        # show rows in current page
        if self.current_rows_per_page:
            page_frame = list(self.current_rows_per_page.keys())[self.current_page_num]
            page_frame.pack()
            # print("\n[Table Page]")
            # i = 0
            for row in self.current_rows_per_page[page_frame]:
                row.pack(pady=(0,BaseStyles.PAD_1))
                row.date_col.grid(row=0, column=0, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
                row.type_col.grid(row=0, column=1, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
                row.category_col.grid(row=0, column=2, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
                row.description_col.grid(row=0, column=3, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
                row.amount_col.grid(row=0, column=4, padx=(0,BaseStyles.PAD_2), pady=0, sticky="nw")
                # print(f"\t{row.date_label._text} | {row.type_label._text} | {row.category_label._text} | {row.description_label._text} | {row.amount_label._text}")
            #     i += 1
            # print(f"\t{i = }")


    def displayCurrentTablePage(self):
        self._hideRowsOfOtherPages()
        self.after_idle(self._showRowsOfCurrentPage)


#--------------------------------------------------------------------------------------------------------


class HistoryPage(ctk.CTkFrame):
    def __init__(self, app, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app
        self.tm = tm

        # initialize state
        self.is_current_page = False

        # header
        self.header_section = HistoryHeader(
            master=self,
            fg_color=HistoryStyles.HEADER_SECTION_FG_COLOR,
            corner_radius=BaseStyles.RAD_2
        )
        self.header_section.pack(pady=(BaseStyles.PAD_5+BaseStyles.PAD_5,0))

        # table
        self.table_section = Table(
            app=self.app,
            tm=self.tm,
            header_section=self.header_section,
            master=self,
            fg_color=HistoryStyles.TABLE_SECTION_FG_COLOR,
            corner_radius=0
        )
        self.table_section.pack(padx=BaseStyles.PAD_3, pady=(BaseStyles.PAD_2,0))
    
    
    def updatePageDisplay(self):
        # destroy prev ver of the history
        for page in self.table_section.table_body.winfo_children():
            page.destroy()
        
        # replace destroyed widgets with updated ones
        self.table_section.all_rows_by_filter_per_page = self.table_section.loadAllRowsByFilterPerTablePage()
        self.table_section.current_rows_per_page = self.table_section.all_rows_by_filter_per_page[self.table_section.filters.type_menu.get()]
        self.table_section.current_page_num = 0
        self.table_section.displayCurrentTablePage()
