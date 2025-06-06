# external/built-in modules/libs
import customtkinter as ctk
from PIL import Image
import os
import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# our modules/libs
from frontend.styles import BaseStyles, HomeStyles # paddings, dimensions, colors, etc


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
            text_color=HomeStyles.DATE_COL_TEXT_COLOR,
            fg_color=HomeStyles.DATE_COL_FG_COLOR,
            width=HomeStyles.DATE_COL_W,
            height=HomeStyles.TABLE_ROW_H,
            anchor="w"
        )
        self.date_header.grid(row=0, column=0, padx=(BaseStyles.PAD_2,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        
        # type
        self.type_header = ctk.CTkLabel(
            master=self,
            text="Type",
            font=self.font3,
            text_color=HomeStyles.TYPE_COL_TEXT_COLOR,
            fg_color=HomeStyles.TYPE_COL_FG_COLOR,
            width=HomeStyles.TYPE_COL_W,
            height=HomeStyles.TABLE_ROW_H,
            anchor="w"
        )
        self.type_header.grid(row=0, column=1, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        
        # category
        self.category_header = ctk.CTkLabel(
            master=self,
            text="Category",
            font=self.font3,
            text_color=HomeStyles.CATEGORY_COL_TEXT_COLOR,
            fg_color=HomeStyles.CATEGORY_COL_FG_COLOR,
            width=HomeStyles.CATEGORY_COL_W,
            height=HomeStyles.TABLE_ROW_H,
            anchor="w"
        )
        self.category_header.grid(row=0, column=2, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        
        # description
        self.description_header = ctk.CTkLabel(
            master=self,
            text="Description",
            font=self.font3,
            text_color=HomeStyles.DESCRIPTION_COL_TEXT_COLOR,
            fg_color=HomeStyles.DESCRIPTION_COL_FG_COLOR,
            width=HomeStyles.DESCRIPTION_COL_W,
            height=HomeStyles.TABLE_ROW_H,
            anchor="w"
        )
        self.description_header.grid(row=0, column=3, padx=(0,BaseStyles.PAD_2), pady=BaseStyles.PAD_1)
        
        # amount
        self.amount_header = ctk.CTkLabel(
            master=self,
            text="Amount",
            font=self.font3,
            text_color=HomeStyles.AMOUNT_COL_TEXT_COLOR,
            fg_color=HomeStyles.AMOUNT_COL_FG_COLOR,
            width=HomeStyles.AMOUNT_COL_W,
            height=HomeStyles.TABLE_ROW_H,
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
            text_color=HomeStyles.DATE_COL_TEXT_COLOR,
            fg_color=HomeStyles.DATE_COL_FG_COLOR,
            width=HomeStyles.DATE_COL_W,
            height=HomeStyles.TABLE_ROW_H,
            wraplength=HomeStyles.DATE_COL_W,
            anchor="w",
            justify="left"
        )
        
        # type
        self.type_col = ctk.CTkLabel(
            master=self,
            text=self.t.t_type,
            font=self.font2,
            text_color=HomeStyles.TYPE_COL_TEXT_COLOR,
            fg_color=HomeStyles.TYPE_COL_FG_COLOR,
            width=HomeStyles.TYPE_COL_W,
            height=HomeStyles.TABLE_ROW_H,
            wraplength=HomeStyles.TYPE_COL_W,
            anchor="w",
            justify="left"
        )
        
        # category
        self.category_col = ctk.CTkLabel(
            master=self,
            text=self.t.t_category,
            font=self.font2,
            text_color=HomeStyles.CATEGORY_COL_TEXT_COLOR,
            fg_color=HomeStyles.CATEGORY_COL_FG_COLOR,
            width=HomeStyles.CATEGORY_COL_W,
            height=HomeStyles.TABLE_ROW_H,
            wraplength=HomeStyles.CATEGORY_COL_W,
            anchor="w",
            justify="left"
        )
        
        # description
        self.description_col = ctk.CTkLabel(
            master=self,
            text=self.t.t_description,
            font=self.font2,
            text_color=HomeStyles.DESCRIPTION_COL_TEXT_COLOR,
            fg_color=HomeStyles.DESCRIPTION_COL_FG_COLOR,
            width=HomeStyles.DESCRIPTION_COL_W,
            height=HomeStyles.TABLE_ROW_H,
            wraplength=HomeStyles.DESCRIPTION_COL_W,
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
            text_color=HomeStyles.AMOUNT_COL_TEXT_COLOR,
            fg_color=HomeStyles.AMOUNT_COL_FG_COLOR,
            width=HomeStyles.AMOUNT_COL_W-BaseStyles.PAD_1,
            height=HomeStyles.TABLE_ROW_H,
            wraplength=HomeStyles.AMOUNT_COL_W,
            anchor="e",
            justify="right"
        )
        

#--------------------------------------------------------------------------------------------------------


class Table(ctk.CTkFrame):
    def __init__(self, app, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app
        self.tm = tm
        
        # initialize font
        self.font3 = ("Bodoni MT", BaseStyles.FONT_SIZE_3, "italic")
        self.font4 = ("Bodoni MT", BaseStyles.FONT_SIZE_4, "italic")

        # table title
        self.title_section = ctk.CTkLabel(
            master=self,
            text="Recent Transactions",
            font=self.font4,
            corner_radius=BaseStyles.RAD_2,
            text_color=HomeStyles.TABLE_TITLE_TEXT_COLOR,
            fg_color=HomeStyles.TABLE_TITLE_SECTION_FG_COLOR,
            width=HomeStyles.TABLE_TITLE_SECTION_W,
            height=HomeStyles.TABLE_TITLE_SECTION_H
        )
        self.title_section.pack(pady=(0, BaseStyles.PAD_2))
        
        # table header
        self.table_header = TableHeader(
            master=self,
            corner_radius=BaseStyles.RAD_2,
            fg_color=HomeStyles.TABLE_HEADER_FG_COLOR
        )
        self.table_header.pack(pady=(0,BaseStyles.PAD_1))
        
        # table body
        self.table_body = ctk.CTkScrollableFrame(
            master=self,
            orientation="vertical",
            corner_radius=BaseStyles.RAD_2,
            width=HomeStyles.TABLE_BODY_W,
            height=HomeStyles.TABLE_BODY_H,
            fg_color=HomeStyles.TABLE_BODY_FG_COLOR
        )
        self.table_body.pack()

        # table rows 
        self.recent_rows = self.loadRecentRows()
        self.showRows()


    def loadRecentRows(self):
        # retrieve 5 recent transactions
        recent_transactions = self.tm.repo.getRecentTransactions(user_id=self.app.user_id, t_count=10)
        # convert transactions to rows
        recent_rows = []
        for t in recent_transactions:
            row = TableRow(
                transaction=t,
                master=self.table_body,
                fg_color=HomeStyles.TABLE_ROW_FG_COLOR
            )
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


#--------------------------------------------------------------------------------------------------------


class MonthlyReport(ctk.CTkFrame):
    def __init__(self, app, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app
        self.tm = tm
        
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
            fg_color=HomeStyles.MONTHLY_LEFT_GRAPH_FRAME_FG_COLOR,
            corner_radius=BaseStyles.RAD_2
        )
        self.income_frame.grid(row=0, column=0, padx=(0,BaseStyles.PAD_2))

        # expense section
        self.expense_frame = ctk.CTkFrame(
            master=self.graphs_section,
            fg_color=HomeStyles.MONTHLY_RIGHT_GRAPH_FRAME_FG_COLOR,
            corner_radius=BaseStyles.RAD_2
        )
        self.expense_frame.grid(row=0, column=1)

        # graphs
        self.income_canvas, self.expense_canvas = self.loadAndDisplayGraphsWidget()
        
    
    def loadAndDisplayGraphsWidget(self):
        # graph figures
        income_graph, expense_graph = self.tm.createMonthlyGraph(
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
        income_canvas.get_tk_widget().pack(padx=BaseStyles.PAD_1, pady=(BaseStyles.PAD_1,BaseStyles.PAD_3))
        
        # expense graph widget
        expense_canvas = FigureCanvasTkAgg(figure=expense_graph, master=self.expense_frame)
        expense_canvas.draw()
        expense_canvas.get_tk_widget().pack(padx=BaseStyles.PAD_1, pady=(BaseStyles.PAD_1,BaseStyles.PAD_3))
        
        return income_canvas, expense_canvas
    

    def updateGraphsDisplay(self):
        self.income_canvas.get_tk_widget().destroy()
        self.expense_canvas.get_tk_widget().destroy()
        self.income_canvas, self.expense_canvas = self.loadAndDisplayGraphsWidget()


#--------------------------------------------------------------------------------------------------------


class QuarterlyReport(ctk.CTkFrame):
    def __init__(self, app, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app
        self.tm = tm
        
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
            width=HomeStyles.QUARTERLY_GRAPH_SECTION_W,
            height=HomeStyles.QUARTERLY_GRAPH_SECTION_H
        )
        self.graph_section.pack()
        
        # graph
        # dpi = self.winfo_fpixels("1i") # pixels per inch
        # graph_width = 760 / dpi
        # graph_height = 700 / dpi
        # title_size = 15
        # label_size = 10
        # self.graph = self.tm.createQuarterlyGraph(user_id=self.app.user_id, width=graph_width, height=graph_height,
        #                                           dpi=dpi, title_size=title_size, label_size=label_size)
        # # layout graph
        # self.graph_canvas = FigureCanvasTkAgg(figure=self.income_graph, master=self.income_frame)
        # self.graph_canvas.draw()
        # self.graph_canvas.get_tk_widget().pack(padx=BaseStyles.PAD_1, pady=(BaseStyles.PAD_1,BaseStyles.PAD_3))
        # display sections


#--------------------------------------------------------------------------------------------------------


class HomePage(ctk.CTkFrame):
    def __init__(self, app, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app
        self.tm = tm

        # initialize state
        self.is_current_page = False
        
        # scrollable frame
        self.scroll_frame = ctk.CTkScrollableFrame(
            master=self,
            orientation="vertical",
            corner_radius=0,
            fg_color=HomeStyles.MAIN_FRAME_FG_COLOR,
            width=HomeStyles.MAIN_FRAME_W,
            height=HomeStyles.MAIN_FRAME_H
        )
        self.scroll_frame.pack()

        # header
        home_icon = self.loadIcons()
        balance = self.loadOverallBalance()
        self.header_section = HomeHeader(
            img=home_icon,
            summary_type="Total Balance:",
            amount=balance,
            master=self.scroll_frame,
            fg_color=HomeStyles.HEADER_SECTION_FG_COLOR,
            corner_radius=BaseStyles.RAD_2
        )
        self.header_section.pack(pady=(BaseStyles.PAD_5*2,0))

        # table
        self.table_section = Table(
            app=self.app,
            tm=self.tm,
            master=self.scroll_frame,
            corner_radius=0,
            fg_color=HomeStyles.TABLE_SECTION_FG_COLOR
        )
        self.table_section.pack(pady=(BaseStyles.PAD_2,0))

        # monthly
        self.monthly_section = MonthlyReport(
            app=self.app,
            tm=self.tm,
            master=self.scroll_frame,
            fg_color=HomeStyles.MONTHLY_SECTION_FG_COLOR
        )
        self.monthly_section.pack(pady=(BaseStyles.PAD_2,0))

        # quarterly
        self.quarterly_section = QuarterlyReport(
            app=self.app,
            tm=self,
            master=self.scroll_frame,
            fg_color=HomeStyles.QUARTERLY_SECTION_FG_COLOR
        )
        self.quarterly_section.pack(pady=(BaseStyles.PAD_2,BaseStyles.PAD_5*3))


    def loadOverallBalance(self):
        finance = self.tm.calculateOverallFinance(self.app.user_id)
        balance = self.tm.calculateOverallBalance(finance)
        return balance


    def loadIcons(self):
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


    def updatePageDisplay(self):
        # update balance
        finance = self.tm.calculateOverallFinance(self.app.user_id)
        balance = self.tm.calculateOverallBalance(finance)
        self.header_section.amount_label.configure(text=f"₱ {balance:,}")
        # update table
        self.table_section.deletePrevRowsVersion()
        self.table_section.recent_rows = self.table_section.loadRecentRows()
        self.table_section.showRows()
        # update monthly
        self.monthly_section.updateGraphsDisplay()
