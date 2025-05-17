# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from frontend.utilities.date_picker import DatePicker
from backend.transaction_manager import Transaction


FONT_SIZE_1 = 60
FONT_SIZE_2 = 50
FONT_SIZE_3 = 40
FONT_SIZE_4 = 30
FONT_SIZE_5 = 25

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


# header section
class Header(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_1, slant="italic", weight="normal")
        self.label = ctk.CTkLabel(self, text="Edit Transaction",
                                  font=self.font, text_color=DARK_GREY)
        self.label.pack(anchor="w")


# transaction form section
class EditTransactionForm(ctk.CTkFrame):
    def __init__(self, tm, user_id, t_type, categories, master, **kwargs):
        super().__init__(master, **kwargs)
        # initialize transaction options
        self.tm = tm
        self.user_id = user_id
        self.t_type = t_type
        self.transaction_options = []
        self.updateTransactionMenuOptionsByType()
        # initialize state
        self.isCurrentEditTransactionForm = False
        # initialize fonts
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_3, slant="italic", weight="normal")
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_4, slant="italic", weight="normal")
        self.font3 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_5, slant="italic", weight="normal")
        # create guide frames
        self.frame1 = ctk.CTkFrame(self, fg_color=WHITE, corner_radius=0)
        self.frame2 = ctk.CTkFrame(self, fg_color=WHITE, corner_radius=0)
        self.frame3 = ctk.CTkFrame(self, fg_color=WHITE, corner_radius=0)
        # create frame 1 components
        self.transactionLabel = ctk.CTkLabel(self.frame1, text="Select Transaction",
                                             font=self.font1, text_color=DARK_GREY)
        self.transactionMenu = ctk.CTkOptionMenu(self.frame1, values=self.transaction_options,
                                                 font=self.font3, text_color=DARK_GREY,
                                                 fg_color=BLUE, dropdown_font=self.font2,
                                                 dropdown_fg_color=BLUE,
                                                 dropdown_hover_color=DARK_BLUE,
                                                 dropdown_text_color=DARK_GREY,
                                                 corner_radius=RAD, width=MENU_W, height=MENU_H)
        self.dateLabel = ctk.CTkLabel(self.frame1, text="Select New Date",
                                      font=self.font1, text_color=DARK_GREY)
        self.dateMenu = DatePicker(picker_height=MENU_H, spacing=PAD_X5, rad=RAD,
                                   day_width=DAY_MENU_W, month_width=MONTH_MENU_W, year_width=YEAR_MENU_W, 
                                   master=self.frame1, ctk_font=self.font3, dropdown_ctk_font=self.font2,
                                   fg_color=WHITE)
        # create frame 2 components
        self.categoryLabel = ctk.CTkLabel(self.frame2, text="Select New Category",
                                          font=self.font1, text_color=DARK_GREY)
        self.categoryMenu = ctk.CTkOptionMenu(self.frame2, values=categories,
                                                font=self.font3, text_color=DARK_GREY,
                                                width=MENU_W, fg_color=BLUE,
                                                dropdown_font=self.font2,
                                                dropdown_fg_color=BLUE,
                                                dropdown_hover_color=DARK_BLUE,
                                                dropdown_text_color=DARK_GREY,
                                                corner_radius=RAD, height=MENU_H)
        self.descriptionLabel = ctk.CTkLabel(self.frame2, text="Enter New Description",
                                             font=self.font1, text_color=DARK_GREY)
        self.descriptionEntry = ctk.CTkEntry(self.frame2, font=self.font3,
                                             text_color=DARK_GREY, fg_color=BLUE,
                                             corner_radius=RAD, width=ENTRY_W2, height=ENTRY_H,
                                             placeholder_text="Description",
                                             placeholder_text_color=GREY,
                                             border_width=0)
        # create frame 3 components
        self.amountLabel = ctk.CTkLabel(self.frame3, text="Enter New Amount",
                                        font=self.font1, text_color=DARK_GREY)
        self.amountEntry = ctk.CTkEntry(self.frame3, font=self.font3,
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
    
    def updateTransactionMenuOptionsByType(self) -> list[str]:
        transactions = self.tm.repo.getTransactionsByType(self.user_id, self.t_type)
        transaction_options = []
        for t in transactions:
            formatted_t = f" {t.t_id} | {t.t_date} | {t.t_category} | {t.t_amount} | {t.t_description} "
            formatted_t = f"{formatted_t[:60]}..." if len(formatted_t) > 60 else formatted_t
            transaction_options.append(formatted_t)
        self.transaction_options = transaction_options


# tabs section of the page
class Tabs(ctk.CTkFrame):
    def __init__(self, transactionForms, master, **kwargs):
        super().__init__(master, **kwargs)
        self.transactionForms = transactionForms
        self.font = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_4, slant="italic", weight="normal")
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
        self.savingsBTN.grid(row=0, column=1, padx=(PAD_X2, 0))
        self.investmentBTN.grid(row=0, column=2, padx=(PAD_X2, 0))
        self.incomeBTN.grid(row=0, column=3, padx=(PAD_X2,0))
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
    
    def _switchPageTo(self, transaction_type):
        for t_type, form in self.transactionForms.items():
            # set all transaction forms's isCurrentEditTransactionForm attr to false
            form.isCurrentEditTransactionForm = False
            # close all transaction forms
            form.grid_forget()
            # reset fg, hover & text color of all buttons
            self.tabBTNs[t_type].configure(fg_color=WHITE, hover_color=LIGHT_GREY, text_color=DARK_GREY)
        # open expense form and change fg, hover & text color
        self.transactionForms[transaction_type].isCurrentEditTransactionForm = True
        self.transactionForms[transaction_type].grid(row=2, column=0, sticky="nsew")
        self.tabBTNs[transaction_type].configure(fg_color=BLUE, hover_color=DARK_BLUE, text_color=WHITE)


