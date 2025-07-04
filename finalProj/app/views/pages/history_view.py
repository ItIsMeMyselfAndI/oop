# external/built-in modules/libs
import customtkinter as ctk
from typing import Dict, List
# our modules/libs
from backend import Transaction
from views.styles import BaseStyles, HistoryStyles # paddings, dimensions, colors, etc
from views.widgets.table import TransactionTableFilters, TransactionTableHeader, TransactionTableBody, TransactionTableNavigation

from backend import Transaction
from models import HistoryPageModel


#--------------------------------------------------------------------------------------------------------


class HistoryPageView(ctk.CTkFrame):
    def __init__(self, model: HistoryPageModel, master, **kwargs):
        super().__init__(master, **kwargs)
        self.model = model


    def create(self):
        print("\n[DEBUG] creating history page...")
        self._create_header()
        self._create_table()
        print("[DEBUG] history page created successfully")
        

    def _create_header(self):
        print("[DEBUG] creating header...")
        self.header = Header(
            master=self,
            fg_color=HistoryStyles.HEADER_SECTION_FG_COLOR,
            corner_radius=BaseStyles.RAD_2
        )
        self.header.pack(pady=(BaseStyles.PAD_5+BaseStyles.PAD_5,0))
        self.update_idletasks()
        print("[DEBUG] header created successfully")


    def _create_table(self):
        print("[DEBUG] creating table...")
        transactions_per_filter: Dict[str, List[Transaction]] = self.model.load_transactions_per_filter()
        self.table = TransactionTable(
            transactions_per_filter=transactions_per_filter,
            filter_master=self.header,
            master=self,
            fg_color=HistoryStyles.TABLE_SECTION_FG_COLOR
        )
        self.table.pack(padx=BaseStyles.PAD_3, pady=(BaseStyles.PAD_2,0))
        self.update_idletasks()
        print("[DEBUG] table created successfully")


#--------------------------------------------------------------------------------------------------------


class Header(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font6 = ("Arial", BaseStyles.FONT_SIZE_6, "bold")
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


class TransactionTable(ctk.CTkFrame):
    def __init__(self, transactions_per_filter, filter_master, master, **kwargs):
        super().__init__(master, **kwargs)

        self.create(transactions_per_filter, filter_master)


    def create(self, transactions_per_filter, filter_master):
        self._create_header()
        self._create_body(transactions_per_filter)
        self._create_nav()
        self._create_filters(filter_master)


    def _create_header(self):
        print("[DEBUG] creating table header...")
        self.header = TransactionTableHeader(
            master=self,
            corner_radius=BaseStyles.RAD_2,
            fg_color=HistoryStyles.TABLE_HEADER_FG_COLOR
        )
        self.header.pack(pady=(0,BaseStyles.PAD_1))
        self.update_idletasks()
        print("[DEBUG] table header created successfully")
        
    
    def _create_body(self, transactions_per_filter):
        print("[DEBUG] creating table body...")
        self.body = TransactionTableBody(
            init_filter_type="All Types",
            transactions_per_filter=transactions_per_filter,
            master=self,
            fg_color=HistoryStyles.TABLE_BODY_FG_COLOR,
            orientation="vertical",
            corner_radius=BaseStyles.RAD_2,
            height=HistoryStyles.TABLE_BODY_H,
            width=HistoryStyles.TABLE_BODY_W,
        )
        self.body.pack()
        self.update_idletasks()
        print("[DEBUG] table body created successfully")
        
        
    def _create_nav(self):
        print("[DEBUG] creating table navigation...")
        self.nav = TransactionTableNavigation(
            table_body=self.body,
            master=self,
            fg_color=HistoryStyles.TABLE_NAV_FG_COLOR
        )
        self.nav.pack(pady=(BaseStyles.PAD_1,0))
        self.update_idletasks()
        print("[DEBUG] table navigation created successfully")

    
    def _create_filters(self, filter_master):
        print("[DEBUG] creating table filters...")
        self.filters = TransactionTableFilters(
            table_body=self.body,
            table_nav=self.nav,
            master=filter_master,
            fg_color=HistoryStyles.FILTERS_FRAME_FG_COLOR
        )
        self.filters.grid(row=0, column=1, padx=(0, BaseStyles.PAD_2), pady=(0,BaseStyles.PAD_2), sticky="s")
        self.update_idletasks()
        print("[DEBUG] table filters created successfully")
