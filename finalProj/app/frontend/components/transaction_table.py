# external/built-in modules/libs
import customtkinter as ctk
from typing import Dict, List
# our modules/libs
from frontend.styles import BaseStyles, TransactionTableStyles # paddings, dimensions, colors, etc
from backend import Transaction


#--------------------------------------------------------------------------------------------------------


class TransactionTableHeader(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font3 = ("Bodoni MT", BaseStyles.FONT_SIZE_3, "italic")
        self.font4 = ("Bodoni MT", BaseStyles.FONT_SIZE_4, "italic")
        
        # date
        self.date_header = ctk.CTkLabel(
            master=self,
            text="Date",
            font=self.font3,
            text_color=TransactionTableStyles.DATE_COL_TEXT_COLOR,
            fg_color=TransactionTableStyles.DATE_COL_FG_COLOR,
            width=TransactionTableStyles.DATE_COL_W,
            height=TransactionTableStyles.TABLE_ROW_H,
            anchor="w"
        )
        self.date_header.grid(row=0, column=0, padx=(BaseStyles.PAD_2,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        
        # type
        self.type_header = ctk.CTkLabel(
            master=self,
            text="Type",
            font=self.font3,
            text_color=TransactionTableStyles.TYPE_COL_TEXT_COLOR,
            fg_color=TransactionTableStyles.TYPE_COL_FG_COLOR,
            width=TransactionTableStyles.TYPE_COL_W,
            height=TransactionTableStyles.TABLE_ROW_H,
            anchor="w"
        )
        self.type_header.grid(row=0, column=1, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        
        # category
        self.category_header = ctk.CTkLabel(
            master=self,
            text="Category",
            font=self.font3,
            text_color=TransactionTableStyles.CATEGORY_COL_TEXT_COLOR,
            fg_color=TransactionTableStyles.CATEGORY_COL_FG_COLOR,
            width=TransactionTableStyles.CATEGORY_COL_W,
            height=TransactionTableStyles.TABLE_ROW_H,
            anchor="w"
        )
        self.category_header.grid(row=0, column=2, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        
        # description
        self.description_header = ctk.CTkLabel(
            master=self,
            text="Description",
            font=self.font3,
            text_color=TransactionTableStyles.DESCRIPTION_COL_TEXT_COLOR,
            fg_color=TransactionTableStyles.DESCRIPTION_COL_FG_COLOR,
            width=TransactionTableStyles.DESCRIPTION_COL_W,
            height=TransactionTableStyles.TABLE_ROW_H,
            anchor="w"
        )
        self.description_header.grid(row=0, column=3, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        
        # amount
        self.amount_header = ctk.CTkLabel(
            master=self,
            text="Amount",
            font=self.font3,
            text_color=TransactionTableStyles.AMOUNT_COL_TEXT_COLOR,
            fg_color=TransactionTableStyles.AMOUNT_COL_FG_COLOR,
            width=TransactionTableStyles.AMOUNT_COL_W,
            height=TransactionTableStyles.TABLE_ROW_H,
            anchor="e"
        )
        self.amount_header.grid(row=0, column=4, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)


#--------------------------------------------------------------------------------------------------------


class TransactionTableRow(ctk.CTkFrame):
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
            text_color=TransactionTableStyles.DATE_COL_TEXT_COLOR,
            fg_color=TransactionTableStyles.DATE_COL_FG_COLOR,
            width=TransactionTableStyles.DATE_COL_W,
            height=TransactionTableStyles.TABLE_ROW_H,
            wraplength=TransactionTableStyles.DATE_COL_W,
            anchor="w",
            justify="left"
        )
        
        # type
        self.type_col = ctk.CTkLabel(
            master=self,
            text=self.t.t_type,
            font=self.font2,
            text_color=TransactionTableStyles.TYPE_COL_TEXT_COLOR,
            fg_color=TransactionTableStyles.TYPE_COL_FG_COLOR,
            width=TransactionTableStyles.TYPE_COL_W,
            height=TransactionTableStyles.TABLE_ROW_H,
            wraplength=TransactionTableStyles.TYPE_COL_W,
            anchor="w",
            justify="left"
        )
        
        # category
        self.category_col = ctk.CTkLabel(
            master=self,
            text=self.t.t_category,
            font=self.font2,
            text_color=TransactionTableStyles.CATEGORY_COL_TEXT_COLOR,
            fg_color=TransactionTableStyles.CATEGORY_COL_FG_COLOR,
            width=TransactionTableStyles.CATEGORY_COL_W,
            height=TransactionTableStyles.TABLE_ROW_H,
            wraplength=TransactionTableStyles.CATEGORY_COL_W,
            anchor="w",
            justify="left"
        )
        
        # description
        self.description_col = ctk.CTkLabel(
            master=self,
            text=self.t.t_description,
            font=self.font2,
            text_color=TransactionTableStyles.DESCRIPTION_COL_TEXT_COLOR,
            fg_color=TransactionTableStyles.DESCRIPTION_COL_FG_COLOR,
            width=TransactionTableStyles.DESCRIPTION_COL_W,
            height=TransactionTableStyles.TABLE_ROW_H,
            wraplength=TransactionTableStyles.DESCRIPTION_COL_W,
            anchor="w",
            justify="left"
        )
        
        # amount
        if self.t.t_type == "income":
            amount = f"₱ +{self.t.t_amount:,}"
        elif self.t.t_type == "expense":
            amount = f"₱ -{self.t.t_amount:,}"
        else:
            amount = f"₱ {self.t.t_amount:,}"
        self.amount_col = ctk.CTkLabel(
            master=self,
            text=amount,
            font=self.font2,
            text_color=TransactionTableStyles.AMOUNT_COL_TEXT_COLOR,
            fg_color=TransactionTableStyles.AMOUNT_COL_FG_COLOR,
            width=TransactionTableStyles.AMOUNT_COL_W-BaseStyles.PAD_1,
            height=TransactionTableStyles.TABLE_ROW_H,
            wraplength=TransactionTableStyles.AMOUNT_COL_W,
            anchor="e",
            justify="right"
        )
        
        
#--------------------------------------------------------------------------------------------------------


class TablePage(ctk.CTkFrame):
    def __init__(self, transactions, master, **kwargs):
        super().__init__(master, **kwargs)
        self.rows = []

        self.createRows(transactions=transactions)


    def createRows(self, transactions):
        for t in transactions:
            row = TransactionTableRow(
                transaction=t,
                master=self,
                fg_color=TransactionTableStyles.TABLE_ROW_FG_COLOR
            )
            self.rows.append(row)
    
    
    def showRows(self):
        for row in self.rows:
            row.date_col.grid(row=0, column=0, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
            row.type_col.grid(row=0, column=1, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
            row.category_col.grid(row=0, column=2, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
            row.description_col.grid(row=0, column=3, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
            row.amount_col.grid(row=0, column=4, padx=(0,BaseStyles.PAD_2), pady=0, sticky="nw")
            row.pack(pady=(0,BaseStyles.PAD_1))
            self.update_idletasks


#--------------------------------------------------------------------------------------------------------


class TransactionTableBody(ctk.CTkScrollableFrame):
    def __init__(self, init_filter_type, transactions_per_filter: Dict[str, List[Transaction]], master, **kwargs):
        super().__init__(master, **kwargs)
        self.current_page_num = 0
        self.filter_type = init_filter_type
        self.transactions_per_filter = transactions_per_filter
        
        # self.filtered_table_pages = []
        self.pages_count = 0
        self.transactions_per_page = dict()
        self.current_table_page = None

        self.filterTransactions()
        self.countFilteredTablePages()
        self.separateFilteredTransactionsPerPage()
        self.updateCurrentTablePage()


    def filterTransactions(self):
        self.filtered_transactions = self.transactions_per_filter[self.filter_type]
        print(f"[DEBUG] {self.filter_type = }")


    def countFilteredTablePages(self):
        num = len(self.filtered_transactions) / 20 # 20 transactions per page
        if num.is_integer():
            self.pages_count = int(num)
        else:
            self.pages_count = int(num) + 1 # plus one page for excess transactions
        print(f"[DEBUG] {self.pages_count = }")


    def separateFilteredTransactionsPerPage(self):
        i = 0
        for j in range(len((self.filtered_transactions))):

            if j % 20 != 0: # skip if not div by 20
                continue

            transactions = self.filtered_transactions[i*20: i*20+20]
            self.transactions_per_page.update({i: transactions})
            i += 1


    def _destroyPrevTablePage(self):
        if self.current_table_page:
            print("[DEBUG] _destroyPrevTablePage()")
            self.current_table_page.destroy()
        self.update_idletasks()


    def _createCurrentTablePage(self):
        print("[DEBUG] _createCurrentTablePage()")
        transactions = self.transactions_per_page[self.current_page_num]
        self.current_table_page = TablePage(
            transactions=transactions,
            master=self,
            fg_color=TransactionTableStyles.TABLE_PAGE_FRAME_FG_COLOR
        )


    def _displayCurrentTablePage(self):
        print("[DEBUG] _displayCurrentTablePage()")
        self.current_table_page.showRows()
        self.current_table_page.pack()
        self.update_idletasks()


    def updateCurrentTablePage(self):
        print("[DEBUG] updateCurrentTablePage()")
        self._destroyPrevTablePage()
        if self.pages_count == 0:
            print("[DEBUG] empty page")
            return
        self._createCurrentTablePage()
        self._displayCurrentTablePage()


#--------------------------------------------------------------------------------------------------------


class TransactionTableNavigation(ctk.CTkFrame):
    def __init__(self, table_body, master, **kwargs):
        super().__init__(master, **kwargs)
        self.table_body = table_body
        self.font1 = ("Bodoni MT", BaseStyles.FONT_SIZE_1, "italic")
        
        # previous button
        self.prevBTN = ctk.CTkButton(
            master=self,
            text="Prev",
            text_color=TransactionTableStyles.NAV_PREV_ON_BTN_TEXT_COLOR,
            fg_color=TransactionTableStyles.NAV_PREV_ON_BTN_FG_COLOR,
            hover_color=TransactionTableStyles.NAV_PREV_BTN_HOVER_COLOR,
            width=TransactionTableStyles.TABLE_NAV_BTN_W,
            height=TransactionTableStyles.TABLE_NAV_BTN_H,
            font=self.font1,
            corner_radius=BaseStyles.RAD_2,
            text_color_disabled=TransactionTableStyles.NAV_PREV_OFF_BTN_TEXT_COLOR,
            command=self.onClickPrev,
        )
        self.prevBTN.grid(row=0, column=0, padx=(0,BaseStyles.PAD_1))

        page_num_text = self.table_body.current_page_num + 1
        if self.table_body.pages_count == 0:
            page_num_text = 0
        # page number display
        self.page_num_label = ctk.CTkLabel(
            master=self,
            corner_radius=BaseStyles.RAD_2,
            font=self.font1,
            text=f"{page_num_text}/{self.table_body.pages_count}",
            text_color=TransactionTableStyles.PAGE_NUM_LABEL_TEXT_COLOR,
            fg_color=TransactionTableStyles.PAGE_NUM_LABEL_FG_COLOR,
            width=TransactionTableStyles.PAGE_NUM_LABEL_W,
            height=TransactionTableStyles.PAGE_NUM_LABEL_H,
            anchor="center",
            justify="center"
        )
        self.page_num_label.grid(row=0, column=1, padx=(0,BaseStyles.PAD_1))

        # next button
        self.nextBTN = ctk.CTkButton(
            master=self,
            text="Next",
            text_color=TransactionTableStyles.NAV_NEXT_ON_BTN_TEXT_COLOR,
            fg_color=TransactionTableStyles.NAV_NEXT_ON_BTN_FG_COLOR,
            hover_color=TransactionTableStyles.NAV_NEXT_BTN_HOVER_COLOR,
            width=TransactionTableStyles.TABLE_NAV_BTN_W,
            height=TransactionTableStyles.TABLE_NAV_BTN_H,
            font=self.font1,
            corner_radius=BaseStyles.RAD_2,
            text_color_disabled=TransactionTableStyles.NAV_NEXT_OFF_BTN_TEXT_COLOR,
            command=self.onClickNext
        )
        self.nextBTN.grid(row=0, column=2)

        self.initializeBTNsState()
        

    def initializeBTNsState(self):
        # disable table navigation if in first and/or last page
        self.prevBTN.configure(state="disabled", fg_color=TransactionTableStyles.NAV_PREV_OFF_BTN_FG_COLOR)
        if self.table_body.pages_count in [0, 1]: # has no or only has one page
            self.nextBTN.configure(state="disabled", fg_color=TransactionTableStyles.NAV_NEXT_OFF_BTN_FG_COLOR)
        else:
            self.nextBTN.configure(state="normal", fg_color=TransactionTableStyles.NAV_NEXT_ON_BTN_FG_COLOR)


    def _disableBTN(self, btn_name):
        if btn_name == "prev":
            self.prevBTN.configure(state="disabled", fg_color=TransactionTableStyles.NAV_PREV_OFF_BTN_FG_COLOR)
        elif btn_name == "next":
            self.nextBTN.configure(state="disabled", fg_color=TransactionTableStyles.NAV_NEXT_OFF_BTN_FG_COLOR)
        self.update_idletasks()


    def _enableBTN(self, btn_name):
        if btn_name == "prev":
            self.prevBTN.configure(state="normal", fg_color=TransactionTableStyles.NAV_PREV_ON_BTN_FG_COLOR)
        elif btn_name == "next":
            self.nextBTN.configure(state="normal", fg_color=TransactionTableStyles.NAV_NEXT_ON_BTN_FG_COLOR)
        self.update_idletasks()


    def _updatePageNumberDisplay(self):
        if self.table_body.pages_count == 0: # no page
            self.page_num_label.configure(text="0/0")
            print("[DEBUG] 0/0 page")
        else:
            self.page_num_label.configure(text=f"{self.table_body.current_page_num+1}/{self.table_body.pages_count}")


    def onClickPrev(self):
        self._disableBTN("prev")

        if self.table_body.current_page_num > 0:
            # update page num & display
            self.table_body.current_page_num -= 1
            self.table_body.updateCurrentTablePage()
            self._updatePageNumberDisplay() 

            if self.table_body.current_page_num != 0: # if not last
                self.after(100, lambda: self._enableBTN("prev")) # delay to avoid rapid clicks bug

            self._enableBTN("next")
        

    def onClickNext(self):
        self._disableBTN("next")

        if self.table_body.current_page_num < self.table_body.pages_count - 1:
            # update page num & display
            self.table_body.current_page_num += 1
            self.table_body.updateCurrentTablePage()
            self._updatePageNumberDisplay() 

            if self.table_body.current_page_num != self.table_body.pages_count - 1:
                self.after(100, lambda: self._enableBTN("next")) # delay to avoid rapid clicks bug
            
            self._enableBTN("prev")


#--------------------------------------------------------------------------------------------------------


class TransactionTableFilters(ctk.CTkFrame):
    def __init__(self, table_body, table_nav, master, **kwargs):
        super().__init__(master, **kwargs)
        self.table_body = table_body
        self.table_nav = table_nav

        # initialize fonts
        self.font1 = ("Bodoni MT", BaseStyles.FONT_SIZE_1, "italic")

        # options
        self.t_type = ["All Types"] + sorted(["Income", "Expenses", "Savings", "Investment"])
        self.categories_by_type = {
            "Income": ["All Categories"] + sorted(["Salary", "Bonus", "Side-hustles", "Tips"]),
            "Expenses": ["All Categories"] + sorted(["Bills", "Education", "Entertainment", "Food & Drinks",
                        "Grocery", "Healthcare", "House", "Shopping",
                        "Transportation", "Wellness", "Other"]),
            "Savings": ["All Categories"] + sorted(["Monthly Allowance", "Change", "Miscellaneous"]),
            "Investment": ["All Categories"] + sorted(["Stocks", "Crypto", "Bonds", "Real Estate"])
        }
        self.all_categories = ["All Categories"] + sorted([c for categories in self.categories_by_type.values() for c in categories if c != "All Categories"])
        
        # type filter
        self.type_menu = ctk.CTkOptionMenu(
            master=self,
            values=self.t_type,
            font=self.font1,
            dropdown_font=self.font1,
            text_color=TransactionTableStyles.FILTER_TYPE_MENU_TEXT_COLOR,
            fg_color=TransactionTableStyles.FILTER_TYPE_MENU_FG_COLOR,
            dropdown_fg_color=TransactionTableStyles.FILTER_TYPE_DROPDOWN_FG_COLOR,
            dropdown_hover_color=TransactionTableStyles.FILTER_TYPE_DROPDOWN_HOVER_COLOR,
            dropdown_text_color=TransactionTableStyles.FILTER_TYPE_DROPDOWN_TEXT_COLOR,
            button_color=TransactionTableStyles.FILTER_TYPE_BTN_FG_COLOR,
            button_hover_color=TransactionTableStyles.FILTER_TYPE_BTN_HOVER_COLOR,
            width=TransactionTableStyles.FILTER_MENU_W,
            height=TransactionTableStyles.FILTER_MENU_H,
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
            text_color=TransactionTableStyles.FILTER_CATEGORY_MENU_TEXT_COLOR,
            fg_color=TransactionTableStyles.FILTER_CATEGORY_MENU_FG_COLOR,
            dropdown_fg_color=TransactionTableStyles.FILTER_CATEGORY_DROPDOWN_FG_COLOR,
            dropdown_hover_color=TransactionTableStyles.FILTER_CATEGORY_DROPDOWN_HOVER_COLOR,
            dropdown_text_color=TransactionTableStyles.FILTER_CATEGORY_DROPDOWN_TEXT_COLOR,
            button_color=TransactionTableStyles.FILTER_CATEGORY_BTN_FG_COLOR,
            button_hover_color=TransactionTableStyles.FILTER_CATEGORY_BTN_HOVER_COLOR,
            width=TransactionTableStyles.FILTER_MENU_W,
            height=TransactionTableStyles.FILTER_MENU_H,
            corner_radius=BaseStyles.RAD_2,
            command=self.onPickCategory
        )
        self.category_menu.grid(row=0, column=1)


    def _filterRows(self, filter_type):
        # reset current page
        self.table_body.current_page_num = 0
        self.table_body.filter_type = filter_type
        self.table_body.filterTransactions()
        self.table_body.separateFilteredTransactionsPerPage()
        self.table_body.countFilteredTablePages()
        self.table_body.updateCurrentTablePage()

    
    def _initializeBTNsState(self):
        # disable table navigation if in first and last page
        self.table_nav.prevBTN.configure(state="disabled", fg_color=TransactionTableStyles.NAV_PREV_OFF_BTN_FG_COLOR)
        if self.table_body.pages_count in [0, 1]:
            self.table_nav.nextBTN.configure(state="disabled", fg_color=TransactionTableStyles.NAV_NEXT_OFF_BTN_FG_COLOR)
        else:
            self.table_nav.nextBTN.configure(state="normal", fg_color=TransactionTableStyles.NAV_NEXT_ON_BTN_FG_COLOR)


    def _updateCategoryMenuByType(self, t_type):
        if t_type == "All Types":
            self.current_categories = self.all_categories
        else:
            self.current_categories = self.categories_by_type[t_type]
        self.category_menu.configure(values=self.current_categories)
        self.category_menu.set(self.current_categories[0])
    

    def onPickType(self, t_type):
        print("[ON CLICK] onPickType()")
        self.after_idle(self._filterRows, t_type)
        self.after_idle(self._initializeBTNsState)
        self.after_idle(self.table_nav._updatePageNumberDisplay)
        self.after_idle(self._updateCategoryMenuByType, t_type)
        self.update_idletasks()


    def onPickCategory(self, t_category):
        print("[ON CLICK] onPickCategory()")
        self.after_idle(self._filterRows, t_category)
        self.after_idle(self._initializeBTNsState)
        self.after_idle(self.table_nav._updatePageNumberDisplay)
        self.update_idletasks()

