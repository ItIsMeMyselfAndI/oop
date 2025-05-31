# external/built-in modules/libs
import customtkinter as ctk
from PIL import Image
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# our modules/libs
from frontend.styles import BaseStyles, HomeStyles # paddings, dimensions, colors, etc


class HomeHeader(ctk.CTkFrame):
    def __init__(self, img, summary_type, amount, master, **kwargs):
        super().__init__(master, ** kwargs)
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_4, weight="normal", slant="italic" )
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_6, weight="normal", slant="italic" )
        self.img = img
        # create guide frames
        self.balance_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        self.img_bg = ctk.CTkLabel(self, corner_radius=0, image=img, text="",
                                   width=HomeStyles.IMG_BG_W, height=HomeStyles.IMG_BG_H)
        # create label
        self.summary_type_label = ctk.CTkLabel(self.balance_frame, text=summary_type, font=self.font1,
                                               text_color=BaseStyles.WHITE, anchor="w")
        self.amount_label = ctk.CTkLabel(self.balance_frame, text=f"₱ {amount:,}", font=self.font2,
                                         text_color=BaseStyles.WHITE, width=HomeStyles.LABEL_W,
                                         anchor="w", justify="left")
        # display guide frames
        self.balance_frame.grid(row=0, column=0, padx=(BaseStyles.PAD_4,0))
        self.img_bg.grid(row=0, column=1, pady=BaseStyles.PAD_3, padx=BaseStyles.PAD_3, sticky="e")
        # display labels
        self.summary_type_label.pack(anchor="w")
        self.amount_label.pack(anchor="w")


class TableRow(ctk.CTkFrame):
    def __init__(self, transaction, master, **kwargs):
        super().__init__(master, **kwargs)
        self.t = transaction
        # initialize font
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_2, weight="normal", slant="italic" )
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_4, weight="normal", slant="italic" )
        
        self.date_label = ctk.CTkLabel(self, text=self.t.t_date, font=self.font1,
                                       text_color=BaseStyles.DARK_GREY, fg_color=BaseStyles.WHITE, anchor="w",
                                       width=HomeStyles.TABLE_COL_W1, wraplength=HomeStyles.TABLE_COL_W1, justify="left")
        self.type_label = ctk.CTkLabel(self, text=self.t.t_type, font=self.font1,
                                       text_color=BaseStyles.DARK_GREY, fg_color=BaseStyles.WHITE, anchor="w",
                                       width=HomeStyles.TABLE_COL_W2, wraplength=HomeStyles.TABLE_COL_W2, justify="left")
        self.category_label = ctk.CTkLabel(self, text=self.t.t_category, font=self.font1,
                                           text_color=BaseStyles.DARK_GREY, fg_color=BaseStyles.WHITE, anchor="w",
                                           width=HomeStyles.TABLE_COL_W2, wraplength=HomeStyles.TABLE_COL_W2, justify="left")
        self.description_label = ctk.CTkLabel(self, text=self.t.t_description, font=self.font1,
                                              text_color=BaseStyles.DARK_GREY, fg_color=BaseStyles.WHITE, anchor="w",
                                              width=HomeStyles.TABLE_COL_W3, wraplength=HomeStyles.TABLE_COL_W3, justify="left")
        self.amount_label = ctk.CTkLabel(self, text=f"₱ {self.t.t_amount:,}", font=self.font1,
                                         text_color=BaseStyles.DARK_GREY, fg_color=BaseStyles.WHITE, anchor="e",
                                         width=HomeStyles.TABLE_COL_W3-BaseStyles.PAD_1,
                                         wraplength=HomeStyles.TABLE_COL_W3-BaseStyles.PAD_1,
                                         justify="right")
        

