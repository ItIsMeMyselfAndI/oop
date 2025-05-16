# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from frontend.utilities.date_picker import DatePicker 


FONT_SIZE_1 = 60
FONT_SIZE_2 = 50
FONT_SIZE_3 = 40
FONT_SIZE_4 = 30
FONT_SIZE_5 = 20

LIGHT_BLUE = "#cef2ff"
BLUE = "#559eef"
DARK_BLUE = "#427cbd"
LIGHT_GREY = "#c4c4c4"
GREY = "grey"
DARK_GREY = "#545454"
WHITE= "white"

ENTRY_W1 = 1430
ENTRY_W2 = 600
ENTRY_H = 60
MENU_W = 800
MENU_W = 800
MENU_H = 60
YEAR_MENU_W = 180
MONTH_MENU_W = 220
DAY_MENU_W = 180
PAD_X1 = 40
PAD_X2 = 30
PAD_X3 = 20
PAD_X4 = 20
PAD_X5 = 10
PAD_Y1 = 40
PAD_Y2 = 30
PAD_Y3 = 20
PAD_Y4 = 20
PAD_Y5 = 10
BTN_W = 350
BTN_H = 60
RAD = 20

# title section of the page
class Title(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_1, slant="italic", weight="normal")
        self.label = ctk.CTkLabel(self, text="Edit Transaction",
                                  font=self.font, text_color=DARK_GREY)
        self.label.pack(anchor="w")


# expense/savings/investment/income selection section of the page
class Selection(ctk.CTkFrame):
    def __init__(self, categories, transactions, master, **kwargs):
        super().__init__(master, **kwargs)
        self.isCurrentSelection = False
        # initialize fonts
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_3, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_4, slant="italic", weight="normal")
        # create guide frames
        self.frame1 = ctk.CTkFrame(self, fg_color=WHITE, corner_radius=0)
        self.frame2 = ctk.CTkFrame(self, fg_color=WHITE, corner_radius=0, height=100)
        self.frame3 = ctk.CTkFrame(self, fg_color=WHITE, corner_radius=0, height=100)
        # create frame 1 components
        self.transactionLabel = ctk.CTkLabel(self.frame1, text="Select Transaction",
                                             font=self.font1, text_color=DARK_GREY)
        self.transactionMenu = ctk.CTkOptionMenu(self.frame1, values=transactions,
                                                 font=self.font2, text_color=DARK_GREY,
                                                 fg_color=BLUE, dropdown_font=self.font2,
                                                 dropdown_fg_color=BLUE,
                                                 dropdown_hover_color=DARK_BLUE,
                                                 dropdown_text_color=DARK_GREY,
                                                 corner_radius=RAD, width=MENU_W, height=MENU_H)
        self.dateLabel = ctk.CTkLabel(self.frame1, text="Select New Date",
                                      font=self.font1, text_color=DARK_GREY)
        self.dateMenu = DatePicker(picker_height=MENU_H, spacing=PAD_X5, rad=RAD,
                                   day_width=DAY_MENU_W, month_width=MONTH_MENU_W, year_width=YEAR_MENU_W, 
                                   master=self.frame1, ctk_font=self.font2, fg_color=WHITE)
        # create frame 2 components
        self.categoryLabel = ctk.CTkLabel(self.frame2, text="Select New Category",
                                          font=self.font1, text_color=DARK_GREY)
        self.categoryMenu = ctk.CTkOptionMenu(self.frame2, values=categories,
                                                font=self.font2, text_color=DARK_GREY,
                                                width=MENU_W, fg_color=BLUE,
                                                dropdown_font=self.font2,
                                                dropdown_fg_color=BLUE,
                                                dropdown_hover_color=DARK_BLUE,
                                                dropdown_text_color=DARK_GREY,
                                                corner_radius=RAD, height=MENU_H)
        self.descriptionLabel = ctk.CTkLabel(self.frame2, text="Enter New Description",
                                             font=self.font1, text_color=DARK_GREY)
        self.descriptionEntry = ctk.CTkEntry(self.frame2, font=self.font2,
                                             text_color=DARK_GREY, fg_color=BLUE,
                                             corner_radius=RAD, width=ENTRY_W2, height=ENTRY_H,
                                             placeholder_text="Description",
                                             placeholder_text_color=GREY,
                                             border_width=0)
        # create frame 3 components
        self.amountLabel = ctk.CTkLabel(self.frame3, text="Enter New Amount",
                                        font=self.font1, text_color=DARK_GREY)
        self.amountEntry = ctk.CTkEntry(self.frame3, font=self.font2,
                                        text_color=DARK_GREY, fg_color=BLUE,
                                        corner_radius=RAD, width=ENTRY_W1, height=ENTRY_H,
                                        placeholder_text="Philippine Peso",
                                        placeholder_text_color=GREY,
                                        border_width=0)
        # display guide frames
        self.frame1.pack(fill="both", pady=(PAD_Y1,0))
        self.frame2.pack(fill="both", pady=(PAD_Y1,0))
        self.frame3.pack(fill="both", pady=PAD_Y1)
        # display frame 1 components
        self.transactionLabel.grid(row=0, column=0, sticky="w", padx=(PAD_X2,0), pady=(0,PAD_Y2))
        self.transactionMenu.grid(row=1, column=0, sticky="w", padx=(PAD_X2,0), pady=0)
        self.dateLabel.grid(row=0, column=1, sticky="w", padx=PAD_X2, pady=(0,PAD_Y2))
        self.dateMenu.grid(row=1, column=1, sticky="w", padx=PAD_X2, pady=0)
        # display frame 2 components
        self.categoryLabel.grid(row=0, column=0, sticky="w", padx=(PAD_X2,0), pady=(0,PAD_Y2))
        self.categoryMenu.grid(row=1, column=0, sticky="w", padx=(PAD_X2,0), pady=0)
        self.descriptionLabel.grid(row=0, column=1, sticky="w", padx=PAD_X2, pady=(0,PAD_Y2))
        self.descriptionEntry.grid(row=1, column=1, sticky="w", padx=PAD_X2, pady=0)
        # display frame 3 components
        self.amountLabel.pack(anchor="w", padx=PAD_X2, pady=(0,PAD_Y2))
        self.amountEntry.pack(anchor="w", padx=PAD_X2, pady=0)


