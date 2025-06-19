# external/built-in modules/libs
import customtkinter as ctk
from datetime import datetime
# our modules/libs


class DatePicker(ctk.CTkFrame):
    def __init__(self, picker_height, spacing, rad, day_width, month_width, year_width, ctk_font,
                 menu_fg_color, menu_text_color, dropdown_ctk_font, dropdown_text_color, dropdown_fg_color,
                 dropdown_hover_color, btn_fg_color, btn_hover_color, master, **kwargs):
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
        self.year_menu = ctk.CTkOptionMenu(self, values=self.years,
                                      font=ctk_font, text_color=menu_text_color,
                                      fg_color=menu_fg_color, dropdown_font=dropdown_ctk_font,
                                      dropdown_fg_color=dropdown_fg_color,
                                      dropdown_hover_color=dropdown_hover_color,
                                      dropdown_text_color=dropdown_text_color, corner_radius=rad,
                                      button_color=btn_fg_color, button_hover_color=btn_hover_color,
                                      width=year_width, height=picker_height, 
                                      command=self.updateDaysFromYear)
        self.month_menu = ctk.CTkOptionMenu(self, values=self.months,
                                       font=ctk_font, text_color=menu_text_color,
                                       fg_color=menu_fg_color, dropdown_font=dropdown_ctk_font,
                                       dropdown_fg_color=dropdown_fg_color,
                                       dropdown_hover_color=dropdown_hover_color,
                                       dropdown_text_color=dropdown_text_color, corner_radius=rad,
                                      button_color=btn_fg_color, button_hover_color=btn_hover_color,
                                       width=month_width, height=picker_height,
                                       command=self.updateDaysFromMonth)
        self.day_menu = ctk.CTkOptionMenu(self, values=self.days,
                                     font=ctk_font, text_color=menu_text_color,
                                     fg_color=menu_fg_color, dropdown_font=dropdown_ctk_font,
                                     dropdown_fg_color=dropdown_fg_color,
                                     dropdown_hover_color=dropdown_hover_color,
                                     dropdown_text_color=dropdown_text_color,
                                      button_color=btn_fg_color, button_hover_color=btn_hover_color,
                                     corner_radius=rad, width=day_width, height=picker_height)
        # display date menu
        self.year_menu.grid(row=0, column=0, padx=(0,spacing))
        self.month_menu.grid(row=0, column=1, padx=(0,spacing))
        self.day_menu.grid(row=0, column=2, padx=(0,0))

    def updateDaysFromYear(self, year):
        month = self.month_menu.get()
        if month == "February":
            year = int(year)
            if (year % 4 == 0) and ( (year % 400 == 0) or (year % 100 != 0) ): # leap
                print("leap")
                self.day_menu.configure(values=self.days[:29]) # 29 days
            else:
                self.day_menu.configure(values=self.days[:28]) # 28 days
        elif month in ["January", "March", "May", "July", "August", "October", "December"]:
            self.day_menu.configure(values=self.days[:31]) # 31 days
        else:
            self.day_menu.configure(values=self.days[:30]) # 30 days
        self.day_menu.set(self.days[0])
    
    def updateDaysFromMonth(self, month):
        if month == "February":
            year = int(self.year_menu.get())
            if (year % 4 == 0) and ( (year % 400 == 0) or (year % 100 != 0) ): # leap
                print("leap")
                self.day_menu.configure(values=self.days[:29]) # 29 days
            else:
                self.day_menu.configure(values=self.days[:28]) # 28 days
        elif month in ["January", "March", "May", "July", "August", "October", "December"]:
            self.day_menu.configure(values=self.days[:31]) # 31 days
        else:
            self.day_menu.configure(values=self.days[:30]) # 30 days
        self.day_menu.set(self.days[0])




