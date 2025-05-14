import customtkinter as ctk
from frontend.utilities.date_picker import DatePicker


class AddTitle(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font = ctk.CTkFont(family="Bodoni MT", size=40, slant="italic", weight="normal")
        self.label = ctk.CTkLabel(self, text="Add Transaction",
                                 font=self.font, text_color="#545454")
        self.label.pack(side="left", padx=(20,0))


# same with class selection sa edit
class InputSection(ctk.CTkFrame):
    def __init__(self, categories, master, **kwargs):
        super().__init__(master, **kwargs)
        self.isCurrentSelection = False
        # initialize fonts
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=30, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=20, slant="italic", weight="normal")
        
        # create frames
        self.frame1 = ctk.CTkFrame(self, fg_color="white", corner_radius=10)
        self.frame2 = ctk.CTkFrame(self, fg_color="white", corner_radius=10, height=100)
        self.frame3 = ctk.CTkFrame(self, fg_color="white", corner_radius=10, height=100)
    
        # create frame 1 for date
        self.dateLabel = ctk.CTkLabel(self.frame1, text="Select Date",
                                    font=self.font1, text_color="#545454")
        self.dateMenu = DatePicker(picker_height=40, spacing=10,
                                   day_width=344, month_width=390, 
                                   year_width=344, master=self.frame1, 
                                   fg_color="white")
        
        # create frame 2 for category and description
        self.categoryLabel = ctk.CTkLabel(self.frame2, text="Select Category",
                                        font=self.font1, text_color="#545454")
        self.categoryMenu = ctk.CTkOptionMenu(self.frame2, values=categories,
                                            font=self.font2, text_color="#545454",
                                            width=680, fg_color="#559eef",
                                            dropdown_font=self.font2,
                                            dropdown_fg_color="#559eef",
                                            dropdown_hover_color="#427cbd",
                                            dropdown_text_color="#545454",
                                            corner_radius=10, height=40)
        self.descriptionLabel = ctk.CTkLabel(self.frame2, text="Enter Description",
                                           font=self.font1, text_color="#545454")
        self.descriptionEntry = ctk.CTkEntry(self.frame2, font=self.font2,
                                           text_color="#545454", fg_color="#559eef",
                                           corner_radius=10, width=400, height=40,
                                           placeholder_text="Description",
                                           placeholder_text_color="grey",
                                           border_width=0)
        
        # create frame 3 for amount
        self.amountLabel = ctk.CTkLabel(self.frame3, text="Enter Amount",
                                      font=self.font1, text_color="#545454")
        self.amountEntry = ctk.CTkEntry(self.frame3, font=self.font2,
                                      text_color="#545454", fg_color="#559eef",
                                      corner_radius=10, width=1100, height=40,
                                      placeholder_text="Philippine Peso",
                                      placeholder_text_color="grey",
                                      border_width=0)
        
        # guide frames
        self.frame1.pack(fill="both", pady=(10,10))
        self.frame2.pack(fill="both", pady=(0,10))
        self.frame3.pack(fill="both", pady=(0,10))
        
        # display frame 1 
        self.dateLabel.grid(row=0, column=0, sticky="w", pady=(20, 0), padx=(20, 0))
        self.dateMenu.grid(row=1, column=0, sticky="ew", pady=(20, 10), padx=(20, 20), columnspan=2)
        self.frame1.grid_columnconfigure(0, weight=1)  # Allow column to expand
        
        # display frame 2 
        self.categoryLabel.grid(row=0, column=0, sticky="w", pady=(20,0), padx=(20,0))
        self.categoryMenu.grid(row=1, column=0, sticky="w", pady=(20,10), padx=(20,0))
        self.descriptionLabel.grid(row=0, column=1, sticky="w", pady=(20,0), padx=(20,0))
        self.descriptionEntry.grid(row=1, column=1, sticky="w", pady=(20,10), padx=(20,20))
        
        # display frame 3 
        self.amountLabel.pack(anchor="w", pady=(20,0), padx=(20,0))
        self.amountEntry.pack(anchor="w", pady=(20,20), padx=(20,20))


