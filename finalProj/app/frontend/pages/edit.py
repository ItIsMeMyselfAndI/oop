# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from frontend.styles import BaseStyles, EditStyles # paddings, dimensions, colors, etc
from frontend.components.date_picker import DatePicker
from backend.transaction_manager import Transaction


# header section
class EditHeader(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font6 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_6, weight="normal", slant="italic" )
        self.title_label = ctk.CTkLabel(self, text="Edit Transaction", font=self.font6, text_color=EditStyles.HEADER_TITLE_TEXT_COLOR,
                                  width=EditStyles.HEADER_TITLE_LABEL_W, fg_color=EditStyles.HEADER_TITLE_LABEL_FG_COLOR, anchor="w")
        self.title_label.pack(anchor="w")


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
        self.categories = categories
        # initialize state
        self.isCurrentEditTransactionForm = False
        # initialize fonts
        self.font2 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_2, weight="normal", slant="italic" )
        self.font4 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_4, weight="normal", slant="italic" )
        # create sections
        self.first_section = ctk.CTkFrame(self, fg_color=EditStyles.FORM_FIRST_SECTION_FG_COLOR, corner_radius=0)
        self.second_section = ctk.CTkFrame(self, fg_color=EditStyles.FORM_SECOND_SECTION_FG_COLOR, corner_radius=0)
        self.third_section = ctk.CTkFrame(self, fg_color=EditStyles.FORM_THIRD_SECTION_FG_COLOR, corner_radius=0)
        # create first section components
        self.transactionLabel = ctk.CTkLabel(self.first_section, text="Select Transaction", font=self.font4,
                                             text_color=EditStyles.TRANSACTION_LABEL_TEXT_COLOR, fg_color=EditStyles.TRANSACTION_LABEL_FG_COLOR)
        self.transactionMenu = ctk.CTkOptionMenu(self.first_section, values=self.transaction_options, font=self.font2, corner_radius=BaseStyles.RAD_2,
                                                 text_color=EditStyles.TRANSACTION_MENU_TEXT_COLOR, fg_color=EditStyles.TRANSACTION_MENU_FG_COLOR,
                                                 dropdown_font=self.font2, dropdown_fg_color=EditStyles.TRANSACTION_DROPDOWN_FG_COLOR,
                                                 dropdown_hover_color=EditStyles.TRANSACTION_DROPDOWN_HOVER_COLOR,
                                                 dropdown_text_color=EditStyles.TRANSACTION_DROPDOWN_TEXT_COLOR,
                                                 width=EditStyles.TRANSACTION_MENU_W, height=EditStyles.TRANSACTION_MENU_H)
        self.dateLabel = ctk.CTkLabel(self.first_section, text="Select New Date", font=self.font4,
                                      text_color=EditStyles.DATE_LABEL_TEXT_COLOR, fg_color=EditStyles.DATE_LABEL_FG_COLOR)
        self.dateMenu = DatePicker(picker_height=EditStyles.DATE_MENU_H, spacing=BaseStyles.PAD_1, rad=BaseStyles.RAD_2,
                                   day_width=EditStyles.DAY_MENU_W, month_width=EditStyles.MONTH_MENU_W, year_width=EditStyles.YEAR_MENU_W, 
                                   master=self.first_section, ctk_font=self.font2, fg_color=EditStyles.DATE_MENU_FRAME_FG_COLOR,
                                   menu_fg_color=EditStyles.DATE_MENU_FG_COLOR, menu_text_color=EditStyles.DATE_MENU_TEXT_COLOR,
                                   dropdown_ctk_font=self.font2, dropdown_text_color=EditStyles.DATE_DROPDOWN_TEXT_COLOR,
                                   dropdown_fg_color=EditStyles.DATE_DROPDOWN_FG_COLOR, dropdown_hover_color=EditStyles.DATE_DROPDOWN_HOVER_COLOR)
        # create second section components
        self.categoryLabel = ctk.CTkLabel(self.second_section, text="Select New Category", font=self.font4,
                                          text_color=EditStyles.CATEGORY_LABEL_TEXT_COLOR, fg_color=EditStyles.CATEGORY_LABEL_FG_COLOR)
        self.categoryMenu = ctk.CTkOptionMenu(self.second_section, values=self.categories, font=self.font2, corner_radius=BaseStyles.RAD_2,
                                              text_color=EditStyles.CATEGORY_MENU_TEXT_COLOR, fg_color=EditStyles.CATEGORY_MENU_FG_COLOR,
                                              dropdown_font=self.font2, dropdown_fg_color=EditStyles.CATEGORY_DROPDOWN_FG_COLOR,
                                              dropdown_hover_color=EditStyles.CATEGORY_DROPDOWN_HOVER_COLOR,
                                              dropdown_text_color=EditStyles.CATEGORY_DROPDOWN_TEXT_COLOR,
                                              width=EditStyles.CATEGORY_MENU_W, height=EditStyles.CATEGORY_MENU_H)
        self.descriptionLabel = ctk.CTkLabel(self.second_section, text="Enter New Description", font=self.font4,
                                             text_color=EditStyles.DESCRIPTION_LABEL_TEXT_COLOR, fg_color=EditStyles.DESCRIPTION_LABEL_FG_COLOR)
        self.descriptionEntry = ctk.CTkEntry(self.second_section, font=self.font2, border_width=0, corner_radius=BaseStyles.RAD_2,
                                             text_color=EditStyles.DESCRIPTION_ENTRY_TEXT_COLOR, fg_color=EditStyles.DESCRIPTION_ENTRY_FG_COLOR,
                                             bg_color=EditStyles.DESCRIPTION_ENTRY_BG_COLOR, placeholder_text="Description",
                                             placeholder_text_color=EditStyles.DESCRIPTION_PLACEHOLDER_TEXT_COLOR,
                                             width=EditStyles.DESCRIPTION_ENTRY_W, height=EditStyles.DESCRIPTION_ENTRY_H,)
        # create third section components
        self.amountLabel = ctk.CTkLabel(self.third_section, text="Enter New Amount", font=self.font4,
                                        text_color=EditStyles.AMOUNT_LABEL_TEXT_COLOR, fg_color=EditStyles.AMOUNT_LABEL_FG_COLOR)
        self.amountEntry = ctk.CTkEntry(self.third_section, font=self.font2, border_width=0, corner_radius=BaseStyles.RAD_2,
                                        text_color=EditStyles.AMOUNT_ENTRY_TEXT_COLOR, fg_color=EditStyles.AMOUNT_ENTRY_FG_COLOR,
                                        bg_color=EditStyles.AMOUNT_ENTRY_BG_COLOR, placeholder_text="Philippine Peso",
                                        placeholder_text_color=EditStyles.AMOUNT_PLACEHOLDER_TEXT_COLOR,
                                        width=EditStyles.AMOUNT_ENTRY_W, height=EditStyles.AMOUNT_ENTRY_H,)
        # display sections
        self.first_section.pack(fill="both", pady=(BaseStyles.PAD_4,0))
        self.second_section.pack(fill="both", pady=(BaseStyles.PAD_4,0))
        self.third_section.pack(fill="both", pady=BaseStyles.PAD_4)
        # display first section components
        self.transactionLabel.grid(row=0, column=0, sticky="w", padx=(BaseStyles.PAD_3,0), pady=(0,BaseStyles.PAD_3))
        self.transactionMenu.grid(row=1, column=0, sticky="w", padx=(BaseStyles.PAD_3,0), pady=0)
        self.dateLabel.grid(row=0, column=1, sticky="w", padx=BaseStyles.PAD_3, pady=(0,BaseStyles.PAD_3))
        self.dateMenu.grid(row=1, column=1, sticky="w", padx=BaseStyles.PAD_3, pady=0)
        # display second section components
        self.categoryLabel.grid(row=0, column=0, sticky="w", padx=(BaseStyles.PAD_3,0), pady=(0,BaseStyles.PAD_3))
        self.categoryMenu.grid(row=1, column=0, sticky="w", padx=(BaseStyles.PAD_3,0), pady=0)
        self.descriptionLabel.grid(row=0, column=1, sticky="w", padx=BaseStyles.PAD_3, pady=(0,BaseStyles.PAD_3))
        self.descriptionEntry.grid(row=1, column=1, sticky="w", padx=BaseStyles.PAD_3, pady=0)
        # display third section components
        self.amountLabel.pack(anchor="w", padx=BaseStyles.PAD_3, pady=(0,BaseStyles.PAD_3))
        self.amountEntry.pack(anchor="w", padx=BaseStyles.PAD_3, pady=0)
    
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
        self.font3 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_3, weight="normal", slant="italic" )
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
        btn = ctk.CTkButton(self, text=text, font=self.font3, corner_radius=BaseStyles.RAD_2,
                            text_color=EditStyles.OFF_TAB_TEXT_COLOR, fg_color=EditStyles.OFF_TAB_BUTTON_FG_COLOR,
                            hover_color=EditStyles.OFF_TAB_BUTTON_HOVER_COLOR,
                            height=EditStyles.TAB_H, width=EditStyles.TAB_W, command=command)
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
            self.tabBTNs[t_type].configure(fg_color=EditStyles.OFF_TAB_BUTTON_FG_COLOR, hover_color=EditStyles.OFF_TAB_BUTTON_HOVER_COLOR,
                                           text_color=EditStyles.OFF_TAB_TEXT_COLOR)
        # open selected and change fg, hover & text color
        self.transactionForms[transaction_type].isCurrentEditTransactionForm = True
        self.transactionForms[transaction_type].grid(row=2, column=0, sticky="nsew")
        self.tabBTNs[transaction_type].configure(fg_color=EditStyles.ON_TAB_BUTTON_FG_COLOR, hover_color=EditStyles.ON_TAB_BUTTON_HOVER_COLOR,
                                                 text_color=EditStyles.ON_TAB_TEXT_COLOR)


