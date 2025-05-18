# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from frontend.utilities.date_picker import DatePicker
from backend.transaction_manager import Transaction


FONT_SIZE_1 = 25
FONT_SIZE_2 = 30
FONT_SIZE_3 = 40
FONT_SIZE_4 = 50
FONT_SIZE_5 = 60

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

MENU_W1 = 800
MENU_W2 = 1360 
MENU_H = 60

YEAR_MENU_W = 450
MONTH_MENU_W = 500 
DAY_MENU_W = 450

PAD_X1 = 10
PAD_X2 = 20
PAD_X3 = 20
PAD_X4 = 30
PAD_X5 = 40

PAD_Y5 = 40
PAD_Y4 = 30
PAD_Y3 = 20
PAD_Y2 = 20
PAD_Y1 = 10

BTN_W = 350
BTN_H = 60

RAD = 20


# header section
class AddHeader(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_5, slant="italic", weight="normal")
        self.label = ctk.CTkLabel(self, text="Add Transaction",
                                  font=self.font, text_color=DARK_GREY)
        self.label.pack(anchor="w")


# same with class selection sa edit
class AddTransactionForm(ctk.CTkFrame):
    def __init__(self, tm, user_id, t_type, categories, master, **kwargs):
        super().__init__(master, **kwargs)
        # initialize transaction options
        self.tm = tm
        self.user_id = user_id
        self.t_type = t_type
        # initialize state
        self.isCurrentEditTransactionForm = False
        # initialize fonts
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_3, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_2, slant="italic", weight="normal")
        self.font3 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_1, slant="italic", weight="normal")
        # create guide frames
        self.frame1 = ctk.CTkFrame(self, fg_color=WHITE, corner_radius=0)
        self.frame2 = ctk.CTkFrame(self, fg_color=WHITE, corner_radius=0)
        self.frame3 = ctk.CTkFrame(self, fg_color=WHITE, corner_radius=0)
        # create frame 1 components
        self.dateLabel = ctk.CTkLabel(self.frame1, text="Select Date",
                                      font=self.font1, text_color=DARK_GREY)
        self.dateMenu = DatePicker(picker_height=MENU_H, spacing=PAD_X1, rad=RAD,
                                   day_width=DAY_MENU_W, month_width=MONTH_MENU_W, year_width=YEAR_MENU_W, 
                                   master=self.frame1, ctk_font=self.font3, dropdown_ctk_font=self.font2,
                                   fg_color=WHITE)
        # create frame 2 components
        self.categoryLabel = ctk.CTkLabel(self.frame2, text="Select Category",
                                          font=self.font1, text_color=DARK_GREY)
        self.categoryMenu = ctk.CTkOptionMenu(self.frame2, values=categories,
                                                font=self.font3, text_color=DARK_GREY,
                                                width=MENU_W1, fg_color=BLUE,
                                                dropdown_font=self.font2,
                                                dropdown_fg_color=BLUE,
                                                dropdown_hover_color=DARK_BLUE,
                                                dropdown_text_color=DARK_GREY,
                                                corner_radius=RAD, height=MENU_H)
        self.descriptionLabel = ctk.CTkLabel(self.frame2, text="Enter Description",
                                             font=self.font1, text_color=DARK_GREY)
        self.descriptionEntry = ctk.CTkEntry(self.frame2, font=self.font3,
                                             text_color=DARK_GREY, fg_color=BLUE,
                                             corner_radius=RAD, width=ENTRY_W2, height=ENTRY_H,
                                             placeholder_text="Description",
                                             placeholder_text_color=GREY,
                                             border_width=0)
        # create frame 3 components
        self.amountLabel = ctk.CTkLabel(self.frame3, text="Enter Amount",
                                        font=self.font1, text_color=DARK_GREY)
        self.amountEntry = ctk.CTkEntry(self.frame3, font=self.font3,
                                        text_color=DARK_GREY, fg_color=BLUE,
                                        corner_radius=RAD, width=ENTRY_W1, height=ENTRY_H,
                                        placeholder_text="Philippine Peso",
                                        placeholder_text_color=GREY,
                                        border_width=0)
        # display guide frames
        self.frame1.pack(fill="both", pady=(PAD_Y5,0))
        self.frame2.pack(fill="both", pady=(PAD_Y5,0))
        self.frame3.pack(fill="both", pady=PAD_Y5)
        # display frame 1 
        self.dateLabel.grid(row=0, column=0, sticky="w", padx=PAD_X4, pady=(0,PAD_Y4))
        self.dateMenu.grid(row=1, column=0, sticky="w", padx=PAD_X4, pady=0)
        # display frame 2 
        self.categoryLabel.grid(row=0, column=0, sticky="w", padx=(PAD_X4,0), pady=(0,PAD_Y4))
        self.categoryMenu.grid(row=1, column=0, sticky="w", padx=(PAD_X4,0), pady=0)
        self.descriptionLabel.grid(row=0, column=1, sticky="w", padx=PAD_X4, pady=(0,PAD_Y4))
        self.descriptionEntry.grid(row=1, column=1, sticky="w", padx=PAD_X4, pady=0)
        # display frame 3 
        self.amountLabel.pack(anchor="w", padx=PAD_X4, pady=(0,PAD_Y4))
        self.amountEntry.pack(anchor="w", padx=PAD_X4, pady=0)
    

