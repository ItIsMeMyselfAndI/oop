import customtkinter as ctk
from datetime import datetime


SKY_BLUE = "#cef2ff"
BLUE = "#559eef"
DARK_BLUE = "#427cbd"
LIGHT_GREY = "#c4c4c4"
GREY = "grey"
DARK_GREY = "#545454"
WHITE= "white"


class DatePicker(ctk.CTkFrame):
    def __init__(self, picker_height, spacing, rad, day_width, month_width, year_width,
                 ctk_font, dropdown_ctk_font, dropdown_fg_color, master, **kwargs):
        super().__init__(master, **kwargs)
        # initialize fonts
        # create date options
        current_year = datetime.now().year
        years = [str(i) for i in range(current_year, 1800, -1)]
        months = ["January", "February", "March", "April",
                       "May", "June", "July", "August",
                       "September", "October", "November", "December"]
        days = [f"{str(i):0>2}" for i in range(1, 32)]
        # create date menu
        self.year = ctk.CTkOptionMenu(self, values=years,
                                      font=ctk_font, text_color=DARK_GREY,
                                      fg_color=BLUE, dropdown_font=dropdown_ctk_font,
                                      dropdown_fg_color=dropdown_fg_color,
                                      dropdown_hover_color=DARK_BLUE,
                                      dropdown_text_color=DARK_GREY,
                                      corner_radius=rad, width=year_width, height=picker_height)
        self.month = ctk.CTkOptionMenu(self, values=months,
                                       font=ctk_font, text_color=DARK_GREY,
                                       fg_color=BLUE, dropdown_font=dropdown_ctk_font,
                                       dropdown_fg_color=dropdown_fg_color,
                                       dropdown_hover_color=DARK_BLUE,
                                       dropdown_text_color=DARK_GREY,
                                       corner_radius=rad, width=month_width, height=picker_height)
        self.day = ctk.CTkOptionMenu(self, values=days,
                                     font=ctk_font, text_color=DARK_GREY,
                                     fg_color=BLUE, dropdown_font=dropdown_ctk_font,
                                     dropdown_fg_color=dropdown_fg_color,
                                     dropdown_hover_color=DARK_BLUE,
                                     dropdown_text_color=DARK_GREY,
                                     corner_radius=rad, width=day_width, height=picker_height)
        # display date menu
        self.year.grid(row=0, column=0, padx=(0,spacing))
        self.month.grid(row=0, column=1, padx=(0,spacing))
        self.day.grid(row=0, column=2, padx=(0,0))

