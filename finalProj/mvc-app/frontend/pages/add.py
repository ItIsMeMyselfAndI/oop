# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from frontend.styles import BaseStyles, AddStyles # paddings, dimensions, colors, etc
from frontend.components import DatePicker
from backend import Transaction, TransactionManager

from models.base_model import Model
from controllers.base_controller import Controller


#--------------------------------------------------------------------------------------------------------


class AddPageModel:
    def __init__(self, transaction_manager: TransactionManager, user_id_var: ctk.IntVar):
        self.initialize_managers(transaction_manager)
        self.initialize_vars(user_id_var)
        self.initialize_categories_by_type()

        self.is_current_page = False


    def initialize_managers(self, transaction_manager: TransactionManager):
        self.t_man = transaction_manager
    

    def initialize_vars(self, user_id_var: ctk.IntVar):
        self.user_id_var = user_id_var


    def initialize_categories_by_type(self):
        self.categories_per_type = {
            "expense": ["Bills", "Education", "Entertainment", "Food & Drinks",
                        "Grocery", "Healthcare", "House", "Shopping",
                        "Transportation", "Wellness", "Other"],
            "savings": ["Monthly Allowance", "Change", "Miscellaneous"],
            "investment": ["Stocks", "Crypto", "Bonds", "Real Estate"],
            "income": ["Salary", "Bonus", "Side-hustles", "Tips"]
        }


    def save_new_transaction_to_database(self, form_per_transaction_type):
        month_2_numeric = {
            "January":"01", "February":"02", "March":"03", "April":"04",
            "May":"05", "June":"06", "July":"07", "August":"08",
            "September":"09", "October":"10", "November":"11", "December":"12"
        }
        for transaction_type, form in form_per_transaction_type.items():
            if form.is_current_form == True:
                # retrieve user inputs from the UI
                year = form.dateMenu.year_menu.get()
                month = month_2_numeric[form.dateMenu.month_menu.get()]
                day = form.dateMenu.day_menu.get()
                
                new_date = f"{year}-{month}-{day}"
                new_category = form.categoryMenu.get()
                new_description = form.descriptionEntry.get()
                new_amount = form.amountEntry.get()
                
                if "-" in new_amount:
                    raise ValueError

                new_amount = float(new_amount)
                # create new_transaction obj
                new_transaction = Transaction(
                    t_date=new_date,
                    t_type=transaction_type,
                    t_category=new_category,
                    t_amount=new_amount,
                    t_description=new_description
                )

                # update db with new_transaction
                result = self.t_man.repo.addTransaction(
                    user_id=int(self.user_id_var.get()),
                    new_transaction=new_transaction
                )

                # display result for debugging
                print("\n[DEBUG] update transaction, details:")
                print(f"\t{result = }")
                print(f"\t{transaction_type = }")
                print(f"\t{new_date = }")
                print(f"\t{new_category = }")
                print(f"\t{new_description = }")
                print(f"\t{new_amount = }")

                # reset form
                form.dateMenu.year_menu.set(form.dateMenu.years[0])
                form.dateMenu.month_menu.set(form.dateMenu.months[0])
                form.dateMenu.day_menu.set(form.dateMenu.days[0])
                form.categoryMenu.set(form.categories[0])
                form.descriptionEntry.delete(first_index=0, last_index=ctk.END)
                form.amountEntry.delete(first_index=0, last_index=ctk.END)


#--------------------------------------------------------------------------------------------------------


class AddPageView(ctk.CTkFrame):
    def __init__(self, model: AddPageModel, master, **kwargs):
        super().__init__(master, **kwargs)
        self.model = model
        self.is_current_page = False


    def create(self):
        self._create_header()
        self._create_form_per_transaction_type()
        self._create_tabs()

    
    def _create_header(self):
        self.header = Header(
            master=self,
            fg_color=AddStyles.HEADER_SECTION_FG_COLOR,
            corner_radius=0
        )
        self.header.grid(row=0, column=0, pady=(BaseStyles.PAD_4+BaseStyles.PAD_4,0))


    def _create_form_per_transaction_type(self):
        self.forms_section = ctk.CTkFrame(
            master=self,
            fg_color=AddStyles.FORMS_SECTION_FG_COLOR,
            corner_radius=BaseStyles.RAD_2
        )
        self.forms_section.grid(row=2, column=0, pady=(BaseStyles.PAD_3,0))

        self.form_per_transaction_type = dict()
        for t_type in self.model.categories_per_type.keys():
            form = TransactionForm(
                model=self.model,
                t_type=t_type,
                categories=self.model.categories_per_type[t_type],
                master=self.forms_section,
                fg_color=AddStyles.FORM_FRAME_FG_COLOR,
                corner_radius=BaseStyles.RAD_2
            )
            self.form_per_transaction_type.update({t_type: form})


    def _create_tabs(self):
        self.tabs = Tabs(
            form_per_transaction_type=self.form_per_transaction_type,
            master=self,
            fg_color=AddStyles.TABS_FRAME_FG_COLOR, 
            corner_radius=0
        )
        self.tabs.grid(row=1, column=0, padx=BaseStyles.PAD_3, pady=(BaseStyles.PAD_4,0))