# save section of the page
class Save(ctk.CTkFrame):
    def __init__(self, tm, user_id, transactionForms, master, **kwargs):
        super().__init__(master, **kwargs)
        self.tm = tm
        self.user_id = user_id
        self.transactionForms = transactionForms 
        self.font = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_4, slant="italic", weight="normal")
        self.btn = ctk.CTkButton(self, width=BTN_W, height=BTN_H, text="Save Changes",
                                 font=self.font, text_color=WHITE,
                                 fg_color=BLUE, hover_color=DARK_BLUE,
                                 corner_radius=RAD, command=self.saveTransactionChanges)
        self.btn.pack()

    def saveTransactionChanges(self):
        month_2_numeric = {"January":"01", "February":"02", "March":"03", "April":"04",
                           "May":"05", "June":"06", "July":"07", "August":"08",
                           "September":"09", "October":"10", "November":"11", "December":"12"}
        for transaction_type, form in self.transactionForms.items():
            # retrieve user inputs from the UI
            original_transaction = form.transactionMenu.get().strip()
            transaction_id = int(original_transaction.split()[0])
            year = form.dateMenu.year.get()
            month = month_2_numeric[form.dateMenu.month.get()]
            day = form.dateMenu.day.get()
            new_date = f"{year}-{month}-{day}"
            new_category = form.categoryMenu.get()
            new_description = form.descriptionEntry.get()
            new_amount = form.amountEntry.get()
            if form.isCurrentEditTransactionForm == True:
                # create updated transaction obj
                updated_transaction = Transaction(t_date=new_date, t_type=transaction_type, t_category=new_category,
                                                t_amount=float(new_amount), t_description=new_description)
                # update db with updated transaction
                result = self.tm.repo.modifyTransaction(user_id=self.user_id, t_id=transaction_id,
                                                        updated_transaction=updated_transaction)
                # display result for debugging
                print("\n", result)
                print()
                print(len(original_transaction)+3)
                print(f"{original_transaction = }")
                print(f"{transaction_type = }")
                print(f"{transaction_id = }")
                print(f"{new_date = }")
                print(f"{new_category = }")
                print(f"{new_description = }")
                print(f"{new_amount = }")
            # update all transaction forms
            form.updateTransactionMenuOptionsByType()
            form.transactionMenu.configure(values=form.transaction_options)
            form.transactionMenu.set(form.transaction_options[0])


# main edit page
class Edit(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # create page sections 
        self.header_section = Header(self, fg_color=LIGHT_BLUE, corner_radius=0)
        self.forms_section = ctk.CTkFrame(self, fg_color=LIGHT_BLUE, corner_radius=RAD)
        # create transaction forms
        self.expenseForm = self.createEditTransactionForm("expense")
        self.savingsForm = self.createEditTransactionForm("savings")
        self.investmentForm = self.createEditTransactionForm("investment")
        self.incomeForm = self.createEditTransactionForm("income")
        self.transactionForms = {
            "expense":self.expenseForm, "savings":self.savingsForm,
            "investment":self.investmentForm, "income":self.incomeForm
        }
        # create sub-pages tabs
        self.tabs = Tabs(transactionForms=self.transactionForms, master=self,
                         fg_color=LIGHT_BLUE, corner_radius=0)
        # create save button
        self.save = Save(tm=self.tm, user_id=self.user_id, transactionForms=self.transactionForms, master=self,
                         fg_color=LIGHT_BLUE, corner_radius=0)
        # show page sections 
        self.header_section.pack(anchor="w", padx=PAD_X1+PAD_X1, pady=(PAD_Y1+PAD_Y1,0))
        self.tabs.pack(padx=PAD_X2, pady=(PAD_Y1,0))
        self.forms_section.pack(padx=PAD_X2, pady=(PAD_Y2,0))
        self.save.pack(pady=PAD_Y1)

    def createEditTransactionForm(self, transaction_type):
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
        form = EditTransactionForm(tm=self.tm, user_id=self.user_id, t_type=transaction_type,
                                   categories=categories_by_type[transaction_type],
                                   master=self.forms_section, fg_color=WHITE, corner_radius=RAD)
        return form