# tabs section of the page
class Tabs(ctk.CTkFrame):
    def __init__(self, selections, master, **kwargs):
        super().__init__(master, **kwargs)
        self.selections = selections
        self.font = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_4, slant="italic", weight="normal")
        # create buttons/tabs
        self.expenseBtn = ctk.CTkButton(self, text="Expense", text_color=DARK_GREY,
                                        height=BTN_H, width=BTN_W,
                                        font=self.font, corner_radius=RAD,
                                        fg_color=WHITE, hover_color=LIGHT_GREY,
                                        command=self.on_click_expense)
        self.savingsBtn = ctk.CTkButton(self, text="Savings", text_color=DARK_GREY,
                                        height=BTN_H, width=BTN_W,
                                        font=self.font, corner_radius=RAD,
                                        fg_color=WHITE, hover_color=LIGHT_GREY,
                                        command=self.on_click_savings)
        self.investmentBtn = ctk.CTkButton(self, text="Investment", text_color=DARK_GREY,
                                           height=BTN_H, width=BTN_W,
                                           font=self.font, corner_radius=RAD,
                                           fg_color=WHITE, hover_color=LIGHT_GREY,
                                           command=self.on_click_investment)
        self.incomeBtn = ctk.CTkButton(self, text="Income", text_color=DARK_GREY,
                                       height=BTN_H, width=BTN_W,
                                       font=self.font, corner_radius=RAD,
                                       fg_color=WHITE, hover_color=LIGHT_GREY,
                                       command=self.on_click_income)
        # show buttons/tabs
        self.expenseBtn.grid(row=0, column=0, padx=(0, 0))
        self.savingsBtn.grid(row=0, column=1, padx=(PAD_X2, 0))
        self.investmentBtn.grid(row=0, column=2, padx=(PAD_X2, 0))
        self.incomeBtn.grid(row=0, column=3, padx=(PAD_X2,0))
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
        self.font = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_4, slant="italic", weight="normal")
        self.btn = ctk.CTkButton(self, width=BTN_W, height=BTN_H, text="Save Changes",
                                 font=self.font, text_color=WHITE,
                                 fg_color=BLUE, hover_color=DARK_BLUE,
                                 corner_radius=RAD, command=self.on_click_save)
        self.btn.pack()

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
        print(len(old_transaction)+3)
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
        
        # create page components
        self.title = Title(self, fg_color=LIGHT_BLUE, corner_radius=0)
        self.selection = ctk.CTkFrame(self, fg_color=LIGHT_BLUE, corner_radius=RAD)
        # create sub-pages
        self.expensePage = Selection(categories=expense_categories,
                                     transactions=self.f_all_type_transactions["expense"],
                                     master=self.selection, fg_color=WHITE, corner_radius=RAD)
        self.savingsPage = Selection(categories=savings_categories,
                                     transactions=self.f_all_type_transactions["savings"],
                                     master=self.selection, fg_color=WHITE, corner_radius=RAD)
        self.investmentPage = Selection(categories=investment_categories,
                                        transactions=self.f_all_type_transactions["investment"],
                                        master=self.selection, fg_color=WHITE, corner_radius=RAD)
        self.incomePage = Selection(categories=income_categories,
                                    transactions=self.f_all_type_transactions["income"],
                                    master=self.selection, fg_color=WHITE, corner_radius=RAD)
        self.selections = {
            "expense":self.expensePage, "savings":self.savingsPage,
            "investment":self.investmentPage, "income":self.incomePage
        }
        # create sub-pages tabs
        self.tabs = Tabs(selections=self.selections, master=self, fg_color=LIGHT_BLUE, corner_radius=0)
        # create save button
        self.save = Save(selections=self.selections, master=self, fg_color=LIGHT_BLUE, corner_radius=0)
        # show page components
        self.title.pack(anchor="w", padx=PAD_X1+PAD_X1, pady=(PAD_Y1+PAD_Y1,0))
        self.tabs.pack(padx=PAD_X2, pady=(PAD_Y1,0))
        self.selection.pack(padx=PAD_X2, pady=(PAD_Y2,0))
        self.save.pack(pady=PAD_Y1)

    def formatTransactionMenuOptions(self, transactions):
        # "f_" = "formatted_"
        f_transactions = []
        for t in transactions:
            f_t = f" {t.t_id} | {t.t_date} | {t.t_category} | {t.t_amount} | {t.t_description} "
            f_t = f"{f_t[:45]}..." if len(f_t) > 50 else f_t
            f_transactions.append(f_t)
        return f_transactions