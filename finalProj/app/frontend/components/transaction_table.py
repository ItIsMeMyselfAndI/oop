# external/built-in modules/libs
import customtkinter as ctk
from typing import Dict, List
# our modules/libs
from frontend.styles import BaseStyles, TransactionTableStyles # paddings, dimensions, colors, etc


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
    def __init__(self, transactions_per_filter, master, has_filter, **kwargs):
        super().__init__(master, **kwargs)
        self.has_filter = has_filter

        self.current_page_num = 0
        self.initializeTableBodyContent(transactions_per_filter)

        # display default table page
        self.displayCurrentTablePage()


    def initializeTableBodyContent(self, transactions_per_filter):
        self.pages_per_filter = self.createTablePagesPerFilter(transactions_per_filter=transactions_per_filter)
        if self.has_filter:
            self.current_table_pages = self.pages_per_filter["All Types"]
        else:
            self.current_table_pages = list(self.pages_per_filter.values())[0]


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


    def _layoutRow(self, row):
        row.date_col.grid(row=0, column=0, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
        row.type_col.grid(row=0, column=1, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
        row.category_col.grid(row=0, column=2, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
        row.description_col.grid(row=0, column=3, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
        row.amount_col.grid(row=0, column=4, padx=(0,BaseStyles.PAD_2), pady=0, sticky="nw")
        row.pack(pady=(0,BaseStyles.PAD_1))


    def displayCurrentTablePage(self):
        self.after_idle(self._hideAllTablePages)

        # show rows in current page
        if self.current_table_pages:
            page_frame = list(self.current_table_pages)[self.current_page_num]

            for row in page_frame.winfo_children():
                self.after_idle(self._layoutRow, row)
            self.after_idle(page_frame.pack)


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
            command=self.onClickPrev,
        )
        self.prevBTN.grid(row=0, column=0, padx=(0,BaseStyles.PAD_1))

        # page number display
        self.page_num_label = ctk.CTkLabel(
            master=self,
            corner_radius=BaseStyles.RAD_2,
            font=self.font1,
            text=f"{self.table_body.current_page_num+1}/{len(self.table_body.current_table_pages)}",
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
            text_color=TransactionTableStyles.NAV_NEXT_BUTTON_TEXT_COLOR,
            fg_color=TransactionTableStyles.NAV_NEXT_BUTTON_FG_COLOR,
            hover_color=TransactionTableStyles.NAV_NEXT_BUTTON_HOVER_COLOR,
            width=TransactionTableStyles.TABLE_NAV_BTN_W,
            height=TransactionTableStyles.TABLE_NAV_BTN_H,
            font=self.font1,
            corner_radius=BaseStyles.RAD_2,
            command=self.onClickNext
        )
        self.nextBTN.grid(row=0, column=2)
        
        # disable table navigation if in first and last page
        self.prevBTN.configure(fg_color=TransactionTableStyles.NAV_PREV_BUTTON_HOVER_COLOR)
        if len(self.table_body.current_table_pages) in [0, 1]:
            self.nextBTN.configure(fg_color=TransactionTableStyles.NAV_NEXT_BUTTON_HOVER_COLOR)
        else:
            self.nextBTN.configure(fg_color=TransactionTableStyles.NAV_NEXT_BUTTON_FG_COLOR)


    def onClickPrev(self):
        if self.table_body.current_page_num > 0:
            self.table_body.current_page_num -= 1
            # print("table prev")
            self.after_idle(self.table_body.displayCurrentTablePage)

            # enable next button
            self.nextBTN.configure(fg_color=TransactionTableStyles.NAV_NEXT_BUTTON_FG_COLOR)

            # disable previous button if in first page
            if self.table_body.current_page_num == 0:
                self.prevBTN.configure(fg_color=TransactionTableStyles.NAV_PREV_BUTTON_HOVER_COLOR)
            
            # update page number display
            if not len(self.table_body.current_table_pages):
                self.page_num_label.configure(text="0/0")
            else:
                self.page_num_label.configure(text=f"{self.table_body.current_page_num+1}/{len(self.table_body.current_table_pages)}")
        

    def onClickNext(self):
        if self.table_body.current_page_num < len(self.table_body.current_table_pages) - 1:
            self.table_body.current_page_num += 1
            # print("table next")
            self.after_idle(self.table_body.displayCurrentTablePage)

            # enable previous button
            self.prevBTN.configure(fg_color=TransactionTableStyles.NAV_PREV_BUTTON_FG_COLOR)

            # disable next button if in last page
            if self.table_body.current_page_num == len(self.table_body.current_table_pages) - 1:
                self.nextBTN.configure(fg_color=TransactionTableStyles.NAV_NEXT_BUTTON_HOVER_COLOR)
            
            # update page number display
            if not len(self.table_body.current_table_pages):
                self.page_num_label.configure(text="0/0")
            else:
                self.page_num_label.configure(text=f"{self.table_body.current_page_num+1}/{len(self.table_body.current_table_pages)}")


    def disableNextIfOnlyOneTablePage(self):
        if len(self.table_body.current_table_pages) == 1:
            self.nextBTN.configure(state="disabled")


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
        # set new table page base on filter
        self.table_body.current_table_pages = self.table_body.pages_per_filter[filter_type]
        # reset page num
        self.table_body.current_page_num = 0
        # display current table page
        self.table_body.displayCurrentTablePage()

    
    def _disableTableNavigation(self):
        # disable table navigation if in first and last page
        self.table_nav.prevBTN.configure(fg_color=TransactionTableStyles.NAV_PREV_BUTTON_HOVER_COLOR)
        if len(self.table_body.current_table_pages) in [0, 1]:
            self.table_nav.nextBTN.configure(fg_color=TransactionTableStyles.NAV_NEXT_BUTTON_HOVER_COLOR)
        else:
            self.table_nav.nextBTN.configure(fg_color=TransactionTableStyles.NAV_NEXT_BUTTON_FG_COLOR)
        
        # update page number display
        if not len(self.table_body.current_table_pages):
            self.table_nav.page_num_label.configure(text="0/0")
        else:
            self.table_nav.page_num_label.configure(text=f"{self.table_body.current_page_num+1}/{len(self.table_body.current_table_pages)}")


    def _updateCategoryMenuByType(self, t_type):
        if t_type == "All Types":
            self.current_categories = self.all_categories
        else:
            self.current_categories = self.categories_by_type[t_type]
        self.category_menu.configure(values=self.current_categories)
        self.category_menu.set(self.current_categories[0])
    

    def onPickType(self, t_type):
        self.after_idle(self._filterRows, t_type)
        self.after_idle(self._disableTableNavigation)
        self.after_idle(self._updateCategoryMenuByType, t_type)


    def onPickCategories(self, t_categories):
        self.after_idle(self._filterRows, t_categories)
        self.after_idle(self._disableTableNavigation)