#--------------------------------------------------------------------------------------------------------


class AddPageController(Controller):
    def __init__(self, transaction_manager: TransactionManager, user_id_var: ctk.IntVar, master):
        self.model = AddPageModel(transaction_manager=transaction_manager, user_id_var=user_id_var)
        self.view = AddPageView(model=self.model, master=master, fg_color=AddStyles.MAIN_FRAME_FG_COLOR)


    def run(self):
        pass


    def update_display(self):
        # print("[DEBUG] updating edit page display...")
        # print("[DEBUG] edit page display updated successfully")
        pass


#--------------------------------------------------------------------------------------------------------


# header section
class Header(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font6 = ("Arial", BaseStyles.FONT_SIZE_6, "normal")
        self.title_label = ctk.CTkLabel(self, text="Add Transaction", font=self.font6, text_color=AddStyles.HEADER_TITLE_TEXT_COLOR,
                                  width=AddStyles.HEADER_TITLE_LABEL_W, fg_color=AddStyles.HEADER_TITLE_LABEL_FG_COLOR, anchor="w")
        self.title_label.pack(anchor="w")


#--------------------------------------------------------------------------------------------------------


# same with class selection sa edit
class TransactionForm(ctk.CTkFrame):
    def __init__(self, model, t_type, categories, master, **kwargs):
        super().__init__(master, **kwargs)
        self.model = model
        self.t_type = t_type
        self.categories = categories
        
        # initialize state
        self.is_current_form = False
        
        # initialize fonts
        self.font2 = ("Arial", BaseStyles.FONT_SIZE_2, "normal")
        self.font4 = ("Arial", BaseStyles.FONT_SIZE_4, "normal")

        self.create()


    def create(self):
        self._create_sections()
        self._create_top_section_content()
        self._create_mid_section_content()
        self._create_bot_section_content()


    def _create_sections(self):
        self.top_section = ctk.CTkFrame(
            master=self,
            fg_color=AddStyles.FORM_TOP_SECTION_FG_COLOR,
            corner_radius=0
        )
        self.top_section.pack(fill="both", pady=(BaseStyles.PAD_4,0))
        
        self.mid_section = ctk.CTkFrame(
            master=self,
            fg_color=AddStyles.FORM_MID_SECTION_FG_COLOR,
            corner_radius=0
        )
        self.mid_section.pack(fill="both", pady=(BaseStyles.PAD_4,0))
        
        self.bot_section = ctk.CTkFrame(
            master=self,
            fg_color=AddStyles.FORM_BOT_SECTION_FG_COLOR,
            corner_radius=0
        )
        self.bot_section.pack(fill="both", pady=BaseStyles.PAD_4)


    def _create_top_section_content(self): 
        # date
        self.dateLabel = ctk.CTkLabel(
            master=self.top_section,
            text="Select New Date",
            font=self.font4,
            text_color=AddStyles.DATE_LABEL_TEXT_COLOR,
            fg_color=AddStyles.DATE_LABEL_FG_COLOR
        )
        self.dateMenu = DatePicker(
            picker_height=AddStyles.DATE_MENU_H,
            spacing=BaseStyles.PAD_1,
            rad=BaseStyles.RAD_2,
            day_width=AddStyles.DAY_MENU_W,
            month_width=AddStyles.MONTH_MENU_W,
            year_width=AddStyles.YEAR_MENU_W, 
            master=self.top_section,
            ctk_font=self.font2,
            fg_color=AddStyles.DATE_MENU_FRAME_FG_COLOR,
            menu_fg_color=AddStyles.DATE_MENU_FG_COLOR,
            menu_text_color=AddStyles.DATE_MENU_TEXT_COLOR,
            dropdown_ctk_font=self.font2,
            dropdown_text_color=AddStyles.DATE_DROPDOWN_TEXT_COLOR,
            dropdown_fg_color=AddStyles.DATE_DROPDOWN_FG_COLOR,
            dropdown_hover_color=AddStyles.DATE_DROPDOWN_HOVER_COLOR
        )
        self.dateLabel.grid(row=0, column=1, sticky="w", padx=BaseStyles.PAD_3, pady=(0,BaseStyles.PAD_3))
        self.dateMenu.grid(row=1, column=1, sticky="w", padx=BaseStyles.PAD_3, pady=0)
        
    
    def _create_mid_section_content(self):
        # category
        self.categoryLabel = ctk.CTkLabel(
            master=self.mid_section,
            text="Select New Category",
            font=self.font4,
            text_color=AddStyles.CATEGORY_LABEL_TEXT_COLOR,
            fg_color=AddStyles.CATEGORY_LABEL_FG_COLOR
        )
        self.categoryMenu = ctk.CTkOptionMenu(
            master=self.mid_section,
            values=self.categories,
            font=self.font2,
            corner_radius=BaseStyles.RAD_2,
            text_color=AddStyles.CATEGORY_MENU_TEXT_COLOR,
            fg_color=AddStyles.CATEGORY_MENU_FG_COLOR,
            dropdown_font=self.font2,
            dropdown_fg_color=AddStyles.CATEGORY_DROPDOWN_FG_COLOR,
            dropdown_hover_color=AddStyles.CATEGORY_DROPDOWN_HOVER_COLOR,
            dropdown_text_color=AddStyles.CATEGORY_DROPDOWN_TEXT_COLOR,
            width=AddStyles.CATEGORY_MENU_W,
            height=AddStyles.CATEGORY_MENU_H
        )
        self.categoryLabel.grid(row=0, column=0, sticky="w", padx=(BaseStyles.PAD_3,0), pady=(0,BaseStyles.PAD_3))
        self.categoryMenu.grid(row=1, column=0, sticky="w", padx=(BaseStyles.PAD_3,0), pady=0)
        
        # description
        self.descriptionLabel = ctk.CTkLabel(
            master=self.mid_section,
            text="Enter New Description",
            font=self.font4,
            text_color=AddStyles.DESCRIPTION_LABEL_TEXT_COLOR,
            fg_color=AddStyles.DESCRIPTION_LABEL_FG_COLOR
        )
        self.descriptionEntry = ctk.CTkEntry(
            master=self.mid_section,
            font=self.font2,
            border_width=0,
            corner_radius=BaseStyles.RAD_2,
            text_color=AddStyles.DESCRIPTION_ENTRY_TEXT_COLOR,
            fg_color=AddStyles.DESCRIPTION_ENTRY_FG_COLOR,
            bg_color=AddStyles.DESCRIPTION_ENTRY_BG_COLOR,
            placeholder_text="Description",
            placeholder_text_color=AddStyles.DESCRIPTION_PLACEHOLDER_TEXT_COLOR,
            width=AddStyles.DESCRIPTION_ENTRY_W,
            height=AddStyles.DESCRIPTION_ENTRY_H
        )
        self.descriptionLabel.grid(row=0, column=1, sticky="w", padx=BaseStyles.PAD_3, pady=(0,BaseStyles.PAD_3))
        self.descriptionEntry.grid(row=1, column=1, sticky="w", padx=BaseStyles.PAD_3, pady=0)
        

    def _create_bot_section_content(self):
        self.amountLabel = ctk.CTkLabel(
            master=self.bot_section,
            text="Enter New Amount",
            font=self.font4,
            text_color=AddStyles.AMOUNT_LABEL_TEXT_COLOR,
            fg_color=AddStyles.AMOUNT_LABEL_FG_COLOR
        )
        self.amountEntry = ctk.CTkEntry(
            master=self.bot_section,
            font=self.font2,
            border_width=0,
            corner_radius=BaseStyles.RAD_2,
            text_color=AddStyles.AMOUNT_ENTRY_TEXT_COLOR,
            fg_color=AddStyles.AMOUNT_ENTRY_FG_COLOR,
            bg_color=AddStyles.AMOUNT_ENTRY_BG_COLOR,
            placeholder_text="Philippine Peso",
            placeholder_text_color=AddStyles.AMOUNT_PLACEHOLDER_TEXT_COLOR,
            width=AddStyles.AMOUNT_ENTRY_W,
            height=AddStyles.AMOUNT_ENTRY_H
        )
        self.amountLabel.pack(anchor="w", padx=BaseStyles.PAD_3, pady=(0,BaseStyles.PAD_3))
        self.amountEntry.pack(anchor="w", padx=BaseStyles.PAD_3, pady=0)
    

#--------------------------------------------------------------------------------------------------------


class Tabs(ctk.CTkFrame):
    def __init__(self, form_per_transaction_type, master, **kwargs):
        super().__init__(master, **kwargs)
        self.form_per_transaction_type = form_per_transaction_type
        
        # initialize ctk font
        self.font3 = ("Arial", BaseStyles.FONT_SIZE_3, "normal")
        
        # expense tabs
        self.expenseBTN = self.createTabButton(text="Expense", command=self.onClickExpenseTab)
        self.expenseBTN.grid(row=0, column=0, padx=(0, 0))
        
        # savings tabs
        self.savingsBTN = self.createTabButton(text="Savings", command=self.onClickSavingsTab)
        self.savingsBTN.grid(row=0, column=1, padx=(BaseStyles.PAD_3, 0))
        
        # investment tabs
        self.investmentBTN = self.createTabButton(text="Investment", command=self.onClickInvestmentTab)
        self.investmentBTN.grid(row=0, column=2, padx=(BaseStyles.PAD_3, 0))
        
        # income tabs
        self.incomeBTN = self.createTabButton(text="Income", command=self.onClickIncomeTab)
        self.incomeBTN.grid(row=0, column=3, padx=(BaseStyles.PAD_3,0))
        
        # all tabs
        self.tab_btns = {
            "expense":self.expenseBTN, "savings":self.savingsBTN,
            "investment":self.investmentBTN, "income":self.incomeBTN
        }
        
        # open default tab (expense)
        self.onClickExpenseTab()


    def createTabButton(self, text, command):
        btn = ctk.CTkButton(
            master=self,
            text=text,
            font=self.font3,
            corner_radius=BaseStyles.RAD_2,
            text_color=AddStyles.OFF_TAB_TEXT_COLOR,
            fg_color=AddStyles.OFF_TAB_BTN_FG_COLOR,
            hover_color=AddStyles.OFF_TAB_BTN_HOVER_COLOR,
            height=AddStyles.TAB_H,
            width=AddStyles.TAB_W,
            command=command
        )
        return btn
    

    def _hideOtherPages(self, transaction_type):
        # hide other pages
        for t_type, form in self.form_per_transaction_type.items():
            if not t_type == transaction_type:

                try:
                    form.is_current_form = False # set page to not current page
                    form.pack_forget() # close page
                    self.tab_btns[t_type].configure( # reset tab config
                        fg_color=AddStyles.OFF_TAB_BTN_FG_COLOR, 
                        hover_color=AddStyles.OFF_TAB_BTN_HOVER_COLOR,
                        text_color=AddStyles.OFF_TAB_TEXT_COLOR
                    )

                except Exception as e:
                    print(f"[Silent Error] Failed to hide: edit-{t_type} form")
                    print(f"\t{e}")

        self.update_idletasks()


    def _showPage(self, transaction_type):
        # open selected page and change fg, hover & text color
        if not self.form_per_transaction_type[transaction_type].is_current_form:

            try:
                self.form_per_transaction_type[transaction_type].is_current_form = True
                self.tab_btns[transaction_type].configure(
                    fg_color=AddStyles.ON_TAB_BTN_FG_COLOR,
                    hover_color=AddStyles.ON_TAB_BTN_HOVER_COLOR,
                    text_color=AddStyles.ON_TAB_TEXT_COLOR
                )
                self.form_per_transaction_type[transaction_type].pack()

            except Exception as e:
                print(f"[Silent Error] Failed to show: edit-{transaction_type} form")
                print(f"\t{e}")

        self.update_idletasks()


    def onClickExpenseTab(self):
        self.after(100, lambda: self._hideOtherPages("expense"))
        self.after(300, lambda: self._showPage("expense"))


    def onClickSavingsTab(self):
        self.after(100, lambda: self._hideOtherPages("savings"))
        self.after(300, lambda: self._showPage("savings"))


    def onClickInvestmentTab(self):
        self.after(100, lambda: self._hideOtherPages("investment"))
        self.after(300, lambda: self._showPage("investment"))


    def onClickIncomeTab(self):
        self.after(100, lambda: self._hideOtherPages("income"))
        self.after(300, lambda: self._showPage("income"))