class AddPageTabs(ctk.CTkFrame):
    def __init__(self, transactionForms, master, **kwargs):
        super().__init__(master, **kwargs)
        self.transactionForms = transactionForms
        self.font = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_2, slant="italic", weight="normal")
        # create buttons/tabs
        self.expenseBTN = self.createTabButton(text="Expense", command=self.onClickExpenseTab)
        self.savingsBTN = self.createTabButton(text="Savings", command=self.onClickSavingsTab)
        self.investmentBTN = self.createTabButton(text="Investment", command=self.onClickInvestmentTab)
        self.incomeBTN = self.createTabButton(text="Income", command=self.onClickIncomeTab)
        self.tabBTNs = {
            "expense":self.expenseBTN, "savings":self.savingsBTN,
            "investment":self.investmentBTN, "income":self.incomeBTN
        }
        # show buttons/tabs
        self.expenseBTN.grid(row=0, column=0, padx=(0, 0))
        self.savingsBTN.grid(row=0, column=1, padx=(PAD_X4, 0))
        self.investmentBTN.grid(row=0, column=2, padx=(PAD_X4, 0))
        self.incomeBTN.grid(row=0, column=3, padx=(PAD_X4,0))
        # open default tab (expense)
        self._switchPageTo("expense")

    def createTabButton(self, text, command):
        btn = ctk.CTkButton(self, text=text, text_color=DARK_GREY, height=BTN_H, width=BTN_W,
                            font=self.font, corner_radius=RAD, fg_color=WHITE, hover_color=LIGHT_GREY,
                            command=command)
        return btn
    
    def onClickExpenseTab(self): self._switchPageTo("expense")
    def onClickSavingsTab(self): self._switchPageTo("savings")
    def onClickInvestmentTab(self): self._switchPageTo("investment")
    def onClickIncomeTab(self): self._switchPageTo("income")
    
    # method for switching between tabs
    def _switchPageTo(self, transaction_type):
        for t_type, form in self.transactionForms.items():
            # set all transaction forms's isCurrentEditTransactionForm attr to false
            form.isCurrentEditTransactionForm = False
            # close all transaction forms
            form.grid_forget()
            # reset all buttons
            self.tabBTNs[t_type].configure(fg_color=WHITE, hover_color=LIGHT_GREY, text_color=DARK_GREY)
        # open selected and change fg, hover & text color
        self.transactionForms[transaction_type].isCurrentEditTransactionForm = True
        self.transactionForms[transaction_type].grid(row=2, column=0, sticky="nsew")
        self.tabBTNs[transaction_type].configure(fg_color=BLUE, hover_color=DARK_BLUE, text_color=WHITE)


# main add page class
class Add(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize state
        self.isCurrentPage = False
        # create page sections 
        self.title = AddHeader(self, fg_color=LIGHT_BLUE, corner_radius=0)
        self.forms_section = ctk.CTkFrame(self, fg_color=LIGHT_BLUE, corner_radius=RAD)
        # create transaction forms
        self.expenseForm = self.createAddTransactionForm("expense")
        self.savingsForm = self.createAddTransactionForm("savings")
        self.investmentForm = self.createAddTransactionForm("investment")
        self.incomeForm = self.createAddTransactionForm("income")
        self.transactionForms = {
            "expense":self.expenseForm, "savings":self.savingsForm,
            "investment":self.investmentForm, "income":self.incomeForm
        }
        # create sub-pages tabs
        self.tabs = AddPageTabs(transactionForms=self.transactionForms, master=self,
                         fg_color=LIGHT_BLUE, corner_radius=0)
        # show page sections 
        self.title.pack(anchor="w", padx=PAD_X5+PAD_X5, pady=(PAD_Y5+PAD_Y5,0))
        self.tabs.pack(padx=PAD_X4, pady=(PAD_Y5,0))
        self.forms_section.pack(padx=PAD_X4, pady=(PAD_Y4,0))

    def createAddTransactionForm(self, transaction_type):
        # valid categories
        categories_by_type = {
            "expense": ["Bills", "Education", "Entertainment", "Food & Drinks",
                        "Grocery", "Healthcare", "House", "Shopping",
                        "Transportation", "Wellness", "Other"],
            "savings": ["Monthly Allowance", "Change", "Miscellaneous"],
            "investment": ["Stocks", "Crypto", "Bonds", "Real Estate"],
            "income": ["Salary", "Bonus", "Side-hustles", "Tips"]
        }
        # create form
        form = AddTransactionForm(tm=self.tm, user_id=self.user_id, t_type=transaction_type,
                                   categories=categories_by_type[transaction_type],
                                   master=self.forms_section, fg_color=WHITE, corner_radius=RAD)
        return form
