# external/built-in modules/libs
import customtkinter as ctk
from typing import Dict, List
# our modules/libs
from backend import Transaction
from frontend.styles import BaseStyles, HistoryStyles # paddings, dimensions, colors, etc
from frontend.components import TransactionTableFilters, TransactionTableHeader, TransactionTableBody, TransactionTableNavigation


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


class TransactionTable(ctk.CTkFrame):
    def __init__(self, transactions_per_filter, header_section, master, **kwargs):
        super().__init__(master, **kwargs)
        # header
        self.table_header = TransactionTableHeader(
            master=self,
            corner_radius=BaseStyles.RAD_2,
            fg_color=HistoryStyles.TABLE_HEADER_FG_COLOR
        )
        self.table_header.pack(pady=(0,BaseStyles.PAD_1))
        
        # body
        self.table_body = TransactionTableBody(
            init_filter_type="All Types",
            transactions_per_filter=transactions_per_filter,
            master=self,
            fg_color=HistoryStyles.TABLE_BODY_FG_COLOR,
            orientation="vertical",
            corner_radius=BaseStyles.RAD_2,
            height=HistoryStyles.TABLE_BODY_H,
            width=HistoryStyles.TABLE_BODY_W,
        )
        self.table_body.pack()
        
        # navigation buttons
        self.table_nav = TransactionTableNavigation(
            table_body=self.table_body,
            master=self,
            fg_color=HistoryStyles.TABLE_NAV_FG_COLOR
        )
        self.table_nav.pack(pady=(BaseStyles.PAD_1,0))

        # filters
        self.filters = TransactionTableFilters(
            table_body=self.table_body,
            table_nav=self.table_nav,
            master=header_section,
            fg_color=HistoryStyles.FILTERS_FRAME_FG_COLOR
        )
        self.filters.grid(row=0, column=1, padx=(0, BaseStyles.PAD_2), pady=(0,BaseStyles.PAD_2), sticky="s")
        

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
        transactions_per_filter = self.loadTransactionsPerFilter()
        self.table_section = TransactionTable(
            transactions_per_filter=transactions_per_filter,
            header_section=self.header_section,
            master=self,
            fg_color=HistoryStyles.TABLE_SECTION_FG_COLOR
        )
        self.table_section.pack(padx=BaseStyles.PAD_3, pady=(BaseStyles.PAD_2,0))


    def loadTransactionsPerFilter(self) -> Dict[str, List[Transaction]]:
        transactions_per_filter = {
            "All Types": self.tm.repo.getAllTransactions(self.app.user_id),
            "Income": self.tm.repo.getTransactionsByType(self.app.user_id, "income"),
            "Savings": self.tm.repo.getTransactionsByType(self.app.user_id, "savings"),
            "Expenses": self.tm.repo.getTransactionsByType(self.app.user_id, "expense"),
            "Investment": self.tm.repo.getTransactionsByType(self.app.user_id, "investment"),
            # income
            "Salary":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Salary"),
            "Bonus":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Bonus"),
            "Side-hustles":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Side-hustles"),
            "Tips":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Tips"),
            # expenses
            "Bills":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Bills"),
            "Education":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Education"),
            "Entertainment":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Entertainment"),
            "Food & Drinks":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Food & Drinks"),
            "Grocery":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Grocery"),
            "Healthcare":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Healthcare"),
            "House":self.tm.repo.getTransactionsByCategory(self.app.user_id, "House"),
            "Shopping":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Shopping"),
            "Transportation":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Transportation"),
            "Wellness":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Wellness"),
            "Other":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Other"),
            # savings
            "Monthly Allowance":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Monthly Allowance"),
            "Change":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Change"),
            "Miscellaneous":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Miscellaneous"),
            # investment
            "Stocks":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Stocks"),
            "Crypto":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Crypto"),
            "Bonds":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Bonds"),
            "Real Estate":self.tm.repo.getTransactionsByCategory(self.app.user_id, "Real Estate")
        }
        return transactions_per_filter

    
    def updatePageDisplay(self):
        # refresh history content
        self.table_section.table_body.transactions_per_filter = self.loadTransactionsPerFilter()
        self.table_section.table_body.filterTransactions()
        self.table_section.table_body.countFilteredTablePages()
        self.table_section.table_body.separateFilteredTransactionsPerPage()
        self.table_section.table_body.updateCurrentTablePage()
        self.table_section.table_nav._updatePageNumberDisplay()
