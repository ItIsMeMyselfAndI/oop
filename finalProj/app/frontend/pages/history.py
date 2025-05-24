import customtkinter as ctk


# create global screen dimension
temp_root = ctk.CTk()
SCREEN_W = temp_root.winfo_screenwidth()
temp_root.destroy()
SCREEN_H = int(0.5625*SCREEN_W)
print(SCREEN_W, SCREEN_H)

FONT_SIZE_1 = int(0.0231*SCREEN_H) #25
FONT_SIZE_2 = int(0.0278*SCREEN_H) #30
FONT_SIZE_3 = int(0.0370*SCREEN_H) #40
FONT_SIZE_4 = int(0.0463*SCREEN_H) #50
FONT_SIZE_5 = int(0.0556*SCREEN_H) #60

WHITE= "white"

WHITE_RED = "#fdecec"
LIGHT_RED = "#ffc7c7"
RED = "#e14242"

WHITE_GREEN = "#dafbf0"
LIGHT_GREEN = "#b2fee3"
GREEN = "#28ab58"

WHITE_PURPLE = "#f3eefe"
LIGHT_PURPLE =  "#d6c5fb"
PURPLE = "#ceb9fe"

WHITE_BLUE = "#ebf2fe"
SKY_BLUE = "#cef2ff"
LIGHT_BLUE = "#bcd4fe"
BLUE = "#559eef"
DARK_BLUE = "#427cbd"

LIGHT_GREY = "#c4c4c4"
GREY = "grey"
DARK_GREY = "#545454"

ENTRY_W1 = int(1.3241*SCREEN_H)#1430
ENTRY_W2 = int(0.5556*SCREEN_H) #600
ENTRY_H = int(0.0556*SCREEN_H) #60

MENU_W1 = int(0.7407*SCREEN_H) #800
MENU_W2 = int(1.2593*SCREEN_H) #1360 
MENU_H = int(0.0556*SCREEN_H) #60

YEAR_MENU_W = int(0.4167*SCREEN_H) #450
MONTH_MENU_W = int(0.4630*SCREEN_H) #500 
DAY_MENU_W = int(0.4167*SCREEN_H) #450

PAD_X1 = int(0.0093*SCREEN_H) #10
PAD_X2 = int(0.0185*SCREEN_H) #20
PAD_X3 = int(0.0278*SCREEN_H) #30
PAD_X4 = int(0.0370*SCREEN_H) #40
PAD_X5 = int(0.0463*SCREEN_H) #50

PAD_Y1 = int(0.0093*SCREEN_H) #10
PAD_Y2 = int(0.0185*SCREEN_H) #20
PAD_Y3 = int(0.0278*SCREEN_H) #30
PAD_Y4 = int(0.0370*SCREEN_H) #40
PAD_Y5 = int(0.0463*SCREEN_H) #50

BTN_W1 = int(0.0648*SCREEN_H) #70
BTN_W2 = int(0.3241*SCREEN_H) #350

BTN_H1 = int(0.0648*SCREEN_H) #70
BTN_H2 = int(0.0556*SCREEN_H) #60

RAD = int(0.0185*SCREEN_H) #20


# ---- exclusive ----

TABLE_COL_W1 = int(0.2315*SCREEN_H) #250
TABLE_COL_W2 = int(0.3704*SCREEN_H) #400

TABLE_W = int(1.4074*SCREEN_H) #1500

HEADER_H = int(0.2593*SCREEN_H) #280
HEADER_W = int(1.5093*SCREEN_H) #1630


class TableFilter(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_3, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_5, slant="italic", weight="normal")
        t_types = ["income", "savings", "expenses", "investment"]
        self.type_menu = ctk.CTkOptionMenu(self, values=t_types,
                                                 font=self.font1, text_color=DARK_GREY,
                                                 fg_color=BLUE, dropdown_font=self.font2,
                                                 dropdown_fg_color=WHITE,
                                                 dropdown_hover_color=DARK_BLUE,
                                                 dropdown_text_color=DARK_GREY,
                                                 corner_radius=RAD, width=MENU_W1, height=MENU_H)
        # t_categories = [""]
        self.type_menu.grid(row=0, column=0)
        # self.


# header section
class HistoryHeader(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_3, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_5, slant="italic", weight="normal")

        self.label = ctk.CTkLabel(self, text="Transaction History", font=self.font1, text_color=DARK_GREY)
        self.filter = TableFilter(self)


        self.label.pack()#anchor="w")


class Table(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_2, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_3, slant="italic", weight="normal")
        # table sections
        self.table_header = ctk.CTkFrame(self, fg_color=WHITE)
        self.table_body = ctk.CTkScrollableFrame(self, fg_color=WHITE, orientation="vertical", 
                                                 height=100, width=TABLE_W)
        # table header content
        self.date_label = ctk.CTkLabel(self.table_header, text="Date", font=self.font1,
                                       text_color=DARK_GREY, width=TABLE_COL_W1, fg_color=WHITE)
        self.type_label = ctk.CTkLabel(self.table_header, text="Type", font=self.font1,
                                       text_color=DARK_GREY, width=TABLE_COL_W1, fg_color=WHITE)
        self.category_label = ctk.CTkLabel(self.table_header, text="Category", font=self.font1,
                                       text_color=DARK_GREY, width=TABLE_COL_W1, fg_color=WHITE)
        self.description_label = ctk.CTkLabel(self.table_header, text="Description", font=self.font1,
                                       text_color=DARK_GREY, width=TABLE_COL_W2, fg_color=WHITE)
        self.amount_label = ctk.CTkLabel(self.table_header, text="Amount", font=self.font1,
                                       text_color=DARK_GREY, width=TABLE_COL_W1, fg_color=WHITE)
        # table body content


        self.table_header.pack()
        self.table_body.pack()

        self.date_label.grid(row=0, column=0, padx=(0,PAD_X3))
        self.type_label.grid(row=0, column=1, padx=(0,PAD_X3))
        self.category_label.grid(row=0, column=2, padx=(0,PAD_X3))
        self.description_label.grid(row=0, column=3, padx=(0,PAD_X3))
        self.amount_label.grid(row=0, column=4, padx=(0,0))


class History(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        # initialize state
        self.isCurrentPage = False

        self.header_section = HistoryHeader(master=self, fg_color=BLUE, corner_radius=RAD,
                                            height=HEADER_H, width=HEADER_W)
        self.table = Table(self, fg_color=RED, corner_radius=RAD)

        self.header_section.pack(fill="y", expand=True, padx=PAD_X5+PAD_X5, pady=(PAD_Y5+PAD_Y5,0))
        self.table.pack(padx=PAD_X3, pady=PAD_Y4)