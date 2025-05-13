import customtkinter as ctk
from datetime import datetime


class DatePicker(ctk.CTkFrame):
    def __init__(self, picker_height, spacing,
                 day_width, month_width, year_width,
                 master, **kwargs):
        super().__init__(master, **kwargs)
        # initialize fonts
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=30, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=20, slant="italic", weight="normal")
        # create date options
        self.months = ["January", "February", "March", "April",
                       "May", "June", "July", "August",
                       "September", "October", "November", "December"]
        self.days = [f"{str(i):0>2}" for i in range(1, 32)]
        current_year = datetime.now().year
        self.years = [str(i) for i in range(current_year, 1800, -1)]
        # create date menu
        self.day = ctk.CTkOptionMenu(self, values=self.days,
                                     font=self.font2, text_color="#545454",
                                     fg_color="#559eef", dropdown_font=self.font2,
                                     dropdown_fg_color="#559eef",
                                     dropdown_hover_color="#427cbd",
                                     dropdown_text_color="#545454",
                                     corner_radius=10, width=day_width, height=picker_height)
        self.month = ctk.CTkOptionMenu(self, values=self.months,
                                       font=self.font2, text_color="#545454",
                                       fg_color="#559eef", dropdown_font=self.font2,
                                       dropdown_fg_color="#559eef",
                                       dropdown_hover_color="#427cbd",
                                       dropdown_text_color="#545454",
                                       corner_radius=10, width=month_width, height=picker_height)
        self.year = ctk.CTkOptionMenu(self, values=self.years,
                                      font=self.font2, text_color="#545454",
                                      fg_color="#559eef", dropdown_font=self.font2,
                                      dropdown_fg_color="#559eef",
                                      dropdown_hover_color="#427cbd",
                                      dropdown_text_color="#545454",
                                      corner_radius=10, width=year_width, height=picker_height)
        # display date menu
        self.day.grid(row=0, column=0, padx=(0,spacing))
        self.month.grid(row=0, column=1, padx=(0,spacing))
        self.year.grid(row=0, column=2, padx=(0,0))

