# external/built-in modules/libs
import customtkinter as ctk


# our modules/libs
from frontend.features.date_picker.date_picker import DatePicker 


# title section of the page
class Title(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font = ctk.CTkFont(family="Bodoni MT", size=40, slant="italic", weight="normal")
        self.label = ctk.CTkLabel(self, text="Edit Transaction",
                                  font=self.font, text_color="#545454")
        self.label.pack(side="left", padx=(20,0))


# expense/savings/investment/income selection section of the page
class Selection(ctk.CTkFrame):
    def __init__(self, categories, transactions, master, **kwargs):
        super().__init__(master, **kwargs)
        self.isCurrentSelection = False
        # initialize fonts
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=30, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=20, slant="italic", weight="normal")
        # create guide frames
        self.frame1 = ctk.CTkFrame(self, fg_color="white", corner_radius=10)
        self.frame2 = ctk.CTkFrame(self, fg_color="white", corner_radius=10, height=100)
        self.frame3 = ctk.CTkFrame(self, fg_color="white", corner_radius=10, height=100)
        # create frame 1 components
        self.transactionLabel = ctk.CTkLabel(self.frame1, text="Select Transaction",
                                             font=self.font1, text_color="#545454")
        self.transactionMenu = ctk.CTkOptionMenu(self.frame1, values=transactions,
                                                 font=self.font2, text_color="#545454",
                                                 fg_color="#559eef", dropdown_font=self.font2,
                                                 dropdown_fg_color="#559eef",
                                                 dropdown_hover_color="#427cbd",
                                                 dropdown_text_color="#545454",
                                                 corner_radius=10, width=680, height=40)
        self.dateLabel = ctk.CTkLabel(self.frame1, text="New Date",
                                      font=self.font1, text_color="#545454")
        self.dateMenu = DatePicker(picker_height=40, spacing=10,
                                   day_width=120, month_width=140, year_width=120, 
                                   master=self.frame1, fg_color="white")
        # create frame 2 components
        self.categoryLabel = ctk.CTkLabel(self.frame2, text="Select New Category",
                                          font=self.font1, text_color="#545454")
        self.categoryMenu = ctk.CTkOptionMenu(self.frame2, values=categories,
                                                font=self.font2, text_color="#545454",
                                                width=680, fg_color="#559eef",
                                                dropdown_font=self.font2,
                                                dropdown_fg_color="#559eef",
                                                dropdown_hover_color="#427cbd",
                                                dropdown_text_color="#545454",
                                                corner_radius=10, height=40)
        self.descriptionLabel = ctk.CTkLabel(self.frame2, text="New Description",
                                             font=self.font1, text_color="#545454")
        self.descriptionEntry = ctk.CTkEntry(self.frame2, font=self.font2,
                                             text_color="#545454", fg_color="#559eef",
                                             corner_radius=10, width=400, height=40,
                                             placeholder_text="Description",
                                             placeholder_text_color="grey",
                                             border_width=0)
        # create frame 3 components
        self.amountLabel = ctk.CTkLabel(self.frame3, text="New Amount",
                                        font=self.font1, text_color="#545454")
        self.amountEntry = ctk.CTkEntry(self.frame3, font=self.font2,
                                        text_color="#545454", fg_color="#559eef",
                                        corner_radius=10, width=1100, height=40,
                                        placeholder_text="Philippine Peso",
                                        placeholder_text_color="grey",
                                        border_width=0)
        # display guide frames
        self.frame1.pack(fill="both", pady=(10,10))
        self.frame2.pack(fill="both", pady=(0,10))
        self.frame3.pack(fill="both", pady=(0,10))
        # display frame 1 components
        self.transactionLabel.grid(row=0, column=0, sticky="w", pady=(10,0), padx=(20,0))
        self.transactionMenu.grid(row=1, column=0, sticky="w", pady=(20,10), padx=(20,0))
        self.dateLabel.grid(row=0, column=1, sticky="w", pady=(20,0), padx=(20,0))
        self.dateMenu.grid(row=1, column=1, sticky="w", pady=(20,10), padx=(20,20))
        # display frame 2 components
        self.categoryLabel.grid(row=0, column=0, sticky="w", pady=(20,0), padx=(20,0))
        self.categoryMenu.grid(row=1, column=0, sticky="w", pady=(20,10), padx=(20,0))
        self.descriptionLabel.grid(row=0, column=1, sticky="w", pady=(20,0), padx=(20,0))
        self.descriptionEntry.grid(row=1, column=1, sticky="w", pady=(20,10), padx=(20,20))
        # display frame 3 components
        self.amountLabel.pack(anchor="w", pady=(20,0), padx=(20,0))
        self.amountEntry.pack(anchor="w", pady=(20,20), padx=(20,20))


