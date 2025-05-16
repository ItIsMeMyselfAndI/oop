import customtkinter as ctk
from datetime import datetime


class DatePicker(ctk.CTkFrame):
    def __init__(self, picker_height, spacing, rad,
                 day_width, month_width, year_width,
                 ctk_font, master, **kwargs):
        super().__init__(master, **kwargs)
        # initialize fonts
        # create date options
        current_year = datetime.now().year
        self.years = [str(i) for i in range(current_year, 1800, -1)]
        self.months = ["January", "February", "March", "April",
                       "May", "June", "July", "August",
                       "September", "October", "November", "December"]
        self.days = [f"{str(i):0>2}" for i in range(1, 32)]
        # create date menu
        self.year = ctk.CTkOptionMenu(self, values=self.years,
                                      font=ctk_font, text_color="#545454",
                                      fg_color="#559eef", dropdown_font=ctk_font,
                                      dropdown_fg_color="#559eef",
                                      dropdown_hover_color="#427cbd",
                                      dropdown_text_color="#545454",
                                      corner_radius=rad, width=year_width, height=picker_height)
        self.month = ctk.CTkOptionMenu(self, values=self.months,
                                       font=ctk_font, text_color="#545454",
                                       fg_color="#559eef", dropdown_font=ctk_font,
                                       dropdown_fg_color="#559eef",
                                       dropdown_hover_color="#427cbd",
                                       dropdown_text_color="#545454",
                                       corner_radius=rad, width=month_width, height=picker_height)
        self.day = ctk.CTkOptionMenu(self, values=self.days,
                                     font=ctk_font, text_color="#545454",
                                     fg_color="#559eef", dropdown_font=ctk_font,
                                     dropdown_fg_color="#559eef",
                                     dropdown_hover_color="#427cbd",
                                     dropdown_text_color="#545454",
                                     corner_radius=rad, width=day_width, height=picker_height)
        # display date menu
        self.year.grid(row=0, column=0, padx=(0,spacing))
        self.month.grid(row=0, column=1, padx=(0,spacing))
        self.day.grid(row=0, column=2, padx=(0,0))

