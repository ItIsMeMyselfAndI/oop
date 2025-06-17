# external/built-in modules/libs
import customtkinter as ctk
from PIL import Image
import os
import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# our modules/libs
from frontend.styles import BaseStyles, HomeStyles # paddings, dimensions, colors, etc
from frontend.components import TransactionTableHeader, TransactionTableBody 


#--------------------------------------------------------------------------------------------------------


class HomeHeader(ctk.CTkFrame):
    def __init__(self, img, summary_type, amount, master, **kwargs):
        super().__init__(master, ** kwargs)
        self.font4 = ("Bodoni MT", BaseStyles.FONT_SIZE_4, "italic")
        self.font6 = ("Bodoni MT", BaseStyles.FONT_SIZE_6, "italic")

        # home icon
        self.img = img
        self.img_bg = ctk.CTkLabel(
            master=self,
            corner_radius=0,
            image=img,
            text="",
            fg_color=HomeStyles.HOME_IMG_BG_COLOR,
            width=HomeStyles.HOME_IMG_BG_W,
            height=HomeStyles.HOME_IMG_BG_H
        )
        self.img_bg.grid(row=0, column=1, pady=BaseStyles.PAD_3, padx=BaseStyles.PAD_3, sticky="e")
        
        # balance summary
        self.balance_frame = ctk.CTkFrame(
            master=self,
            corner_radius=0,
            fg_color=HomeStyles.BALANCE_FRAME_FG_COLOR
        )
        self.balance_title_label = ctk.CTkLabel(
            master=self.balance_frame,
            text=summary_type,
            font=self.font4,
            text_color=HomeStyles.BALANCE_TITLE_TEXT_COLOR,
            fg_color=HomeStyles.BALANCE_TITLE_LABEL_FG_COLOR,
            anchor="w"
        )
        self.amount_label = ctk.CTkLabel(
            master=self.balance_frame,
            text=f"₱ {amount:,}",
            font=self.font6,
            text_color=HomeStyles.BALANCE_AMOUNT_TEXT_COLOR,
            width=HomeStyles.BALANCE_AMOUNT_LABEL_W,
            wraplength=HomeStyles.BALANCE_AMOUNT_LABEL_W,
            fg_color=HomeStyles.BALANCE_AMOUNT_LABEL_FG_COLOR,
            anchor="w",
            justify="left"
        )
        self.balance_frame.grid(row=0, column=0, padx=(BaseStyles.PAD_4,0))
        self.balance_title_label.pack(anchor="w")
        self.amount_label.pack(anchor="w")


#--------------------------------------------------------------------------------------------------------


class RecentTable(ctk.CTkFrame):
    def __init__(self, transactions_per_filter, master, **kwargs):
        super().__init__(master, **kwargs)
        # initialize font
        self.font4 = ("Bodoni MT", BaseStyles.FONT_SIZE_4, "italic")
        
        # title
        self.table_title = ctk.CTkLabel(
            master=master,
            text="Recent Transactions",
            font=self.font4,
            corner_radius=BaseStyles.RAD_2,
            text_color=HomeStyles.TABLE_TITLE_TEXT_COLOR,
            fg_color=HomeStyles.TABLE_TITLE_SECTION_FG_COLOR,
            width=HomeStyles.TABLE_TITLE_SECTION_W,
            height=HomeStyles.TABLE_TITLE_SECTION_H
        )
        self.table_title.pack(pady=(BaseStyles.PAD_2, 0))
        
        # header
        self.table_header = TransactionTableHeader(
            master=self,
            corner_radius=BaseStyles.RAD_2,
            fg_color=HomeStyles.TABLE_HEADER_FG_COLOR
        )
        self.table_header.pack(pady=(0,BaseStyles.PAD_1))
        
        # header
        self.table_body = TransactionTableBody(
            init_filter_type="Recent",
            transactions_per_filter=transactions_per_filter,
            master=self,
            fg_color=HomeStyles.TABLE_BODY_FG_COLOR,
            orientation="vertical",
            corner_radius=BaseStyles.RAD_2,
            height=HomeStyles.TABLE_BODY_H,
            width=HomeStyles.TABLE_BODY_W
        )
        self.table_body.pack()


#--------------------------------------------------------------------------------------------------------


