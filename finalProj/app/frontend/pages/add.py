# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from frontend.styles import BaseStyles, AddStyles # paddings, dimensions, colors, etc
from frontend.components.date_picker import DatePicker
from backend.transaction_manager import Transaction


# header section
class AddHeader(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_6, weight="normal", slant="italic" )
        self.label = ctk.CTkLabel(self, text="Add Transaction", font=self.font,
                                  text_color=BaseStyles.DARK_GREY, anchor="w", width=AddStyles.HEADER_LABEL_W)
        self.label.pack(anchor="w")


# same with class selection sa edit
class AddTransactionForm(ctk.CTkFrame):
    def __init__(self, tm, user_id, t_type, categories, master, **kwargs):
        super().__init__(master, **kwargs)
        # initialize transaction options
        self.tm = tm
        self.user_id = user_id
        self.t_type = t_type
        self.categories = categories
        # initialize state
        self.isCurrentEditTransactionForm = False
        # initialize fonts
        self.font3 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_4, weight="normal", slant="italic" )
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_3, weight="normal", slant="italic" )
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_2, weight="normal", slant="italic" )
        # create guide frames
        self.frame1 = ctk.CTkFrame(self, fg_color=BaseStyles.WHITE, corner_radius=0)
        self.frame2 = ctk.CTkFrame(self, fg_color=BaseStyles.WHITE, corner_radius=0)
        self.frame3 = ctk.CTkFrame(self, fg_color=BaseStyles.WHITE, corner_radius=0)
        # create frame 1 components
        self.dateLabel = ctk.CTkLabel(self.frame1, text="Select Date",
                                      font=self.font3, text_color=BaseStyles.DARK_GREY)
        self.dateMenu = DatePicker(picker_height=AddStyles.DATE_MENU_H, spacing=BaseStyles.PAD_1, rad=BaseStyles.RAD_2,
                                   day_width=AddStyles.DAY_MENU_W, month_width=AddStyles.MONTH_MENU_W, year_width=AddStyles.YEAR_MENU_W, 
                                   master=self.frame1, ctk_font=self.font1, dropdown_ctk_font=self.font1,
                                   dropdown_fg_color=BaseStyles.WHITE, dropdown_hover_color=BaseStyles.BLUE, fg_color=BaseStyles.WHITE)
        # create frame 2 components
        self.categoryLabel = ctk.CTkLabel(self.frame2, text="Select Category",
                                          font=self.font3, text_color=BaseStyles.DARK_GREY)
        self.categoryMenu = ctk.CTkOptionMenu(self.frame2, values=self.categories, font=self.font1,
                                              text_color=BaseStyles.DARK_GREY,fg_color=BaseStyles.BLUE, corner_radius=BaseStyles.RAD_2,
                                              dropdown_font=self.font1, dropdown_fg_color=BaseStyles.WHITE,
                                              dropdown_hover_color=BaseStyles.BLUE, dropdown_text_color=BaseStyles.DARK_GREY,
                                              width=AddStyles.CATEGORY_MENU_W, height=AddStyles.CATEGORY_MENU_H)
        self.descriptionLabel = ctk.CTkLabel(self.frame2, text="Enter Description",
                                             font=self.font3, text_color=BaseStyles.DARK_GREY)
        self.descriptionEntry = ctk.CTkEntry(self.frame2, font=self.font1,
                                             text_color=BaseStyles.DARK_GREY, fg_color=BaseStyles.LIGHT_BLUE,
                                             corner_radius=BaseStyles.RAD_2, border_width=0,
                                             placeholder_text="Description", placeholder_text_color=BaseStyles.GREY,
                                             width=AddStyles.DESCRIPTION_ENTRY_W, height=AddStyles.DESCRIPTION_ENTRY_H,)
        # create frame 3 components
        self.amountLabel = ctk.CTkLabel(self.frame3, text="Enter Amount",
                                        font=self.font3, text_color=BaseStyles.DARK_GREY)
        self.amountEntry = ctk.CTkEntry(self.frame3, font=self.font1,
                                        text_color=BaseStyles.DARK_GREY, fg_color=BaseStyles.LIGHT_BLUE,
                                        corner_radius=BaseStyles.RAD_2, border_width=0,
                                        placeholder_text="Philippine Peso", placeholder_text_color=BaseStyles.GREY,
                                        width=AddStyles.AMOUNT_ENTRY_W, height=AddStyles.AMOUNT_ENTRY_H,)
        # display guide frames
        self.frame1.pack(fill="both", pady=(BaseStyles.PAD_4,0))
        self.frame2.pack(fill="both", pady=(BaseStyles.PAD_4,0))
        self.frame3.pack(fill="both", pady=BaseStyles.PAD_4)
        # display frame 1 
        self.dateLabel.grid(row=0, column=0, sticky="w", padx=BaseStyles.PAD_3, pady=(0,BaseStyles.PAD_3))
        self.dateMenu.grid(row=1, column=0, sticky="w", padx=BaseStyles.PAD_3, pady=0)
        # display frame 2 
        self.categoryLabel.grid(row=0, column=0, sticky="w", padx=(BaseStyles.PAD_3,0), pady=(0,BaseStyles.PAD_3))
        self.categoryMenu.grid(row=1, column=0, sticky="w", padx=(BaseStyles.PAD_3,0), pady=0)
        self.descriptionLabel.grid(row=0, column=1, sticky="w", padx=BaseStyles.PAD_3, pady=(0,BaseStyles.PAD_3))
        self.descriptionEntry.grid(row=1, column=1, sticky="w", padx=BaseStyles.PAD_3, pady=0)
        # display frame 3 
        self.amountLabel.pack(anchor="w", padx=BaseStyles.PAD_3, pady=(0,BaseStyles.PAD_3))
        self.amountEntry.pack(anchor="w", padx=BaseStyles.PAD_3, pady=0)
    

