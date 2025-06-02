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
        self.font4 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_4, weight="normal", slant="italic" )
        self.font6 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_6, weight="normal", slant="italic" )
        self.img = img
        # create guide frames
        self.balance_frame = ctk.CTkFrame(self, corner_radius=0, fg_color=HomeStyles.BALANCE_FRAME_FG_COLOR)
        self.img_bg = ctk.CTkLabel(self, corner_radius=0, image=img, text="", fg_color=HomeStyles.HOME_IMG_BG_COLOR,
                                   width=HomeStyles.HOME_IMG_BG_W, height=HomeStyles.HOME_IMG_BG_H)
        # create balance labels
        self.balance_title_label = ctk.CTkLabel(self.balance_frame, text=summary_type, font=self.font4, text_color=HomeStyles.BALANCE_TITLE_TEXT_COLOR,
                                               fg_color=HomeStyles.BALANCE_TITLE_LABEL_FG_COLOR, anchor="w")
        self.amount_label = ctk.CTkLabel(self.balance_frame, text=f"₱ {amount:,}", font=self.font6, text_color=HomeStyles.BALANCE_AMOUNT_TEXT_COLOR,
                                         width=HomeStyles.BALANCE_AMOUNT_LABEL_W, wraplength=HomeStyles.BALANCE_AMOUNT_LABEL_W,
                                         fg_color=HomeStyles.BALANCE_AMOUNT_LABEL_FG_COLOR, anchor="w", justify="left")
        # display guide frames
        self.balance_frame.grid(row=0, column=0, padx=(BaseStyles.PAD_4,0))
        self.img_bg.grid(row=0, column=1, pady=BaseStyles.PAD_3, padx=BaseStyles.PAD_3, sticky="e")
        # display labels
        self.balance_title_label.pack(anchor="w")
        self.amount_label.pack(anchor="w")


