import customtkinter as ctk


FONT_SIZE_1 = 25
FONT_SIZE_2 = 30
FONT_SIZE_3 = 40
FONT_SIZE_4 = 50
FONT_SIZE_5 = 60

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

ENTRY_W1 = 1430
ENTRY_W2 = 600
ENTRY_H = 60

MENU_W1 = 800
MENU_W2 = 1360 
MENU_H = 60
YEAR_MENU_W = 180
MONTH_MENU_W = 220
DAY_MENU_W = 180

PAD_X1 = 10
PAD_X2 = 20
PAD_X3 = 30
PAD_X4 = 40
PAD_X5 = 50

PAD_Y1 = 10
PAD_Y2 = 20
PAD_Y3 = 30
PAD_Y4 = 40
PAD_Y5 = 50

BTN_W1 = 70
BTN_W2 = 350

BTN_H1 = 70
BTN_H2 = 60

RAD = 20

TABLE_COL_W1 = 250
TABLE_COL_W2 = 400


HEADER_H = 280
HEADER_W = 1630

# header section
class HistoryHeader(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_3, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_5, slant="italic", weight="normal")

        # self.label = ctk.CTkLabel(self, text="Transaction History", font=self.font1, text_color=DARK_GREY)
        # self.label.pack(anchor="w")


class Table(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_2, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_3, slant="italic", weight="normal")
        
        self.header = ctk.CTkFrame(self, fg_color=WHITE)
        self.date_label = ctk.CTkLabel(self.header, text="Date", font=self.font1,
                                       text_color=DARK_GREY, width=TABLE_COL_W1, fg_color=GREEN)
        self.type_label = ctk.CTkLabel(self.header, text="Type", font=self.font1,
                                       text_color=DARK_GREY, width=TABLE_COL_W1, fg_color=GREEN)
        self.category_label = ctk.CTkLabel(self.header, text="Category", font=self.font1,
                                       text_color=DARK_GREY, width=TABLE_COL_W1, fg_color=GREEN)
        self.description_label = ctk.CTkLabel(self.header, text="Description", font=self.font1,
                                       text_color=DARK_GREY, width=TABLE_COL_W2, fg_color=GREEN)
        self.amount_label = ctk.CTkLabel(self.header, text="Amount", font=self.font1,
                                       text_color=DARK_GREY, width=TABLE_COL_W1, fg_color=GREEN)

        self.header.pack() 
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

        self.header_section.pack(padx=PAD_X5+PAD_X5, pady=(PAD_Y5+PAD_Y5,0))
        self.table.pack(padx=PAD_X3, pady=PAD_Y4)
    #     self.transaction_data = []

    #     # Make self fully expandable
    #     self.grid_rowconfigure(1, weight=1)
    #     self.grid_columnconfigure(0, weight=1)

    #     # Title Label
    #     title_label = ctk.CTkLabel(self,
    #                                text="Transaction History",
    #                                font=ctk.CTkFont(family="Bodoni MT", size=40, slant="italic"),
    #                                text_color='#545454')
    #     title_label.grid(row=0, column=0, sticky="w", padx=30, pady=(30, 10))

    #     # Table container
    #     self.table_frame = ctk.CTkFrame(self, corner_radius=25, fg_color='white')
    #     self.table_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=30)

    #     # Columns
    #     for col in range(4):
    #         self.table_frame.grid_columnconfigure(col, weight=1)

    #     # Headers
    #     headers = ['Category', 'Date', 'Amount', 'Description']
    #     for index, header in enumerate(headers):
    #         label = ctk.CTkLabel(self.table_frame,
    #                              text=header,
    #                              font=ctk.CTkFont(family='Sans Serif', size=20, weight='bold'),
    #                              text_color='black')
    #         label.grid(row=0, column=index, sticky="nsew", padx=40, pady=20)

    #     self.row_index = 1


    # def add(self, category, date, amount, description):
    #     self.transaction_data.append((category, date, amount, description))
    #     values = [category, date, amount, description]
    #     for col, value in enumerate(values):
    #         label = ctk.CTkLabel(self.table_frame, text=value, text_color='black')
    #         label.grid(row=self.row_index, column=col, sticky="nsew", padx=40, pady=15)
    #     self.row_index += 1