# tabs section of the page
class Tabs(ctk.CTkFrame):
    def __init__(self, selections, master, **kwargs):
        super().__init__(master, **kwargs)
        self.selections = selections
        self.font = ctk.CTkFont(family="Bodoni MT", size=20, slant="italic", weight="normal")
        # create buttons/tabs
        self.expenseBtn = ctk.CTkButton(self, text="Expense", text_color="#545454",
                                        height=40, width=270,
                                        font=self.font, corner_radius=10,
                                        fg_color="white", hover_color="#c4c4c4",
                                        command=self.on_click_expense)
        self.savingsBtn = ctk.CTkButton(self, text="Savings", text_color="#545454",
                                        height=40, width=270,
                                        font=self.font, corner_radius=10,
                                        fg_color="white", hover_color="#c4c4c4",
                                        command=self.on_click_savings)
        self.investmentBtn = ctk.CTkButton(self, text="Investment", text_color="#545454",
                                           height=40, width=270,
                                           font=self.font, corner_radius=10,
                                           fg_color="white", hover_color="#c4c4c4",
                                           command=self.on_click_investment)
        self.incomeBtn = ctk.CTkButton(self, text="Income", text_color="#545454",
                                       height=40, width=270,
                                       font=self.font, corner_radius=10,
                                       fg_color="white", hover_color="#c4c4c4",
                                       command=self.on_click_income)
        # show buttons/tabs
        self.expenseBtn.grid(row=0, column=0, padx=(20, 0))
        self.savingsBtn.grid(row=0, column=1, padx=(20, 0))
        self.investmentBtn.grid(row=0, column=2, padx=(20, 0))
        self.incomeBtn.grid(row=0, column=3, padx=(20, 20))
        # open default tab (expense)
        self.selections["expense"].grid(row=2, column=0, sticky="nsew")
        self.selections["expense"].isCurrentSelection = True
        self.expenseBtn.configure(fg_color="#559eef", hover_color="#427cbd", text_color="white")

    def on_click_expense(self):
        # close other selections
        self.selections["savings"].grid_forget()
        self.selections["investment"].grid_forget()
        self.selections["income"].grid_forget()
        # reset fg, hover & text color of other buttons
        self.savingsBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        self.investmentBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        self.incomeBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        # open expense and change fg, hover & text color
        self.selections["expense"].grid(row=2, column=0, sticky="nsew")
        self.selections["expense"].isCurrentSelection = True
        self.expenseBtn.configure(fg_color="#559eef", hover_color="#427cbd", text_color="white")

    def on_click_savings(self):
        # close other selections
        self.selections["expense"].grid_forget()
        self.selections["investment"].grid_forget()
        self.selections["income"].grid_forget()
        # reset fg, hover & text color of other buttons
        self.expenseBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        self.investmentBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        self.incomeBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        self.selections["expense"].isCurrentSelection = False 
        self.selections["investment"].isCurrentSelection = False
        self.selections["income"].isCurrentSelection = False
        # open savings and change fg, hover & text color
        self.selections["savings"].grid(row=2, column=0, sticky="nsew")
        self.selections["savings"].isCurrentSelection = True
        self.savingsBtn.configure(fg_color="#559eef", hover_color="#427cbd", text_color="white")

    def on_click_investment(self):
        # close other selections
        self.selections["expense"].grid_forget()
        self.selections["savings"].grid_forget()
        self.selections["income"].grid_forget()
        # reset fg, hover & text color of other buttons
        self.expenseBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        self.savingsBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        self.incomeBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        # set other selections isCurrentSelection to false
        self.selections["expense"].isCurrentSelection = False 
        self.selections["savings"].isCurrentSelection = False
        self.selections["income"].isCurrentSelection = False
        # open investment and change fg, hover & text color
        self.selections["investment"].grid(row=2, column=0, sticky="nsew")
        self.selections["investment"].isCurrentSelection = True
        self.investmentBtn.configure(fg_color="#559eef", hover_color="#427cbd", text_color="white")

    def on_click_income(self):
        # close other selections
        self.selections["expense"].grid_forget()
        self.selections["savings"].grid_forget()
        self.selections["investment"].grid_forget()
        # reset fg, hover & text color of other buttons
        self.expenseBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        self.savingsBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        self.investmentBtn.configure(fg_color="white", hover_color="#c4c4c4", text_color="#545454")
        # set other selections isCurrentSelection to false
        self.selections["expense"].isCurrentSelection = False 
        self.selections["savings"].isCurrentSelection = False
        self.selections["investment"].isCurrentSelection = False
        # open income and change fg, hover & text color
        self.selections["income"].grid(row=2, column=0, sticky="nsew")
        self.selections["income"].isCurrentSelection = True
        self.incomeBtn.configure(fg_color="#559eef", hover_color="#427cbd", text_color="white")


