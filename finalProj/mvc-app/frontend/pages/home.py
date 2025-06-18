# external/built-in modules/libs
import customtkinter as ctk
from PIL import Image
import os
import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from typing import List, Dict, Tuple
# our modules/libs
from frontend.styles import BaseStyles, HomeStyles # paddings, dimensions, colors, etc
from frontend.components import TransactionTableHeader, TransactionTableBody 

from backend import Transaction, TransactionManager # db manager

from models.base_model import Model
from controllers.base_controller import Controller


#--------------------------------------------------------------------------------------------------------


class HomePageModel(Model):
    def __init__(self, transaction_manager: TransactionManager, user_id_var: ctk.StringVar):
        self.initialize_managers(transaction_manager)
        self.initialize_vars(user_id_var)

        self.is_current_page = False
        self.balance_amount = 0


    def initialize_managers(self, transaction_manager: TransactionManager):
        self.t_man = transaction_manager
    

    def initialize_vars(self, user_id_var: ctk.StringVar):
        self.user_id_var = user_id_var


    def load_amounts(self):
        self.finance = self.t_man.calculateOverallFinance(self.user_id_var.get())
        self.balance = self.t_man.calculateOverallBalance(self.finance)
    
    
    def load_transactions_per_filter(self) -> Dict[str, List[Transaction]]:
        print("\n[DEBUG] loading transactions per filter...")
        transactions_per_filter = {
            "Recent": self.t_man.repo.getRecentTransactions(user_id=self.user_id_var.get(), t_count=10)
        }
        print("\n[DEBUG] transactions per filter loaded successfully...")
        return transactions_per_filter


#--------------------------------------------------------------------------------------------------------


class HomePageView(ctk.CTkFrame):
    def __init__(self, model: Model, master, **kwargs):
        super().__init__(master, **kwargs)
        self.model = model


    def create(self):
        print("\n[DEBUG] creating home page...")
        self.model.load_amounts()
        self._load_icon()
        self._create_scrollable_frame()
        self._create_header()
        self._create_recent_table()
        self._create_monthly_report()
        self._create_quarterly_report()
        self.update_idletasks()
        print("[DEBUG] home page created successfully")


    def _load_icon(self):
        print("[DEBUG] loading home page icon...")
        # icon path
        if hasattr(sys, "_MEIPASS"): # # for .exe: memory resources path
            ICONS_FOLDER = os.path.join(sys._MEIPASS, "assets/icons")
        else: # for .py: storage resources path
            ICONS_FOLDER = "assets/icons"
        print(ICONS_FOLDER)
        
        # load icon
        self.home_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "home1.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "home1.png")),
            size=(HomeStyles.HOME_IMG_H, HomeStyles.HOME_IMG_W)
        )
        print("[DEBUG] home page icon loaded successfully")


    def _create_scrollable_frame(self):
        print("[DEBUG] creating scrollable frame...")
        self.scroll_frame = ctk.CTkScrollableFrame(
            master=self,
            orientation="vertical",
            corner_radius=0,
            fg_color=HomeStyles.SCROLL_FRAME_FG_COLOR,
            width=HomeStyles.SCROLL_FRAME_W,
            height=HomeStyles.SCROLL_FRAME_H
        )
        self.scroll_frame.pack()
        self.update_idletasks()
        print("[DEBUG] scrollable frame created successfully")


    def _create_header(self):
        print("[DEBUG] creating header...")
        self.header = Header(
            img=self.home_icon,
            summary_type="Total Balance:",
            amount=self.model.balance,
            master=self.scroll_frame,
            fg_color=HomeStyles.HEADER_SECTION_FG_COLOR,
            corner_radius=BaseStyles.RAD_2
        )
        self.header.pack(pady=(BaseStyles.PAD_5*2,0))
        self.update_idletasks()
        print("[DEBUG] header created successfully")


    def _create_recent_table(self):
        print("[DEBUG] creating recent transactions table...")
        transactions_per_filter = self.model.load_transactions_per_filter()
        self.recent_table = RecentTable(
            transactions_per_filter=transactions_per_filter,
            master=self.scroll_frame,
            fg_color=HomeStyles.TABLE_SECTION_FG_COLOR
        )
        self.recent_table.pack(pady=(BaseStyles.PAD_2,0))
        self.update_idletasks()
        print("[DEBUG] recent transactions table created successfully")


    def _create_monthly_report(self):
        print("[DEBUG] creating monthly report...")
        self.monthly_report = MonthlyReport(
            model=self.model,
            master=self.scroll_frame,
            fg_color=HomeStyles.MONTHLY_SECTION_FG_COLOR
        )
        self.monthly_report.pack(pady=(BaseStyles.PAD_2,0))
        self.update_idletasks()
        print("[DEBUG] monthly report created successfully")

    
    def _create_quarterly_report(self):
        print("[DEBUG] creating quarterly report...")
        self.quarterly_report = QuarterlyReport(
            model=self.model,
            master=self.scroll_frame,
            fg_color=HomeStyles.QUARTERLY_SECTION_FG_COLOR
        )
        self.quarterly_report.pack(pady=(BaseStyles.PAD_2,BaseStyles.PAD_5*3))
        self.update_idletasks()
        print("[DEBUG] quarterly report created successfully")