class TableHeader(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font3 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_3, weight="normal", slant="italic" )
        self.font4 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_4, weight="normal", slant="italic" )
        # table headers
        self.date_header = ctk.CTkLabel(self, text="Date", font=self.font3,
                                        text_color=HomeStyles.DATE_COL_TEXT_COLOR, fg_color=HomeStyles.DATE_COL_FG_COLOR,
                                        width=HomeStyles.DATE_COL_W, height=HomeStyles.TABLE_ROW_H, anchor="w")
        self.type_header = ctk.CTkLabel(self, text="Type", font=self.font3,
                                        text_color=HomeStyles.TYPE_COL_TEXT_COLOR, fg_color=HomeStyles.TYPE_COL_FG_COLOR,
                                        width=HomeStyles.TYPE_COL_W, height=HomeStyles.TABLE_ROW_H, anchor="w")
        self.category_header = ctk.CTkLabel(self, text="Category", font=self.font3,
                                            text_color=HomeStyles.CATEGORY_COL_TEXT_COLOR, fg_color=HomeStyles.CATEGORY_COL_FG_COLOR,
                                            width=HomeStyles.CATEGORY_COL_W, height=HomeStyles.TABLE_ROW_H, anchor="w")
        self.description_header = ctk.CTkLabel(self, text="Description", font=self.font3,
                                               text_color=HomeStyles.DESCRIPTION_COL_TEXT_COLOR, fg_color=HomeStyles.DESCRIPTION_COL_FG_COLOR,
                                               width=HomeStyles.DESCRIPTION_COL_W, height=HomeStyles.TABLE_ROW_H, anchor="w")
        self.amount_header = ctk.CTkLabel(self, text="Amount", font=self.font3,
                                          text_color=HomeStyles.AMOUNT_COL_TEXT_COLOR, fg_color=HomeStyles.AMOUNT_COL_FG_COLOR,
                                          width=HomeStyles.AMOUNT_COL_W, height=HomeStyles.TABLE_ROW_H, anchor="e")
        # display table header
        self.date_header.grid(row=0, column=0, padx=(BaseStyles.PAD_2,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        self.type_header.grid(row=0, column=1, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        self.category_header.grid(row=0, column=2, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        self.description_header.grid(row=0, column=3, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        self.amount_header.grid(row=0, column=4, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)


class TableRow(ctk.CTkFrame):
    def __init__(self, transaction, master, **kwargs):
        super().__init__(master, **kwargs)
        self.t = transaction
        # initialize font
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_2, weight="normal", slant="italic" )
        self.font4 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_4, weight="normal", slant="italic" )
        
        self.date_col = ctk.CTkLabel(self, text=self.t.t_date, font=self.font2,
                                     text_color=HomeStyles.DATE_COL_TEXT_COLOR, fg_color=HomeStyles.DATE_COL_FG_COLOR,
                                     width=HomeStyles.DATE_COL_W, height=HomeStyles.TABLE_ROW_H,
                                     wraplength=HomeStyles.DATE_COL_W, anchor="w", justify="left")
        self.type_col = ctk.CTkLabel(self, text=self.t.t_type, font=self.font2,
                                     text_color=HomeStyles.TYPE_COL_TEXT_COLOR, fg_color=HomeStyles.TYPE_COL_FG_COLOR,
                                     width=HomeStyles.TYPE_COL_W, height=HomeStyles.TABLE_ROW_H,
                                     wraplength=HomeStyles.TYPE_COL_W, anchor="w", justify="left")
        self.category_col = ctk.CTkLabel(self, text=self.t.t_category, font=self.font2,
                                         text_color=HomeStyles.CATEGORY_COL_TEXT_COLOR, fg_color=HomeStyles.CATEGORY_COL_FG_COLOR,
                                         width=HomeStyles.CATEGORY_COL_W, height=HomeStyles.TABLE_ROW_H,
                                         wraplength=HomeStyles.CATEGORY_COL_W, anchor="w", justify="left")
        self.description_col = ctk.CTkLabel(self, text=self.t.t_description, font=self.font2,
                                            text_color=HomeStyles.DESCRIPTION_COL_TEXT_COLOR, fg_color=HomeStyles.DESCRIPTION_COL_FG_COLOR,
                                            width=HomeStyles.DESCRIPTION_COL_W, height=HomeStyles.TABLE_ROW_H,
                                            wraplength=HomeStyles.DESCRIPTION_COL_W, anchor="w", justify="left")
        self.amount_col = ctk.CTkLabel(self, text=f"₱ {self.t.t_amount}", font=self.font2,
                                       text_color=HomeStyles.AMOUNT_COL_TEXT_COLOR, fg_color=HomeStyles.AMOUNT_COL_FG_COLOR,
                                       width=HomeStyles.AMOUNT_COL_W-BaseStyles.PAD_1, height=HomeStyles.TABLE_ROW_H,
                                       wraplength=HomeStyles.AMOUNT_COL_W, anchor="e", justify="right")
        

class Table(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize font
        self.font3 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_3, weight="normal", slant="italic" )
        self.font4 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_4, weight="normal", slant="italic" )
        # table sections
        self.title_section = ctk.CTkLabel(self, text="Recent Transactions", font=self.font4, corner_radius=BaseStyles.RAD_2,
                                          text_color=HomeStyles.TABLE_TITLE_TEXT_COLOR, fg_color=HomeStyles.TABLE_TITLE_SECTION_FG_COLOR,
                                          width=HomeStyles.TABLE_TITLE_SECTION_W, height=HomeStyles.TABLE_TITLE_SECTION_H)
        self.table_header = TableHeader(self, corner_radius=BaseStyles.RAD_2, fg_color=HomeStyles.TABLE_HEADER_FG_COLOR)
        self.table_body = ctk.CTkScrollableFrame(self, orientation="vertical", corner_radius=BaseStyles.RAD_2,
                                                 width=HomeStyles.TABLE_BODY_W, height=HomeStyles.TABLE_BODY_H,
                                                 fg_color=HomeStyles.TABLE_BODY_FG_COLOR)
        # initialize table content
        self.recent_rows = self.loadRecentRows()
        # display table sections
        self.title_section.pack(pady=(0, BaseStyles.PAD_2))
        self.table_header.pack(pady=(0,BaseStyles.PAD_1))
        self.table_body.pack()
        # display table content
        self.showRows()

    def loadRecentRows(self):
        # retrieve 5 recent transactions
        recent_transactions = self.tm.repo.getRecentTransactions(user_id=self.user_id, t_count=10)
        # convert transactions to rows
        recent_rows = []
        for t in recent_transactions:
            row = TableRow(transaction=t, master=self.table_body, fg_color=HomeStyles.TABLE_ROW_FG_COLOR)
            recent_rows.append(row)
        return recent_rows

    def deletePrevRowsVersion(self):
        for row in self.recent_rows:
            row.destroy()

    def showRows(self):
        # show rows
        for row in self.recent_rows:
            row.pack(pady=(0,BaseStyles.PAD_1))
            row.date_col.grid(row=0, column=0, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
            row.type_col.grid(row=0, column=1, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
            row.category_col.grid(row=0, column=2, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
            row.description_col.grid(row=0, column=3, padx=(0,BaseStyles.PAD_2), pady=0, sticky="n")
            row.amount_col.grid(row=0, column=4, padx=(0,BaseStyles.PAD_2), pady=0, sticky="nw")


class MonthlyReport(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize font
        self.font3 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_3, weight="normal", slant="italic" )
        self.font4 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_4, weight="normal", slant="italic" )
        # sections
        self.title_section = ctk.CTkLabel(self, text="Monthly Report", corner_radius=BaseStyles.RAD_2, font=self.font4,
                                          text_color=HomeStyles.MONTHLY_TITLE_TEXT_COLOR, fg_color=HomeStyles.MONTHLY_TITLE_SECTION_FG_COLOR,
                                          width=HomeStyles.MONTHLY_TITLE_SECTION_W, height=HomeStyles.MONTHLY_TITLE_SECTION_H)
        self.graphs_section = ctk.CTkFrame(self, fg_color=HomeStyles.MONTHLY_GRAPHS_SECTION_FG_COLOR)
        # create guide frames
        self.left_frame = ctk.CTkFrame(self.graphs_section, fg_color=HomeStyles.MONTHLY_LEFT_GRAPH_FRAME_FG_COLOR, corner_radius=BaseStyles.RAD_2)
        self.right_frame = ctk.CTkFrame(self.graphs_section, fg_color=HomeStyles.MONTHLY_RIGHT_GRAPH_FRAME_FG_COLOR, corner_radius=BaseStyles.RAD_2)
        # load and display graphs
        self.income_canvas, self.expense_canvas = self.loadAndDisplayGraphsWidget()
        # display sections
        self.title_section.pack(pady=(0,BaseStyles.PAD_2))
        self.graphs_section.pack()
        # display guide frames
        self.left_frame.grid(row=0, column=0, padx=(0,BaseStyles.PAD_2))
        self.right_frame.grid(row=0, column=1)
    
    def loadAndDisplayGraphsWidget(self):
        # graph dimensions in inches
        graph_w_in = HomeStyles.MONTHLY_INCOME_GRAPH_W / BaseStyles.DPI
        graph_h_in = HomeStyles.MONTHLY_EXPENSE_GRAPH_H / BaseStyles.DPI
        income_graph, expense_graph = self.tm.createMonthlyGraph(user_id=self.user_id, width_in=graph_w_in,
                                                                           height_in=graph_h_in, dpi=BaseStyles.DPI,
                                                                           title_size=HomeStyles.MONTHLY_GRAPH_TITLE_SIZE,
                                                                           label_size=HomeStyles.MONTHLY_GRAPH_LABEL_SIZE)
        # layout income
        income_canvas = FigureCanvasTkAgg(figure=income_graph, master=self.left_frame)
        income_canvas.draw()
        income_canvas.get_tk_widget().pack(padx=BaseStyles.PAD_1, pady=(BaseStyles.PAD_1,BaseStyles.PAD_3))
        # layout expense
        expense_canvas = FigureCanvasTkAgg(figure=expense_graph, master=self.right_frame)
        expense_canvas.draw()
        expense_canvas.get_tk_widget().pack(padx=BaseStyles.PAD_1, pady=(BaseStyles.PAD_1,BaseStyles.PAD_3))
        return income_canvas, expense_canvas


class QuarterlyReport(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize font
        self.font3 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_3, weight="normal", slant="italic" )
        self.font4 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_4, weight="normal", slant="italic" )
        # sections
        self.title_section = ctk.CTkLabel(self, text="Quarterly Report", font=self.font4, corner_radius=BaseStyles.RAD_2,
                                          text_color=HomeStyles.QUARTERLY_TITLE_TEXT_COLOR, fg_color=HomeStyles.QUARTERLY_TITLE_SECTION_FG_COLOR,
                                          width=HomeStyles.QUARTERLY_TITLE_SECTION_W, height=HomeStyles.QUARTERLY_TITLE_SECTION_H)
        self.graphs_section = ctk.CTkFrame(self, fg_color=HomeStyles.QUARTERLY_GRAPHS_SECTION_FG_COLOR, corner_radius=BaseStyles.RAD_2,
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
        self.graphs_section.pack()


class HomePage(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize state
        self.is_current_page = False
        # load imgs
        home_icon = self.loadIcons()
        # scrollable frame
        self.scroll_frame = ctk.CTkScrollableFrame(self, orientation="vertical", corner_radius=0, fg_color=HomeStyles.MAIN_FRAME_FG_COLOR,
                                                   width=HomeStyles.MAIN_FRAME_W, height=HomeStyles.MAIN_FRAME_H)
        # calculate balance 
        balance = self.loadOverallBalance()
        # create page sections
        self.header_section = HomeHeader(img=home_icon, summary_type="Total Balance:", amount=balance, master=self.scroll_frame,
                                         fg_color=HomeStyles.HEADER_SECTION_FG_COLOR, corner_radius=BaseStyles.RAD_2)
        self.table_section = Table(user_id=self.user_id, tm=self.tm, master=self.scroll_frame, corner_radius=0, fg_color=HomeStyles.TABLE_SECTION_FG_COLOR)
        self.monthly_section = MonthlyReport(user_id=self.user_id, tm=self.tm, master=self.scroll_frame, fg_color=HomeStyles.MONTHLY_SECTION_FG_COLOR)
        self.quarterly_section = QuarterlyReport(user_id=self.user_id, tm=self, master=self.scroll_frame, fg_color=HomeStyles.QUARTERLY_SECTION_FG_COLOR)
        # display main frame
        self.scroll_frame.pack()
        # display sections
        self.header_section.pack(pady=(BaseStyles.PAD_5*2,0))
        self.table_section.pack(pady=(BaseStyles.PAD_2,0))
        self.monthly_section.pack(pady=(BaseStyles.PAD_2,0))
        self.quarterly_section.pack(pady=(BaseStyles.PAD_2,BaseStyles.PAD_5*3))

    def loadOverallBalance(self):
        finance = self.tm.calculateOverallFinance(self.user_id)
        balance = self.tm.calculateOverallBalance(finance)
        return balance

    def loadIcons(self):
        # icon path
        ICONS_FOLDER = os.path.abspath("assets/icons")
        # load images
        home_icon = ctk.CTkImage(Image.open(f"{ICONS_FOLDER}/home1.png"), size=(HomeStyles.HOME_IMG_H, HomeStyles.HOME_IMG_W))
        return home_icon

    def updatePageDisplay(self):
        # update balance
        finance = self.tm.calculateOverallFinance(self.user_id)
        balance = self.tm.calculateOverallBalance(finance)
        self.header_section.amount_label.configure(text=f"₱ {balance:,}")
        # update table
        self.table_section.deletePrevRowsVersion()
        self.table_section.recent_rows = self.table_section.loadRecentRows()
        self.table_section.showRows()
        # update monthly
        self.monthly_section.income_canvas.get_tk_widget().destroy()
        self.monthly_section.expense_canvas.get_tk_widget().destroy()
        self.monthly_section.loadAndDisplayGraphsWidget()