# save section of the page
class Save(ctk.CTkFrame):
    def __init__(self, selections, master, **kwargs):
        super().__init__(master, **kwargs)
        self.selections = selections 
        self.font = ctk.CTkFont(family="Bodoni MT", size=20, slant="italic", weight="normal")
        self.btn = ctk.CTkButton(self, width=270, height=40, text="Save Changes",
                                 font=self.font, text_color="white",
                                 fg_color="#559eef", hover_color="#427cbd",
                                 corner_radius=10, command=self.on_click_save)
        self.btn.pack(pady=(10,10))

    def on_click_save(self):
        for name, selection in self.selections.items():
            if selection.isCurrentSelection == True:
                selection_type = name
                transaction = selection.transactionMenu.get()
                day = selection.dateMenu.day.get()
                month = selection.dateMenu.month.get()
                year = selection.dateMenu.year.get()
                category = selection.categoryMenu.get()
                description = selection.descriptionEntry.get()
                amount = selection.amountEntry.get()
                break
        print()
        print(f"{selection_type = }")
        print(f"{transaction = }")
        print(f"new date = {day} {month} {year}")
        print(f"new {category = }")
        print(f"new {description = }")
        print(f"new {amount = }")


# main edit page
class Edit(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(2, weight=1) # whole screen
        # valid categories
        expense_categories = ["Bills", "Education", "Entertainment", "Food & Drinks",
                              "Grocery", "Healthcare", "House", "Shopping",
                              "Transportation", "Wellness", "Other"]
        other_categories = ["Savings (unchangeable)",
                            "Investment (unchangeable)",
                            "Income (unchangeable)"]
        # sample expense transactions 
        expense_transactions = ["01 January 2023  |  Food  |  P100",
                                "02 February 2024  |  Bills  |  P100",
                                "03 March 2024  |  Education  |  P100"]
        # sample savings/investment/income expense transactions 
        other_transactions = ["01 January 2023  |  P100  |  Description 1",
                              "02 February 2024  |  P100  |  Description 2",
                              "03 March 2024  |  P100  |  Description 3"]
        # create page components
        self.title = Title(self, fg_color="#cef2ff", corner_radius=10)
        self.selection = ctk.CTkFrame(self, fg_color="#cef2ff", corner_radius=10)
        # create sub-pages
        self.expensePage = Selection(categories=expense_categories, transactions=expense_transactions,
                                     master=self.selection, fg_color="white", corner_radius=10)
        self.savingsPage = Selection(categories=other_categories[0:1], transactions=other_transactions,
                                     master=self.selection, fg_color="white", corner_radius=10)
        self.investmentPage = Selection(categories=other_categories[1:2], transactions=other_transactions,
                                        master=self.selection, fg_color="white", corner_radius=10)
        self.incomePage = Selection(categories=other_categories[2:3], transactions=other_transactions,
                                    master=self.selection, fg_color="white", corner_radius=10)
        self.selections = {
            "expense":self.expensePage, "savings":self.savingsPage,
            "investment":self.investmentPage, "income":self.incomePage
        }
        # create sub-pages tabs
        self.tabs = Tabs(selections=self.selections, master=self, fg_color="#cef2ff", corner_radius=0)
        # create save button
        self.save = Save(selections=self.selections, master=self, fg_color="#cef2ff", corner_radius=10)
        # show page components
        self.title.pack(anchor="w", pady=(40,20))
        self.tabs.pack(pady=(10,10))
        self.selection.pack(pady=(10,10), padx=(20,20))
        self.save.pack(pady=(10,20))