class Table(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize font
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_3, weight="normal", slant="italic" )
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_4, weight="normal", slant="italic" )
        # table sections
        self.title_section = ctk.CTkLabel(self, text="Recent Transactions", text_color=BaseStyles.WHITE,
                                          fg_color=BaseStyles.BLUE, font=self.font2, corner_radius=BaseStyles.RAD_2,
                                          width=HomeStyles.TABLE_TITLE_SECTION_W, height=HomeStyles.TABLE_TITLE_SECTION_H)
        self.table_header = ctk.CTkFrame(self, fg_color=BaseStyles.WHITE, corner_radius=BaseStyles.RAD_2)
        self.table_body = ctk.CTkScrollableFrame(self, fg_color=BaseStyles.WHITE, orientation="vertical", corner_radius=BaseStyles.RAD_2,
                                                 height=HomeStyles.TABLE_BODY_H, width=HomeStyles.TABLE_BODY_W)
        # table header
        self.date_header = ctk.CTkLabel(self.table_header, text="Date", font=self.font1,
                                       text_color=BaseStyles.DARK_GREY, fg_color="transparent", anchor="w",
                                       width=HomeStyles.TABLE_COL_W1, height=HomeStyles.TABLE_ROW_H)
        self.type_header = ctk.CTkLabel(self.table_header, text="Type", font=self.font1,
                                       text_color=BaseStyles.DARK_GREY, fg_color="transparent", anchor="w",
                                       width=HomeStyles.TABLE_COL_W2, height=HomeStyles.TABLE_ROW_H)
        self.category_header = ctk.CTkLabel(self.table_header, text="Category", font=self.font1,
                                       text_color=BaseStyles.DARK_GREY, fg_color="transparent", anchor="w",
                                       width=HomeStyles.TABLE_COL_W2, height=HomeStyles.TABLE_ROW_H)
        self.description_header = ctk.CTkLabel(self.table_header, text="Description", font=self.font1,
                                       text_color=BaseStyles.DARK_GREY, fg_color="transparent", anchor="w",
                                       width=HomeStyles.TABLE_COL_W3, height=HomeStyles.TABLE_ROW_H)
        self.amount_header = ctk.CTkLabel(self.table_header, text="Amount", font=self.font1,
                                       text_color=BaseStyles.DARK_GREY, fg_color="transparent", anchor="e",
                                       width=HomeStyles.TABLE_COL_W3, height=HomeStyles.TABLE_ROW_H)
        # initialize table content
        self.recent_rows = self.loadRecentRows()
        # display table sections
        self.title_section.pack(pady=(0, BaseStyles.PAD_2))
        self.table_header.pack(pady=(0,BaseStyles.PAD_1))
        self.table_body.pack()
        # display table header
        self.date_header.grid(row=0, column=0, padx=(BaseStyles.PAD_2,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        self.type_header.grid(row=0, column=1, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        self.category_header.grid(row=0, column=2, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        self.description_header.grid(row=0, column=3, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        self.amount_header.grid(row=0, column=4, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        # display table content
        self.showRows()

    def _convertTransactionsToRows(self, transactions):
        rows = []
        for t in transactions:
            row = TableRow(transaction=t, master=self.table_body, fg_color=BaseStyles.WHITE)
            rows.append(row)
        return rows
    
    def loadRecentRows(self):
        # retrieve 5 recent transactions
        # recent_transactions = self.tm.repo.getRecentTransactions(user_id=self.user_id, t_count=5)
        recent_transactions = []
        # convert transactions to rows
        recent_rows = self._convertTransactionsToRows(transactions=recent_transactions)
        return recent_rows

    def showRows(self):
        # show rows
        for row in self.recent_rows:
            row.pack(pady=(0,BaseStyles.PAD_1))
            row.date_label.grid(row=0, column=0, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
            row.type_label.grid(row=0, column=1, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
            row.category_label.grid(row=0, column=2, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
            row.description_label.grid(row=0, column=3, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
            row.amount_label.grid(row=0, column=4, padx=(0,BaseStyles.PAD_2), pady=0, sticky="nw")


class MonthlyReport(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize font
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_3, weight="normal", slant="italic" )
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_4, weight="normal", slant="italic" )
        # sections
        self.title_section = ctk.CTkLabel(self, text="Monthly Report", text_color=BaseStyles.WHITE,
                                          fg_color=BaseStyles.BLUE, corner_radius=BaseStyles.RAD_2, font=self.font2,
                                          width=HomeStyles.REPORT_TITLE_SECTION_W, height=HomeStyles.REPORT_TITLE_SECTION_H)
        self.graphs_sections = ctk.CTkFrame(self, fg_color=BaseStyles.SKY_BLUE)
        # graph dimensions in inches
        graph_w_in = HomeStyles.MONTHLY_INCOME_GRAPH_W / BaseStyles.DPI
        graph_h_in = HomeStyles.MONTHLY_EXPENSE_GRAPH_H / BaseStyles.DPI
        self.income_graph, self.expense_graph = self.tm.createMonthlyGraph(user_id=self.user_id, width_in=graph_w_in,
                                                                           height_in=graph_h_in, dpi=BaseStyles.DPI,
                                                                           title_size=HomeStyles.MONTHLY_GRAPH_TITLE_SIZE,
                                                                           label_size=HomeStyles.MONTHLY_GRAPH_LABEL_SIZE)
        # create guide frames
        self.left_frame = ctk.CTkFrame(self.graphs_sections, fg_color=BaseStyles.WHITE, corner_radius=BaseStyles.RAD_2)
        self.right_frame = ctk.CTkFrame(self.graphs_sections, fg_color=BaseStyles.WHITE, corner_radius=BaseStyles.RAD_2)
        # layout income
        self.income_canvas = FigureCanvasTkAgg(figure=self.income_graph, master=self.left_frame)
        self.income_canvas.draw()
        self.income_canvas.get_tk_widget().pack(padx=BaseStyles.PAD_1, pady=(BaseStyles.PAD_1,BaseStyles.PAD_3))
        # layout expense
        self.expense_canvas = FigureCanvasTkAgg(figure=self.expense_graph, master=self.right_frame)
        self.expense_canvas.draw()
        self.expense_canvas.get_tk_widget().pack(padx=BaseStyles.PAD_1, pady=(BaseStyles.PAD_1,BaseStyles.PAD_3))
        # display sections
        self.title_section.pack(pady=(0,BaseStyles.PAD_2))
        self.graphs_sections.pack()
        # display guide frames
        self.left_frame.grid(row=0, column=0, padx=(0,BaseStyles.PAD_2))
        self.right_frame.grid(row=0, column=1)


class QuarterlyReport(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize font
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_3, weight="normal", slant="italic" )
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_4, weight="normal", slant="italic" )
        # sections
        self.title_section = ctk.CTkLabel(self, text="Quarterly Report", text_color=BaseStyles.WHITE,
                                          fg_color=BaseStyles.BLUE, corner_radius=BaseStyles.RAD_2, font=self.font2,
                                          width=HomeStyles.REPORT_TITLE_SECTION_W, height=HomeStyles.REPORT_TITLE_SECTION_H)
        self.graphs_sections = ctk.CTkFrame(self, fg_color=BaseStyles.WHITE, corner_radius=BaseStyles.RAD_2,
                                            width=HomeStyles.QUARTERLY_GRAPH_SECTION_W, height=HomeStyles.QUARTERLY_GRAPH_SECTION_H)
        # graph
        # dpi = self.winfo_fpixels("1i") # pixels per inch
        # graph_width = 760 / dpi
        # graph_height = 700 / dpi
        # title_size = 15
        # label_size = 10
        # self.graph = self.tm.createQuarterlyGraph(user_id=self.user_id, width=graph_width, height=graph_height,
        #                                           dpi=dpi, title_size=title_size, label_size=label_size)
        # # layout graph
        # self.graph_canvas = FigureCanvasTkAgg(figure=self.income_graph, master=self.left_frame)
        # self.graph_canvas.draw()
        # self.graph_canvas.get_tk_widget().pack(padx=BaseStyles.PAD_1, pady=(BaseStyles.PAD_1,BaseStyles.PAD_3))
        # display sections
        self.title_section.pack(pady=(0,BaseStyles.PAD_2))
        self.graphs_sections.pack()


class HomePage(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize state
        self.isCurrentPage = False
        # load imgs
        home_icon = self.loadIcons()
        # calculate balance 
        finance = self.tm.calculateOverallFinance(self.user_id)
        balance = self.tm.calculateOverallBalance(finance)
        # create page sections
        self.header_section = HomeHeader(img=home_icon, summary_type="Total Balance:", amount=balance,
                                         master=self, fg_color=BaseStyles.BLUE, corner_radius=BaseStyles.RAD_2)
        self.table_section = Table(user_id=self.user_id, tm=self.tm, master=self, fg_color=BaseStyles.SKY_BLUE, corner_radius=0)
        self.monthly_section = MonthlyReport(user_id=self.user_id, tm=self.tm, master=self, fg_color=BaseStyles.SKY_BLUE)
        self.quarterly_section = QuarterlyReport(user_id=self.user_id, tm=self, master=self, fg_color=BaseStyles.SKY_BLUE)
        # display sections
        self.header_section.pack(pady=(BaseStyles.PAD_5*2,0))
        self.table_section.pack(pady=(BaseStyles.PAD_2,0))
        self.monthly_section.pack(pady=(BaseStyles.PAD_2,0))
        self.quarterly_section.pack(pady=(BaseStyles.PAD_2,BaseStyles.PAD_5*2))

    def loadIcons(self):
        # icon path
        ICONS_FOLDER = os.path.abspath("assets/icons")
        # load images
        home_icon = ctk.CTkImage(Image.open(f"{ICONS_FOLDER}/home1.png"), size=(HomeStyles.IMG_H, HomeStyles.IMG_W))
        return home_icon
