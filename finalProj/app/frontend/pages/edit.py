# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from frontend.utilities.date_picker import DatePicker
from backend.transaction_manager import Transaction

# create global screen dimension
temp_root = ctk.CTk()
SCREEN_W = temp_root.winfo_screenwidth()
temp_root.destroy()
SCREEN_H = int(0.5625*SCREEN_W)
print(SCREEN_W, SCREEN_H)

FONT_SIZE_1 = int(0.0231*SCREEN_H) #25
FONT_SIZE_2 = int(0.0278*SCREEN_H) #30
FONT_SIZE_3 = int(0.0370*SCREEN_H) #40
FONT_SIZE_4 = int(0.0463*SCREEN_H) #50
FONT_SIZE_5 = int(0.0556*SCREEN_H) #60

WHITE= "white"

WHITE_RED = "#fdecec"
LIGHT_RED = "#ffc7c7"
RED = "#e14242"

WHITE_GREEN = "#dafbf0"
LIGHT_GREEN = "#b2fee3"
GREEN = "#28ab58"

WHITE_PURPLE = "#f3eefe"
LIGHT_PURPLE =  "#d6c5fb"
PURPLE = "#ceb9fe"

WHITE_BLUE = "#ebf2fe"
SKY_BLUE = "#cef2ff"
LIGHT_BLUE = "#bcd4fe"
BLUE = "#559eef"
DARK_BLUE = "#427cbd"

LIGHT_GREY = "#c4c4c4"
GREY = "grey"
DARK_GREY = "#545454"

ENTRY_W1 = int(1.3241*SCREEN_H)#1430
ENTRY_W2 = int(0.5556*SCREEN_H) #600
ENTRY_H = int(0.0556*SCREEN_H) #60

MENU_W1 = int(0.7407*SCREEN_H) #800
MENU_W2 = int(1.2593*SCREEN_H) #1360 
MENU_H = int(0.0556*SCREEN_H) #60

YEAR_MENU_W = int(0.4167*SCREEN_H) #450
MONTH_MENU_W = int(0.4630*SCREEN_H) #500 
DAY_MENU_W = int(0.4167*SCREEN_H) #450

PAD_X1 = int(0.0093*SCREEN_H) #10
PAD_X2 = int(0.0185*SCREEN_H) #20
PAD_X3 = int(0.0278*SCREEN_H) #30
PAD_X4 = int(0.0370*SCREEN_H) #40
PAD_X5 = int(0.0463*SCREEN_H) #50

PAD_Y1 = int(0.0093*SCREEN_H) #10
PAD_Y2 = int(0.0185*SCREEN_H) #20
PAD_Y3 = int(0.0278*SCREEN_H) #30
PAD_Y4 = int(0.0370*SCREEN_H) #40
PAD_Y5 = int(0.0463*SCREEN_H) #50

BTN_W1 = int(0.0648*SCREEN_H) #70
BTN_W2 = int(0.3241*SCREEN_H) #350

BTN_H1 = int(0.0648*SCREEN_H) #70
BTN_H2 = int(0.0556*SCREEN_H) #60

RAD = int(0.0185*SCREEN_H) #20

# ---- exclusive ----
# overwrite date picker size
YEAR_MENU_W = 0.1667*SCREEN_H #180
MONTH_MENU_W = 0.2037*SCREEN_H #220
DAY_MENU_W = 0.1667*SCREEN_H #180