class AddPageTabs(ctk.CTkFrame):
    def __init__(self, transactionForms, master, **kwargs):
        super().__init__(master, **kwargs)
        self.transactionForms = transactionForms
        self.font = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_3, weight="normal", slant="italic" )
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
        self.savingsBTN.grid(row=0, column=1, padx=(BaseStyles.PAD_3, 0))
        self.investmentBTN.grid(row=0, column=2, padx=(BaseStyles.PAD_3, 0))
        self.incomeBTN.grid(row=0, column=3, padx=(BaseStyles.PAD_3,0))
        # open default tab (expense)
        self._switchPageTo("expense")

    def createTabButton(self, text, command):
        btn = ctk.CTkButton(self, text=text, text_color=BaseStyles.DARK_GREY, height=AddStyles.TAB_H, width=AddStyles.TAB_W,
                            font=self.font, corner_radius=BaseStyles.RAD_2, fg_color=BaseStyles.WHITE, hover_color=BaseStyles.LIGHT_GREY,
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
            self.tabBTNs[t_type].configure(fg_color=BaseStyles.WHITE, hover_color=BaseStyles.LIGHT_GREY, text_color=BaseStyles.DARK_GREY)
        # open selected and change fg, hover & text color
        self.transactionForms[transaction_type].isCurrentEditTransactionForm = True
        self.transactionForms[transaction_type].grid(row=2, column=0, sticky="nsew")
        self.tabBTNs[transaction_type].configure(fg_color=BaseStyles.BLUE, hover_color=BaseStyles.DARK_BLUE, text_color=BaseStyles.WHITE)


# main add page class
class AddPage(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize state
        self.isCurrentPage = False
        # create page sections 
        self.title = AddHeader(self, fg_color=BaseStyles.SKY_BLUE, corner_radius=0)
        self.forms_section = ctk.CTkFrame(self, fg_color=BaseStyles.SKY_BLUE, corner_radius=BaseStyles.RAD_2)
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
                         fg_color=BaseStyles.SKY_BLUE, corner_radius=0)
        # show page sections 
        self.title.pack(pady=(BaseStyles.PAD_4+BaseStyles.PAD_4,0))
        self.tabs.pack(pady=(BaseStyles.PAD_4,0))
        self.forms_section.pack(pady=(BaseStyles.PAD_3,0))

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
                                   master=self.forms_section, fg_color=BaseStyles.WHITE, corner_radius=BaseStyles.RAD_2)
        return form

    def saveNewTransactionToDatabase(self):
        month_2_numeric = {"January":"01", "February":"02", "March":"03", "April":"04",
                           "May":"05", "June":"06", "July":"07", "August":"08",
                           "September":"09", "October":"10", "November":"11", "December":"12"}
        for transaction_type, form in self.transactionForms.items():
            # retrieve user inputs from the UI
            year = form.dateMenu.year_menu.get()
            month = month_2_numeric[form.dateMenu.month_menu.get()]
            day = form.dateMenu.day_menu.get()
            new_date = f"{year}-{month}-{day}"
            new_category = form.categoryMenu.get()
            new_description = form.descriptionEntry.get()
            new_amount = form.amountEntry.get()
            if form.isCurrentEditTransactionForm == True:
                # create new_transaction obj
                new_transaction = Transaction(t_date=new_date, t_type=transaction_type,
                                              t_category=new_category, t_amount=float(new_amount),
                                              t_description=new_description)
                # update db with new_transaction
                result = self.tm.repo.addTransaction(user_id=self.user_id, new_transaction=new_transaction)
                # display result for debugging
                print("\n", result)
                print()
                print(f"{transaction_type = }")
                print(f"{new_date = }")
                print(f"{new_category = }")
                print(f"{new_description = }")
                print(f"{new_amount = }")
                # reset form
                form.dateMenu.year_menu.set(form.dateMenu.years[0])
                form.dateMenu.month_menu.set(form.dateMenu.months[0])
                form.dateMenu.day_menu.set(form.dateMenu.days[0])
                form.categoryMenu.set(form.categories[0])
                form.descriptionEntry.delete(first_index=0, last_index=ctk.END)
                form.amountEntry.delete(first_index=0, last_index=ctk.END)