class MonthlyReport(ctk.CTkFrame):
    def __init__(self, app, t_man, master, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app
        self.t_man = t_man
        
        # initialize font
        self.font3 = ("Bodoni MT", BaseStyles.FONT_SIZE_3, "italic")
        self.font4 = ("Bodoni MT", BaseStyles.FONT_SIZE_4, "italic")

        # title
        self.title_section = ctk.CTkLabel(
            master=self,
            text="Monthly Report",
            corner_radius=BaseStyles.RAD_2,
            font=self.font4,
            text_color=HomeStyles.MONTHLY_TITLE_TEXT_COLOR,
            fg_color=HomeStyles.MONTHLY_TITLE_SECTION_FG_COLOR,
            width=HomeStyles.MONTHLY_TITLE_SECTION_W,
            height=HomeStyles.MONTHLY_TITLE_SECTION_H
        )
        self.title_section.pack(pady=(0,BaseStyles.PAD_2))

        # graphs sections
        self.graphs_section = ctk.CTkFrame(
            master=self,
            fg_color=HomeStyles.MONTHLY_GRAPHS_SECTION_FG_COLOR
        )
        self.graphs_section.pack()

        # income section
        self.income_frame = ctk.CTkFrame(
            master=self.graphs_section,
            fg_color=HomeStyles.MONTHLY_INCOME_GRAPH_FRAME_FG_COLOR,
            corner_radius=BaseStyles.RAD_2
        )
        self.income_frame.grid(row=0, column=0, padx=(0,BaseStyles.PAD_2))

        # expense section
        self.expense_frame = ctk.CTkFrame(
            master=self.graphs_section,
            fg_color=HomeStyles.MONTHLY_EXPENSE_GRAPH_FRAME_FG_COLOR,
            corner_radius=BaseStyles.RAD_2
        )
        self.expense_frame.grid(row=0, column=1)

        # graphs
        self.income_canvas, self.expense_canvas = self.loadAndDisplayGraphsWidget()
        
    
    def loadAndDisplayGraphsWidget(self):
        # graph figures
        income_graph, expense_graph = self.t_man.createMonthlyGraphs(
            user_id=self.app.user_id,
            title_size=HomeStyles.MONTHLY_GRAPH_TITLE_SIZE,
            label_size=HomeStyles.MONTHLY_GRAPH_LABEL_SIZE,
            dpi=BaseStyles.DPI,
            width_in=HomeStyles.MONTHLY_GRAPH_W_IN,
            height_in=HomeStyles.MONTHLY_GRAPH_H_IN
        )

        # income graph widget
        income_canvas = FigureCanvasTkAgg(figure=income_graph, master=self.income_frame)
        income_canvas.draw()
        income_canvas.get_tk_widget().pack(padx=BaseStyles.PAD_1, pady=BaseStyles.PAD_1)
        
        # expense graph widget
        expense_canvas = FigureCanvasTkAgg(figure=expense_graph, master=self.expense_frame)
        expense_canvas.draw()
        expense_canvas.get_tk_widget().pack(padx=BaseStyles.PAD_1, pady=BaseStyles.PAD_1)
        
        return income_canvas, expense_canvas
    

    def updateGraphsDisplay(self):
        self.income_canvas.get_tk_widget().destroy()
        self.expense_canvas.get_tk_widget().destroy()
        self.income_canvas, self.expense_canvas = self.loadAndDisplayGraphsWidget()


#--------------------------------------------------------------------------------------------------------


class QuarterlyReport(ctk.CTkFrame):
    def __init__(self, app, t_man, master, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app
        self.t_man = t_man
        
        # initialize font
        self.font3 = ("Bodoni MT", BaseStyles.FONT_SIZE_3, "italic")
        self.font4 = ("Bodoni MT", BaseStyles.FONT_SIZE_4, "italic")
        
        # title
        self.title_section = ctk.CTkLabel(
            master=self,
            text="Quarterly Report",
            font=self.font4,
            corner_radius=BaseStyles.RAD_2,
            text_color=HomeStyles.QUARTERLY_TITLE_TEXT_COLOR,
            fg_color=HomeStyles.QUARTERLY_TITLE_SECTION_FG_COLOR,
            width=HomeStyles.QUARTERLY_TITLE_SECTION_W,
            height=HomeStyles.QUARTERLY_TITLE_SECTION_H
        )
        self.title_section.pack(pady=(0,BaseStyles.PAD_2))
        
        self.graph_section = ctk.CTkFrame(
            master=self,
            fg_color=HomeStyles.QUARTERLY_GRAPHS_SECTION_FG_COLOR,
            corner_radius=BaseStyles.RAD_2,
        )
        self.graph_section.pack()
        self.graph_canvas = self.loadAndDisplayGraphWidget()
        
        
    def loadAndDisplayGraphWidget(self):
        # graph figure
        graph = self.t_man.createQuarterlyGraph(
            user_id=self.app.user_id,
            title_size=HomeStyles.QUARTERLY_GRAPH_TITLE_SIZE,
            label_size=HomeStyles.QUARTERLY_GRAPH_LABEL_SIZE,
            dpi=BaseStyles.DPI,
            width_in=HomeStyles.QUARTERLY_GRAPH_W_IN,
            height_in=HomeStyles.QUARTERLY_GRAPH_H_IN
        )

        # graph widget
        graph_canvas = FigureCanvasTkAgg(figure=graph, master=self.graph_section)
        graph_canvas.draw()
        graph_canvas.get_tk_widget().pack(padx=BaseStyles.PAD_1, pady=BaseStyles.PAD_1)
        
        return graph_canvas
    

    def updateGraphDisplay(self):
        self.graph_canvas.get_tk_widget().destroy()
        self.graph_canvas = self.loadAndDisplayGraphWidget()


#--------------------------------------------------------------------------------------------------------


class HomePage(ctk.CTkFrame):
    def __init__(self, app, t_man, master, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app
        self.t_man = t_man

        # initialize state
        self.is_current_page = False

        self.createScrollableFrame()
        self.createHeader()
        self.createTableSection()
        self.createMonthlySection()
        self.createQuarterlySection()

    
    def createScrollableFrame(self):
        self.scroll_frame = ctk.CTkScrollableFrame(
            master=self,
            orientation="vertical",
            corner_radius=0,
            fg_color=HomeStyles.SCROLL_FRAME_FG_COLOR,
            width=HomeStyles.SCROLL_FRAME_W,
            height=HomeStyles.SCROLL_FRAME_H
        )
        self.scroll_frame.pack()


    def _loadOverallBalance(self):
        finance = self.t_man.calculateOverallFinance(self.app.user_id)
        balance = self.t_man.calculateOverallBalance(finance)
        return balance


    def _loadIcon(self):
        # icon path
        if hasattr(sys, "_MEIPASS"): # # for .exe: memory resources path
            ICONS_FOLDER = os.path.join(sys._MEIPASS, "assets/icons")
        else: # for .py: storage resources path
            ICONS_FOLDER = "assets/icons"
        print(ICONS_FOLDER)
        
        # load icon
        home_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "home1.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "home1.png")),
            size=(HomeStyles.HOME_IMG_H, HomeStyles.HOME_IMG_W)
        )
        return home_icon


    def createHeader(self):
        home_icon = self._loadIcon()
        balance = self._loadOverallBalance()
        self.header_section = HomeHeader(
            img=home_icon,
            summary_type="Total Balance:",
            amount=balance,
            master=self.scroll_frame,
            fg_color=HomeStyles.HEADER_SECTION_FG_COLOR,
            corner_radius=BaseStyles.RAD_2
        )
        self.header_section.pack(pady=(BaseStyles.PAD_5*2,0))


    def createTableSection(self):
        transactions_per_filter = {"Recent": self.t_man.repo.getRecentTransactions(user_id=self.app.user_id, t_count=10)}
        self.table_section = RecentTable(
            transactions_per_filter=transactions_per_filter,
            master=self.scroll_frame,
            fg_color=HomeStyles.TABLE_SECTION_FG_COLOR
        )
        self.table_section.pack(pady=(BaseStyles.PAD_2,0))

    
    def createMonthlySection(self):
        self.monthly_section = MonthlyReport(
            app=self.app,
            t_man=self.t_man,
            master=self.scroll_frame,
            fg_color=HomeStyles.MONTHLY_SECTION_FG_COLOR
        )
        self.monthly_section.pack(pady=(BaseStyles.PAD_2,0))

    
    def createQuarterlySection(self):
        self.quarterly_section = QuarterlyReport(
            app=self.app,
            t_man=self.t_man,
            master=self.scroll_frame,
            fg_color=HomeStyles.QUARTERLY_SECTION_FG_COLOR
        )
        self.quarterly_section.pack(pady=(BaseStyles.PAD_2,BaseStyles.PAD_5*3))


    def updatePageDisplay(self):
        # update total balance in header
        balance = self._loadOverallBalance()
        self.header_section.amount_label.configure(text=f"₱ {balance:,}")

        # destroy prev ver of the Recent transactions
        for page in self.table_section.table_body.winfo_children():
            page.destroy()
        
        # refresh history content
        self.table_section.table_body.transactions_per_filter = {"Recent": self.t_man.repo.getRecentTransactions(user_id=self.app.user_id, t_count=10)}
        self.table_section.table_body.filterTransactions()
        self.table_section.table_body.countFilteredTablePages()
        self.table_section.table_body.separateFilteredTransactionsPerPage()
        self.table_section.table_body.updateCurrentTablePage()

        # update graphs 
        self.monthly_section.updateGraphsDisplay()
        self.quarterly_section.updateGraphDisplay()