# main edit page
class EditPage(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize state
        self.is_current_page = False
        # create page sections 
        self.header_section = EditHeader(self, fg_color=EditStyles.HEADER_SECTION_FG_COLOR, corner_radius=0)
        self.forms_section = ctk.CTkFrame(self, fg_color=EditStyles.FORMS_SECTION_FG_COLOR, corner_radius=BaseStyles.RAD_2)
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
                                 fg_color=EditStyles.TABS_FRAME_FG_COLOR, corner_radius=0)
        # show page sections 
        self.header_section.pack(pady=(BaseStyles.PAD_4+BaseStyles.PAD_4,0))
        self.tabs.pack(padx=BaseStyles.PAD_3, pady=(BaseStyles.PAD_4,0))
        self.forms_section.pack(pady=(BaseStyles.PAD_3,0))

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
                                   categories=categories_by_type[transaction_type], master=self.forms_section,
                                   fg_color=EditStyles.FORM_FRAME_FG_COLOR, corner_radius=BaseStyles.RAD_2)
        return form

    def saveEditedTransactionToDatabase(self):
        month_2_numeric = {"January":"01", "February":"02", "March":"03", "April":"04",
                           "May":"05", "June":"06", "July":"07", "August":"08",
                           "September":"09", "October":"10", "November":"11", "December":"12"}
        for transaction_type, form in self.transactionForms.items():
            # retrieve user inputs from the UI
            original_transaction = form.transactionMenu.get().strip()
            transaction_id = int(original_transaction.split()[0])
            year = form.dateMenu.year_menu.get()
            month = month_2_numeric[form.dateMenu.month_menu.get()]
            day = form.dateMenu.day_menu.get()
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
                # reset form
                form.transactionMenu.set(form.transaction_options[0])
                form.dateMenu.year_menu.set(form.dateMenu.years[0])
                form.dateMenu.month_menu.set(form.dateMenu.months[0])
                form.dateMenu.day_menu.set(form.dateMenu.days[0])
                form.categoryMenu.set(form.categories[0])
                form.descriptionEntry.delete(first_index=0, last_index=ctk.END)
                form.amountEntry.delete(first_index=0, last_index=ctk.END)

    # update edit transaction forms
    def updatePageDisplay(self):
        for form in self.transactionForms.values():
            form.updateTransactionMenuOptionsByType()
            form.transactionMenu.configure(values=form.transaction_options)
            if form.transaction_options:
                form.transactionMenu.set(form.transaction_options[0])
            else:
                form.transactionMenu.set("No Available Transaction")