# header section
class EditHeader(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_5, slant="italic", weight="normal")
        self.label = ctk.CTkLabel(self, text="Edit Transaction", font=self.font, text_color=DARK_GREY)
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
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_2, slant="italic", weight="normal")
        self.font3 = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_1, slant="italic", weight="normal")
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
                                                 dropdown_fg_color=WHITE,
                                                 dropdown_hover_color=BLUE,
                                                 dropdown_text_color=DARK_GREY,
                                                 corner_radius=RAD, width=MENU_W1, height=MENU_H)
        self.dateLabel = ctk.CTkLabel(self.frame1, text="Select New Date",
                                      font=self.font1, text_color=DARK_GREY)
        self.dateMenu = DatePicker(picker_height=MENU_H, spacing=PAD_X1, rad=RAD,
                                   day_width=DAY_MENU_W, month_width=MONTH_MENU_W, year_width=YEAR_MENU_W, 
                                   master=self.frame1, ctk_font=self.font3, dropdown_ctk_font=self.font2,
                                   dropdown_fg_color=WHITE, dropdown_hover_color=BLUE, fg_color=WHITE)
        # create frame 2 components
        self.categoryLabel = ctk.CTkLabel(self.frame2, text="Select New Category",
                                          font=self.font1, text_color=DARK_GREY)
        self.categoryMenu = ctk.CTkOptionMenu(self.frame2, values=categories,
                                                font=self.font3, text_color=DARK_GREY,
                                                width=MENU_W1, fg_color=BLUE,
                                                dropdown_font=self.font2,
                                                dropdown_fg_color=WHITE,
                                                dropdown_hover_color=BLUE,
                                                dropdown_text_color=DARK_GREY,
                                                corner_radius=RAD, height=MENU_H)
        self.descriptionLabel = ctk.CTkLabel(self.frame2, text="Enter New Description",
                                             font=self.font1, text_color=DARK_GREY)
        self.descriptionEntry = ctk.CTkEntry(self.frame2, font=self.font3,
                                             text_color=DARK_GREY, fg_color=LIGHT_BLUE,
                                             corner_radius=RAD, width=ENTRY_W2, height=ENTRY_H,
                                             placeholder_text="Description",
                                             placeholder_text_color=GREY,
                                             border_width=0)
        # create frame 3 components
        self.amountLabel = ctk.CTkLabel(self.frame3, text="Enter New Amount",
                                        font=self.font1, text_color=DARK_GREY)
        self.amountEntry = ctk.CTkEntry(self.frame3, font=self.font3,
                                        text_color=DARK_GREY, fg_color=LIGHT_BLUE,
                                        corner_radius=RAD, width=ENTRY_W1, height=ENTRY_H,
                                        placeholder_text="Philippine Peso",
                                        placeholder_text_color=GREY,
                                        border_width=0)
        # display guide frames
        self.frame1.pack(fill="both", pady=(PAD_Y4,0))
        self.frame2.pack(fill="both", pady=(PAD_Y4,0))
        self.frame3.pack(fill="both", pady=PAD_Y4)
        # display frame 1 components
        self.transactionLabel.grid(row=0, column=0, sticky="w", padx=(PAD_X3,0), pady=(0,PAD_Y3))
        self.transactionMenu.grid(row=1, column=0, sticky="w", padx=(PAD_X3,0), pady=0)
        self.dateLabel.grid(row=0, column=1, sticky="w", padx=PAD_X3, pady=(0,PAD_Y3))
        self.dateMenu.grid(row=1, column=1, sticky="w", padx=PAD_X3, pady=0)
        # display frame 2 components
        self.categoryLabel.grid(row=0, column=0, sticky="w", padx=(PAD_X3,0), pady=(0,PAD_Y3))
        self.categoryMenu.grid(row=1, column=0, sticky="w", padx=(PAD_X3,0), pady=0)
        self.descriptionLabel.grid(row=0, column=1, sticky="w", padx=PAD_X3, pady=(0,PAD_Y3))
        self.descriptionEntry.grid(row=1, column=1, sticky="w", padx=PAD_X3, pady=0)
        # display frame 3 components
        self.amountLabel.pack(anchor="w", padx=PAD_X3, pady=(0,PAD_Y3))
        self.amountEntry.pack(anchor="w", padx=PAD_X3, pady=0)
    
    def updateTransactionMenuOptionsByType(self) -> list[str]:
        transactions = self.tm.repo.getTransactionsByType(self.user_id, self.t_type)
        transaction_options = []
        for t in transactions:
            formatted_t = f" {t.t_id} | {t.t_date} | {t.t_category} | {t.t_amount} | {t.t_description} "
            formatted_t = f"{formatted_t[:60]}..." if len(formatted_t) > 60 else formatted_t
            transaction_options.append(formatted_t)
        self.transaction_options = transaction_options


# tabs section of the page
class EditPageTabs(ctk.CTkFrame):
    def __init__(self, transactionForms, master, **kwargs):
        super().__init__(master, **kwargs)
        self.transactionForms = transactionForms
        # initialize ctk font
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
        self.savingsBTN.grid(row=0, column=1, padx=(PAD_X3, 0))
        self.investmentBTN.grid(row=0, column=2, padx=(PAD_X3, 0))
        self.incomeBTN.grid(row=0, column=3, padx=(PAD_X3,0))
        # open default tab (expense)
        self._switchPageTo("expense")

    def createTabButton(self, text, command):
        btn = ctk.CTkButton(self, text=text, text_color=DARK_GREY, height=BTN_H2, width=BTN_W2,
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
            # reset all buttons
            self.tabBTNs[t_type].configure(fg_color=WHITE, hover_color=LIGHT_GREY, text_color=DARK_GREY)
        # open selected and change fg, hover & text color
        self.transactionForms[transaction_type].isCurrentEditTransactionForm = True
        self.transactionForms[transaction_type].grid(row=2, column=0, sticky="nsew")
        self.tabBTNs[transaction_type].configure(fg_color=BLUE, hover_color=DARK_BLUE, text_color=WHITE)


# main edit page
class Edit(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize state
        self.isCurrentPage = False
        # create page sections 
        self.header_section = EditHeader(self, fg_color=SKY_BLUE, corner_radius=0)
        self.forms_section = ctk.CTkFrame(self, fg_color=SKY_BLUE, corner_radius=RAD)
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
        self.tabs = EditPageTabs(transactionForms=self.transactionForms, master=self,
                         fg_color=SKY_BLUE, corner_radius=0)
        # show page sections 
        self.header_section.pack(anchor="w", padx=PAD_X4+PAD_X4, pady=(PAD_Y4+PAD_Y4,0))
        self.tabs.pack(padx=PAD_X3, pady=(PAD_Y4,0))
        self.forms_section.pack(padx=PAD_X3, pady=(PAD_Y3,0))

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

    def saveEditedTransactionToDatabase(self):
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
                # create updated_transaction obj
                updated_transaction = Transaction(t_date=new_date, t_type=transaction_type,
                                                  t_category=new_category, t_amount=float(new_amount),
                                                  t_description=new_description)
                # update db with updated_transaction
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

    # update edit transaction forms
    def updatePageDisplay(self):
        for form in self.transactionForms.values():
            form.updateTransactionMenuOptionsByType()
            form.transactionMenu.configure(values=form.transaction_options)
            form.transactionMenu.set(form.transaction_options[0])