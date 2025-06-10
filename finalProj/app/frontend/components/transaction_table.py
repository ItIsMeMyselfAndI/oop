# external/built-in modules/libs
import customtkinter as ctk
from typing import Dict, List
# our modules/libs
from frontend.styles import BaseStyles, TransactionTableStyles # paddings, dimensions, colors, etc


#--------------------------------------------------------------------------------------------------------


class TransactionTableFilters(ctk.CTkFrame):
    def __init__(self, table_body, master, **kwargs):
        super().__init__(master, **kwargs)
        self.table_body = table_body

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
            text_color=TransactionTableStyles.FILTER_TYPE_MENU_TEXT_COLOR,
            fg_color=TransactionTableStyles.FILTER_TYPE_MENU_FG_COLOR,
            dropdown_fg_color=TransactionTableStyles.FILTER_TYPE_DROPDOWN_FG_COLOR,
            dropdown_hover_color=TransactionTableStyles.FILTER_TYPE_DROPDOWN_HOVER_COLOR,
            dropdown_text_color=TransactionTableStyles.FILTER_TYPE_DROPDOWN_TEXT_COLOR,
            button_color=TransactionTableStyles.FILTER_TYPE_BUTTON_FG_COLOR,
            button_hover_color=TransactionTableStyles.FILTER_TYPE_BUTTON_HOVER_COLOR,
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
            button_color=TransactionTableStyles.FILTER_CATEGORY_BUTTON_FG_COLOR,
            button_hover_color=TransactionTableStyles.FILTER_CATEGORY_BUTTON_HOVER_COLOR,
            width=TransactionTableStyles.FILTER_MENU_W,
            height=TransactionTableStyles.FILTER_MENU_H,
            corner_radius=BaseStyles.RAD_2,
            command=self.onPickCategories
        )
        self.category_menu.grid(row=0, column=1)


    def _filterRows(self, filter_type):
        # set new table body base on type
        self.table_body.current_filter_pages = self.table_body.pages_per_filter[filter_type]
        # reset page num
        self.table_body.current_page_num = 0
        # display current table page
        self.table_body.displayCurrentTablePage()


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
        self._filterRows(filter_type=t_categories)
        pass


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


class TransactionTableBody(ctk.CTkScrollableFrame):
    def __init__(self, has_filter, transactions_per_filter, master, **kwargs):
        super().__init__(master, **kwargs)
        self.has_filter = has_filter

        self.current_page_num = 0
        self.initializeTableBodyContent(transactions_per_filter)

        # display default table page
        self.displayCurrentTablePage()


    def initializeTableBodyContent(self, transactions_per_filter):
        self.pages_per_filter = self.createTablePagesPerFilter(transactions_per_filter=transactions_per_filter)
        if self.has_filter:
            self.current_filter_pages = self.pages_per_filter["All Types"]
        else:
            self.current_filter_pages = list(self.pages_per_filter.values())[0]


    def _createTablePages(self, transactions) -> List[ctk.CTkFrame]:
        # get number of pages
        pages_count = len(transactions) / 20 # 20 transactions per page
        if pages_count.is_integer():
            pages_count = int(pages_count)
        else:
            pages_count = int(pages_count) + 1 # plus one page for excess transactions
        # create pages
        pages = []
        for _ in range(pages_count):
            page_frame = ctk.CTkFrame(self, fg_color=TransactionTableStyles.TABLE_PAGE_FRAME_FG_COLOR)
            pages.append(page_frame)
        return pages


    def createTablePagesPerFilter(self, transactions_per_filter) -> Dict[str, List[ctk.CTkFrame]]:
        pages_per_filter = {}
        for filter_name, transactions in transactions_per_filter.items():
            pages = self._createTablePages(transactions=transactions)
            for i, t in enumerate(transactions):
                if i % 20 == 0:
                    page_frame = pages[i // 20]
                row = TransactionTableRow(transaction=t, master=page_frame, fg_color=TransactionTableStyles.TABLE_ROW_FG_COLOR)
            pages_per_filter.update({filter_name: pages})
        return pages_per_filter

        
    def _hideAllTablePages(self):
        # hide table pages for all filters 
        for pages in self.pages_per_filter.values():
            for page_frame in pages:
                page_frame.pack_forget()


    def _showCurrentTablePage(self):
        # show rows in current page
        if self.current_filter_pages:
            page_frame = list(self.current_filter_pages)[self.current_page_num]
            page_frame.pack()
            for row in page_frame.winfo_children():
                row.pack(pady=(0,BaseStyles.PAD_1))
                row.date_col.grid(row=0, column=0, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
                row.type_col.grid(row=0, column=1, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
                row.category_col.grid(row=0, column=2, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
                row.description_col.grid(row=0, column=3, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
                row.amount_col.grid(row=0, column=4, padx=(0,BaseStyles.PAD_2), pady=0, sticky="nw")


    def displayCurrentTablePage(self):
        self._hideAllTablePages()
        self.after_idle(self._showCurrentTablePage)


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
            text_color=TransactionTableStyles.NAV_PREV_BUTTON_TEXT_COLOR,
            fg_color=TransactionTableStyles.NAV_PREV_BUTTON_FG_COLOR,
            hover_color=TransactionTableStyles.NAV_PREV_BUTTON_HOVER_COLOR,
            width=TransactionTableStyles.TABLE_NAV_BTN_W,
            height=TransactionTableStyles.TABLE_NAV_BTN_H,
            font=self.font1,
            corner_radius=BaseStyles.RAD_2,
            command=self.onClickPrev
        )
        self.prevBTN.grid(row=0, column=0, padx=(0,BaseStyles.PAD_1))

        # next button
        self.nextBTN = ctk.CTkButton(
            master=self,
            text="Next",
            text_color=TransactionTableStyles.NAV_NEXT_BUTTON_TEXT_COLOR,
            fg_color=TransactionTableStyles.NAV_NEXT_BUTTON_FG_COLOR,
            hover_color=TransactionTableStyles.NAV_NEXT_BUTTON_HOVER_COLOR,
            width=TransactionTableStyles.TABLE_NAV_BTN_W,
            height=TransactionTableStyles.TABLE_NAV_BTN_H,
            font=self.font1,
            corner_radius=BaseStyles.RAD_2,
            command=self.onClickNext
        )
        self.nextBTN.grid(row=0, column=1)


    def onClickPrev(self):
        if self.table_body.current_page_num > 0:
            self.table_body.current_page_num -= 1
            # print("table prev")
            self.after_idle(self.table_body.displayCurrentTablePage)
        

    def onClickNext(self):
        if self.table_body.current_page_num < len(self.table_body.current_filter_pages) - 1:
            self.table_body.current_page_num += 1
            # print("table next")
            self.after_idle(self.table_body.displayCurrentTablePage)