#--------------------------------------------------------------------------------------------------------


class HomePageController(Controller):
    def __init__(self, transaction_manager: TransactionManager, user_id_var: ctk.StringVar, master):
        self.model = HomePageModel(transaction_manager=transaction_manager, user_id_var=user_id_var)
        self.view = HomePageView(model=self.model, master=master, fg_color=HomeStyles.SCROLL_FRAME_FG_COLOR)


    def run(self):
        pass


    def update_display(self):
        print("\n[DEBUG] updating home page display...")
        # update total balance in header
        self.model.load_amounts()
        self.view.header.amount_label.configure(text=f"₱ {self.model.balance:,}")
        
        self._update_table()
        self._update_monthly_report()
        self._update_quarterly_report()
        print("[DEBUG] home page display updated successfully")

    
    def _update_table(self):
        print("[DEBUG] updating recent transaction table...")
        # destroy prev ver of the table
        for page in self.view.recent_table.body.winfo_children():
            page.destroy()

        self.view.recent_table.body.transactions_per_filter = self.model.load_transactions_per_filter()
        self.view.recent_table.body.filterTransactions()
        self.view.recent_table.body.countFilteredTablePages()
        self.view.recent_table.body.separateFilteredTransactionsPerPage()
        self.view.recent_table.body.updateCurrentTablePage()
        self.view.update_idletasks()
        print("[DEBUG] recent transaction table updated successfully")

    
    def _update_monthly_report(self):
        print("[DEBUG] updating monthly report graphs...")
        self.view.monthly_report.income_canvas.get_tk_widget().destroy()
        self.view.monthly_report.expense_canvas.get_tk_widget().destroy()
        self.view.monthly_report.income_canvas, self.view.monthly_report.expense_canvas = self.view.monthly_report.display_graphs_section()
        self.view.update_idletasks()
        print("[DEBUG] monthly report graphs updated successfully")

    
    def _update_quarterly_report(self):
        print("[DEBUG] updating quarterly report graph...")
        self.view.quarterly_report.graph_canvas.get_tk_widget().destroy()
        self.view.quarterly_report.graph_canvas = self.view.quarterly_report.display_graphs_section()
        self.view.update_idletasks()
        print("[DEBUG] quarterly report graph updated successfully")



#--------------------------------------------------------------------------------------------------------


class Header(ctk.CTkFrame):
    def __init__(self, img, summary_type, amount, master, **kwargs):
        super().__init__(master, ** kwargs)
        self.font4 = ("Arial", BaseStyles.FONT_SIZE_4, "normal")
        self.font6 = ("Arial", BaseStyles.FONT_SIZE_6, "normal")

        self.create(img, summary_type, amount)


    def create(self, img:Image, summary_type: str, amount: float):
        self._create_icon(img)
        self._create_balance(summary_type, amount)


    def _create_icon(self, img: Image):
        print("[DEBUG] creating icon...")
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
        self.update_idletasks()
        print("[DEBUG] icon created successfully")


    def _create_balance(self, summary_type: str, amount: float): 
        print("[DEBUG] creating balance...")
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
        self.update_idletasks()
        print("[DEBUG] balance created successfully")


#--------------------------------------------------------------------------------------------------------