class AddPageTabs(ctk.CTkFrame):
    def __init__(self, selections, master, **kwargs):
        super().__init__(master, **kwargs)
        self.selections = selections
        self.font = ctk.CTkFont(family="Bodoni MT", size=20, slant="italic", weight="normal")
      
        self.expenseBtn = ctk.CTkButton(self, text="Expense", text_color="#545454",
                                       height=40, width=366,
                                       font=self.font, corner_radius=10,
                                       fg_color="white", hover_color="#c4c4c4",
                                       command=self.on_click_expense)
        self.savingsBtn = ctk.CTkButton(self, text="Savings", text_color="#545454",
                                       height=40, width=366,
                                       font=self.font, corner_radius=10,
                                       fg_color="white", hover_color="#c4c4c4",
                                       command=self.on_click_savings)
        self.investmentBtn = ctk.CTkButton(self, text="Investment", text_color="#545454",
                                          height=40, width=366,
                                          font=self.font, corner_radius=10,
                                          fg_color="white", hover_color="#c4c4c4",
                                          command=self.on_click_investment)
        
        self.expenseBtn.grid(row=0, column=0, padx=(20, 0))
        self.savingsBtn.grid(row=0, column=1, padx=(20, 0))
        self.investmentBtn.grid(row=0, column=2, padx=(20, 20))
        
        self.selections["expense"].grid(row=2, column=0, sticky="nsew")
        self.selections["expense"].isCurrentSelection = True
        self.expenseBtn.configure(fg_color="#559eef", hover_color="#427cbd", text_color="white")

    def on_click_expense(self):
        self._switch_tab("expense", self.expenseBtn)

    def on_click_savings(self):
        self._switch_tab("savings", self.savingsBtn)

    def on_click_investment(self):
        self._switch_tab("investment", self.investmentBtn)

    # method for switching between tabs
    def _switch_tab(self, tab_name, button):
        # closes other selections
        for name, selection in self.selections.items():
            if name != tab_name:
                selection.grid_forget()
                selection.isCurrentSelection = False
        
        # reset all buttons
        for btn in [self.expenseBtn, self.savingsBtn, self.investmentBtn]:
            btn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        
        # open selected tab and style its button
        self.selections[tab_name].grid(row=2, column=0, sticky="nsew")
        self.selections[tab_name].isCurrentSelection = True
        button.configure(fg_color="#559eef", hover_color="#427cbd", text_color="white")


# Save section
class AddSave(ctk.CTkFrame):
    def __init__(self, selections, master, **kwargs):
        super().__init__(master, **kwargs)
        self.selections = selections 
        self.font = ctk.CTkFont(family="Bodoni MT", size=20, slant="italic", weight="normal")
        self.btn = ctk.CTkButton(self, width=270, height=40, text="Add Transaction",
                                font=self.font, text_color="white",
                                fg_color="#559eef", hover_color="#427cbd",
                                corner_radius=10, command=self.on_click_save)
        self.btn.pack(pady=(10,10))

    def on_click_save(self):
        for name, selection in self.selections.items():
            if selection.isCurrentSelection:
                transaction_type = name
                day = selection.dateMenu.day.get()
                month = selection.dateMenu.month.get()
                year = selection.dateMenu.year.get()
                category = selection.categoryMenu.get()
                description = selection.descriptionEntry.get()
                amount = selection.amountEntry.get()
                break
        
        print(f"\nAdding new {transaction_type} transaction:")
        print(f"Date: {day} {month} {year}")
        print(f"Category: {category}")
        print(f"Description: {description}")
        print(f"Amount: {amount}")

# main add page class
class Add(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(2, weight=1) # whole screen
        
        # nilagyan ko pala ng categories yung savings & investments
        # if not applicable, balik nalang sa dati
        expense_categories = ["Bills", "Education", "Entertainment", "Food & Drinks",
                             "Grocery", "Healthcare", "House", "Shopping",
                             "Transportation", "Wellness", "Other"]
        savings_categories = ["Monthly Allowance", "Change", "Miscellaneous"]
        investment_categories = ["Stocks", "Crypto", "Bonds", "Real Estate"]
        
        self.title = AddTitle(self, fg_color="#cef2ff", corner_radius=10)
        self.selection = ctk.CTkFrame(self, fg_color="#cef2ff", corner_radius=10)
        
        self.expensePage = InputSection(categories=expense_categories,
                                      master=self.selection, fg_color="white", corner_radius=10)
        self.savingsPage = InputSection(categories=savings_categories,
                                      master=self.selection, fg_color="white", corner_radius=10)
        self.investmentPage = InputSection(categories=investment_categories,
                                         master=self.selection, fg_color="white", corner_radius=10)
        
        self.selections = {
            "expense": self.expensePage,
            "savings": self.savingsPage,
            "investment": self.investmentPage
        }
        
        self.tabs = AddPageTabs(selections=self.selections, master=self, fg_color="#cef2ff", corner_radius=0)
        
        self.save = AddSave(selections=self.selections, master=self, fg_color="#cef2ff", corner_radius=10)
        
        self.title.pack(anchor="w", pady=(40,20))
        self.tabs.pack(pady=(10,10))
        self.selection.pack(pady=(10,10), padx=(20,20))
        self.save.pack(pady=(10,20))