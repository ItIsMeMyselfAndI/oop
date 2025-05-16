# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from frontend.utilities.date_picker import DatePicker 

LIGHT_BLUE = "#cef2ff"
BLUE = "#559eef"
DARK_BLUE = "#427cbd"
LIGHT_GREY = "#c4c4c4"
GREY = "grey"
DARK_GREY = "#545454"
WHITE= "white"

# title section of the page
class Title(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font = ctk.CTkFont(family="Bodoni MT", size=40, slant="italic", weight="normal")
        self.label = ctk.CTkLabel(self, text="Edit Transaction",
                                  font=self.font, text_color=DARK_GREY)
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
        self.frame1 = ctk.CTkFrame(self, fg_color=WHITE, corner_radius=10)
        self.frame2 = ctk.CTkFrame(self, fg_color=WHITE, corner_radius=10, height=100)
        self.frame3 = ctk.CTkFrame(self, fg_color=WHITE, corner_radius=10, height=100)
        # create frame 1 components
        self.transactionLabel = ctk.CTkLabel(self.frame1, text="Select Transaction",
                                             font=self.font1, text_color=DARK_GREY)
        self.transactionMenu = ctk.CTkOptionMenu(self.frame1, values=transactions,
                                                 font=self.font2, text_color=DARK_GREY,
                                                 fg_color=BLUE, dropdown_font=self.font2,
                                                 dropdown_fg_color=BLUE,
                                                 dropdown_hover_color=DARK_BLUE,
                                                 dropdown_text_color=DARK_GREY,
                                                 corner_radius=10, width=680, height=40)
        self.dateLabel = ctk.CTkLabel(self.frame1, text="Select New Date",
                                      font=self.font1, text_color=DARK_GREY)
        self.dateMenu = DatePicker(picker_height=40, spacing=10,
                                   day_width=120, month_width=140, year_width=120, 
                                   master=self.frame1, fg_color=WHITE)
        # create frame 2 components
        self.categoryLabel = ctk.CTkLabel(self.frame2, text="Select New Category",
                                          font=self.font1, text_color=DARK_GREY)
        self.categoryMenu = ctk.CTkOptionMenu(self.frame2, values=categories,
                                                font=self.font2, text_color=DARK_GREY,
                                                width=680, fg_color=BLUE,
                                                dropdown_font=self.font2,
                                                dropdown_fg_color=BLUE,
                                                dropdown_hover_color=DARK_BLUE,
                                                dropdown_text_color=DARK_GREY,
                                                corner_radius=10, height=40)
        self.descriptionLabel = ctk.CTkLabel(self.frame2, text="Enter New Description",
                                             font=self.font1, text_color=DARK_GREY)
        self.descriptionEntry = ctk.CTkEntry(self.frame2, font=self.font2,
                                             text_color=DARK_GREY, fg_color=BLUE,
                                             corner_radius=10, width=400, height=40,
                                             placeholder_text="Description",
                                             placeholder_text_color=GREY,
                                             border_width=0)
        # create frame 3 components
        self.amountLabel = ctk.CTkLabel(self.frame3, text="Enter New Amount",
                                        font=self.font1, text_color=DARK_GREY)
        self.amountEntry = ctk.CTkEntry(self.frame3, font=self.font2,
                                        text_color=DARK_GREY, fg_color=BLUE,
                                        corner_radius=10, width=1100, height=40,
                                        placeholder_text="Philippine Peso",
                                        placeholder_text_color=GREY,
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
        self.expenseBtn = ctk.CTkButton(self, text="Expense", text_color=DARK_GREY,
                                        height=40, width=270,
                                        font=self.font, corner_radius=10,
                                        fg_color=WHITE, hover_color=LIGHT_GREY,
                                        command=self.on_click_expense)
        self.savingsBtn = ctk.CTkButton(self, text="Savings", text_color=DARK_GREY,
                                        height=40, width=270,
                                        font=self.font, corner_radius=10,
                                        fg_color=WHITE, hover_color=LIGHT_GREY,
                                        command=self.on_click_savings)
        self.investmentBtn = ctk.CTkButton(self, text="Investment", text_color=DARK_GREY,
                                           height=40, width=270,
                                           font=self.font, corner_radius=10,
                                           fg_color=WHITE, hover_color=LIGHT_GREY,
                                           command=self.on_click_investment)
        self.incomeBtn = ctk.CTkButton(self, text="Income", text_color=DARK_GREY,
                                       height=40, width=270,
                                       font=self.font, corner_radius=10,
                                       fg_color=WHITE, hover_color=LIGHT_GREY,
                                       command=self.on_click_income)
        # show buttons/tabs
        self.expenseBtn.grid(row=0, column=0, padx=(20, 0))
        self.savingsBtn.grid(row=0, column=1, padx=(20, 0))
        self.investmentBtn.grid(row=0, column=2, padx=(20, 0))
        self.incomeBtn.grid(row=0, column=3, padx=(20, 20))
        # open default tab (expense)
        self.on_click_expense()
        # self.selections["expense"].grid(row=2, column=0, sticky="nsew")
        # self.selections["expense"].isCurrentSelection = True
        # self.expenseBtn.configure(fg_color=BLUE, hover_color=DARK_BLUE, text_color=WHITE)

    def on_click_expense(self):
        # close other selections
        self.selections["savings"].grid_forget()
        self.selections["investment"].grid_forget()
        self.selections["income"].grid_forget()
        # reset fg, hover & text color of other buttons
        self.savingsBtn.configure(fg_color=WHITE, hover_color=LIGHT_GREY, text_color=DARK_GREY)
        self.investmentBtn.configure(fg_color=WHITE, hover_color=LIGHT_GREY, text_color=DARK_GREY)
        self.incomeBtn.configure(fg_color=WHITE, hover_color=LIGHT_GREY, text_color=DARK_GREY)
        # open expense and change fg, hover & text color
        self.selections["expense"].grid(row=2, column=0, sticky="nsew")
        self.selections["expense"].isCurrentSelection = True
        self.expenseBtn.configure(fg_color=BLUE, hover_color=DARK_BLUE, text_color=WHITE)

    def on_click_savings(self):
        # close other selections
        self.selections["expense"].grid_forget()
        self.selections["investment"].grid_forget()
        self.selections["income"].grid_forget()
        # reset fg, hover & text color of other buttons
        self.expenseBtn.configure(fg_color=WHITE, hover_color=LIGHT_GREY, text_color=DARK_GREY)
        self.investmentBtn.configure(fg_color=WHITE, hover_color=LIGHT_GREY, text_color=DARK_GREY)
        self.incomeBtn.configure(fg_color=WHITE, hover_color=LIGHT_GREY, text_color=DARK_GREY)
        self.selections["expense"].isCurrentSelection = False 
        self.selections["investment"].isCurrentSelection = False
        self.selections["income"].isCurrentSelection = False
        # open savings and change fg, hover & text color
        self.selections["savings"].grid(row=2, column=0, sticky="nsew")
        self.selections["savings"].isCurrentSelection = True
        self.savingsBtn.configure(fg_color=BLUE, hover_color=DARK_BLUE, text_color=WHITE)

    def on_click_investment(self):
        # close other selections
        self.selections["expense"].grid_forget()
        self.selections["savings"].grid_forget()
        self.selections["income"].grid_forget()
        # reset fg, hover & text color of other buttons
        self.expenseBtn.configure(fg_color=WHITE, hover_color=LIGHT_GREY, text_color=DARK_GREY)
        self.savingsBtn.configure(fg_color=WHITE, hover_color=LIGHT_GREY, text_color=DARK_GREY)
        self.incomeBtn.configure(fg_color=WHITE, hover_color=LIGHT_GREY, text_color=DARK_GREY)
        # set other selections isCurrentSelection to false
        self.selections["expense"].isCurrentSelection = False 
        self.selections["savings"].isCurrentSelection = False
        self.selections["income"].isCurrentSelection = False
        # open investment and change fg, hover & text color
        self.selections["investment"].grid(row=2, column=0, sticky="nsew")
        self.selections["investment"].isCurrentSelection = True
        self.investmentBtn.configure(fg_color=BLUE, hover_color=DARK_BLUE, text_color=WHITE)

    def on_click_income(self):
        # close other selections
        self.selections["expense"].grid_forget()
        self.selections["savings"].grid_forget()
        self.selections["investment"].grid_forget()
        # reset fg, hover & text color of other buttons
        self.expenseBtn.configure(fg_color=WHITE, hover_color=LIGHT_GREY, text_color=DARK_GREY)
        self.savingsBtn.configure(fg_color=WHITE, hover_color=LIGHT_GREY, text_color=DARK_GREY)
        self.investmentBtn.configure(fg_color=WHITE, hover_color=LIGHT_GREY, text_color=DARK_GREY)
        # set other selections isCurrentSelection to false
        self.selections["expense"].isCurrentSelection = False 
        self.selections["savings"].isCurrentSelection = False
        self.selections["investment"].isCurrentSelection = False
        # open income and change fg, hover & text color
        self.selections["income"].grid(row=2, column=0, sticky="nsew")
        self.selections["income"].isCurrentSelection = True
        self.incomeBtn.configure(fg_color=BLUE, hover_color=DARK_BLUE, text_color=WHITE)


# save section of the page
class Save(ctk.CTkFrame):
    def __init__(self, selections, master, **kwargs):
        super().__init__(master, **kwargs)
        self.selections = selections 
        self.font = ctk.CTkFont(family="Bodoni MT", size=20, slant="italic", weight="normal")
        self.btn = ctk.CTkButton(self, width=270, height=40, text="Save Changes",
                                 font=self.font, text_color=WHITE,
                                 fg_color=BLUE, hover_color=DARK_BLUE,
                                 corner_radius=10, command=self.on_click_save)
        self.btn.pack(pady=(10,10))

    def on_click_save(self):
        month_2_numeric = {"January":"01", "February":"02", "March":"03", "April":"04",
                           "May":"05", "June":"06", "July":"07", "August":"08",
                           "September":"09", "October":"10", "November":"11", "December":"12"}
        for transaction_type, selection in self.selections.items():
            if selection.isCurrentSelection == True:
                old_transaction = selection.transactionMenu.get().strip()
                transaction_id = int(old_transaction.split()[0])
                year = selection.dateMenu.year.get()
                month = month_2_numeric[selection.dateMenu.month.get()]
                day = selection.dateMenu.day.get()
                new_date = f"{year}-{month}-{day}"
                new_category = selection.categoryMenu.get()
                new_description = selection.descriptionEntry.get()
                new_amount = selection.amountEntry.get()
                break
        print()
        print(f"{old_transaction = }")
        print(f"{transaction_type = }")
        print(f"{transaction_id = }")
        print(f"{new_date = }")
        print(f"{new_category = }")
        print(f"{new_description = }")
        print(f"{new_amount = }")


# main edit page
class Edit(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        # valid categories
        expense_categories = ["Bills", "Education", "Entertainment", "Food & Drinks",
                              "Grocery", "Healthcare", "House", "Shopping",
                              "Transportation", "Wellness", "Other"]
        savings_categories = ["Monthly Allowance", "Change", "Miscellaneous"]
        investment_categories = ["Stocks", "Crypto", "Bonds", "Real Estate"]
        income_categories = ["Salary", "Bonus", "Side-hustles", "Tips"]
        # get all transactions by type from the db
        self.tm = tm
        self.all_type_transactions = self.tm.repo.getAllTransactionsByType(self.user_id)
        # format transactions for display ("f_" = "formatted_")
        self.f_all_type_transactions = {}
        for t_type, transactions in self.all_type_transactions.items():
            f_transactions = self.formatTransactionMenuOptions(transactions)
            self.f_all_type_transactions[t_type] = f_transactions
        # whole screen
        self.grid_columnconfigure(2, weight=1)
        # create page components
        self.title = Title(self, fg_color=LIGHT_BLUE, corner_radius=10)
        self.selection = ctk.CTkFrame(self, fg_color=LIGHT_BLUE, corner_radius=10)
        # create sub-pages
        self.expensePage = Selection(categories=expense_categories,
                                     transactions=self.f_all_type_transactions["expense"],
                                     master=self.selection, fg_color=WHITE, corner_radius=10)
        self.savingsPage = Selection(categories=savings_categories,
                                     transactions=self.f_all_type_transactions["savings"],
                                     master=self.selection, fg_color=WHITE, corner_radius=10)
        self.investmentPage = Selection(categories=investment_categories,
                                        transactions=self.f_all_type_transactions["investment"],
                                        master=self.selection, fg_color=WHITE, corner_radius=10)
        self.incomePage = Selection(categories=income_categories,
                                    transactions=self.f_all_type_transactions["income"],
                                    master=self.selection, fg_color=WHITE, corner_radius=10)
        self.selections = {
            "expense":self.expensePage, "savings":self.savingsPage,
            "investment":self.investmentPage, "income":self.incomePage
        }
        # create sub-pages tabs
        self.tabs = Tabs(selections=self.selections, master=self, fg_color=LIGHT_BLUE, corner_radius=0)
        # create save button
        self.save = Save(selections=self.selections, master=self, fg_color=LIGHT_BLUE, corner_radius=10)
        # show page components
        self.title.pack(anchor="w", pady=(40,20))
        self.tabs.pack(pady=(10,10))
        self.selection.pack(pady=(10,10), padx=(20,20))
        self.save.pack(pady=(10,20))

    def formatTransactionMenuOptions(self, transactions):
        # "f_" = "formatted_"
        f_transactions = []
        for t in transactions:
            t_description = f"{t.t_description[:20]}..." if len(t.t_description) > 20 else t.t_description
            f_t = f" {t.t_id} | {t.t_date} | {t.t_category} | {t.t_amount} | {t_description} "
            f_transactions.append(f_t)
        return f_transactions