class RecentTable(ctk.CTkFrame):
    def __init__(self, transactions_per_filter: Dict[str, List[Transaction]], master, **kwargs):
        super().__init__(master, **kwargs)
        # initialize font
        self.font4 = ("Arial", BaseStyles.FONT_SIZE_4, "normal")

        self.create(title_master=master, transactions_per_filter=transactions_per_filter)


    def create(self, title_master, transactions_per_filter: Dict[str, List[Transaction]]):
        self._create_title(title_master)
        self._create_header()
        self._create_body(transactions_per_filter)
        
        
    def _create_title(self, title_master):
        print("[DEBUG] creating table title...")
        self.title = ctk.CTkLabel(
            master=title_master,
            text="Recent Transactions",
            font=self.font4,
            corner_radius=BaseStyles.RAD_2,
            text_color=HomeStyles.TABLE_TITLE_TEXT_COLOR,
            fg_color=HomeStyles.TABLE_TITLE_SECTION_FG_COLOR,
            width=HomeStyles.TABLE_TITLE_SECTION_W,
            height=HomeStyles.TABLE_TITLE_SECTION_H
        )
        self.title.pack(pady=(BaseStyles.PAD_2, 0))
        self.update_idletasks()
        print("[DEBUG] table title created successfully")
        
    
    def _create_header(self):
        print("[DEBUG] creating table header...")
        self.header = TransactionTableHeader(
            master=self,
            corner_radius=BaseStyles.RAD_2,
            fg_color=HomeStyles.TABLE_HEADER_FG_COLOR
        )
        self.header.pack(pady=(0,BaseStyles.PAD_1))
        self.update_idletasks()
        print("[DEBUG] table header created successfully")
        
    
    def _create_body(self, transactions_per_filter):
        print("[DEBUG] creating table body...")
        self.body = TransactionTableBody(
            init_filter_type="Recent",
            transactions_per_filter=transactions_per_filter,
            master=self,
            fg_color=HomeStyles.TABLE_BODY_FG_COLOR,
            orientation="vertical",
            corner_radius=BaseStyles.RAD_2,
            height=HomeStyles.TABLE_BODY_H,
            width=HomeStyles.TABLE_BODY_W
        )
        self.body.pack()
        self.update_idletasks()
        print("[DEBUG] table body created successfully")


#--------------------------------------------------------------------------------------------------------


class MonthlyReport(ctk.CTkFrame):
    def __init__(self, model, master, **kwargs):
        super().__init__(master, **kwargs)
        self.model = model
        
        # initialize font
        self.font3 = ("Arial", BaseStyles.FONT_SIZE_3, "normal")
        self.font4 = ("Arial", BaseStyles.FONT_SIZE_4, "normal")

        self.create()


    def create(self):
        self._create_title()
        self._create_graphs()

    
    def _create_title(self):
        print("[DEBUG] creating monthly title...")
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
        self.update_idletasks()
        print("[DEBUG] monthly title created successfully")


    def _create_graphs(self):
        print("[DEBUG] creating monthly graphs...")
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
        self.income_canvas, self.expense_canvas = self.display_graphs_section()
        self.update_idletasks()
        print("[DEBUG] monthly graphs created successfully")
        
    
    def display_graphs_section(self) -> Tuple[FigureCanvasTkAgg, FigureCanvasTkAgg]:
        print("[DEBUG] displaying monthly graphs...")
        # graph figures
        income_graph, expense_graph = self.model.t_man.createMonthlyGraphs(
            user_id=self.model.user_id_var.get(),
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
        self.update_idletasks()
        print("[DEBUG] monthly graphs displayed successfully")
        
        return income_canvas, expense_canvas
    

#--------------------------------------------------------------------------------------------------------


class QuarterlyReport(ctk.CTkFrame):
    def __init__(self, model, master, **kwargs):
        super().__init__(master, **kwargs)
        self.model = model
        
        # initialize font
        self.font3 = ("Arial", BaseStyles.FONT_SIZE_3, "normal")
        self.font4 = ("Arial", BaseStyles.FONT_SIZE_4, "normal")

        self.create()


    def create(self):
        self._create_title()
        self._create_graphs()

    
    def _create_title(self):
        print("[DEBUG] creating quarterly title...")
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
        self.update_idletasks()
        print("[DEBUG] quarterly title created successfully")


    def _create_graphs(self):
        print("[DEBUG] creating quarterly graphs...")
        self.graph_section = ctk.CTkFrame(
            master=self,
            fg_color=HomeStyles.QUARTERLY_GRAPHS_SECTION_FG_COLOR,
            corner_radius=BaseStyles.RAD_2,
        )
        self.graph_section.pack()
        self.graph_canvas = self.display_graphs_section()
        self.update_idletasks()
        print("[DEBUG] quarterly graphs created successfully")
        
        
    def display_graphs_section(self) -> FigureCanvasTkAgg:
        print("[DEBUG] displaying quarterly graphs...")
        # graph figure
        graph = self.model.t_man.createQuarterlyGraph(
            user_id=self.model.user_id_var.get(),
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
        self.update_idletasks()
        print("[DEBUG] quarterly graphs displayed successfully")
        
        return graph_canvas
    
