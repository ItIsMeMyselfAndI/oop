# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from frontend.utilities.styles import * # contains paddings, dimensions, colors, etc


class TableFilter(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_3, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_5, slant="italic", weight="normal")
        t_types = ["income", "savings", "expenses", "investment"]
        self.type_menu = ctk.CTkOptionMenu(self, values=t_types, font=self.font1, text_color=DARK_GREY,
                                           fg_color=BLUE, dropdown_font=self.font2,
                                           dropdown_fg_color=WHITE, dropdown_hover_color=DARK_BLUE,
                                           dropdown_text_color=DARK_GREY, corner_radius=RAD_2,
                                           width=MENU_W1, height=MENU_H)
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

        self.date_label.grid(row=0, column=0, padx=(0,PAD_3))
        self.type_label.grid(row=0, column=1, padx=(0,PAD_3))
        self.category_label.grid(row=0, column=2, padx=(0,PAD_3))
        self.description_label.grid(row=0, column=3, padx=(0,PAD_3))
        self.amount_label.grid(row=0, column=4, padx=(0,0))


class History(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        # initialize state
        self.isCurrentPage = False

        self.header_section = HistoryHeader(master=self, fg_color=BLUE, corner_radius=RAD_2,
                                            height=HEADER_H, width=HEADER_W)
        self.table = Table(self, fg_color=RED, corner_radius=RAD_2)

        self.header_section.pack(fill="y", expand=True, padx=PAD_5+PAD_5, pady=(PAD_5+PAD_5,0))
        self.table.pack(padx=PAD_3, pady=PAD_4)