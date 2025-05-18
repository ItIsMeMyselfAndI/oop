import customtkinter as ctk
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
YEAR_MENU_W = 180
MONTH_MENU_W = 220
DAY_MENU_W = 180

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


# save section
class Save(ctk.CTkFrame):
    def __init__(self, tm, user_id, pages, master, **kwargs):
        super().__init__(master, **kwargs)
        self.tm = tm
        self.user_id = user_id
        self.pages = pages
        self.font = ctk.CTkFont(family="Bodoni MT", size=FONT_SIZE_2, slant="italic", weight="normal")
        self.btn = ctk.CTkButton(self, width=BTN_W, height=BTN_H, text="Save Changes",
                                 font=self.font, text_color=WHITE,
                                 fg_color=BLUE, hover_color=DARK_BLUE,
                                 corner_radius=RAD, command=self.onClickSave)
        self.btn.pack()

    def onClickSave(self):
        for page_name, page in self.pages.items():
            if page.isCurrentPage == True and page_name == "edit":
                self.saveEditedTransactionToDatabase()
            elif page.isCurrentPage == True and page_name == "add":
                self.saveNewTransactionToDatabase()
        self.updateAppMemory()

    def saveEditedTransactionToDatabase(self):
        month_2_numeric = {"January":"01", "February":"02", "March":"03", "April":"04",
                           "May":"05", "June":"06", "July":"07", "August":"08",
                           "September":"09", "October":"10", "November":"11", "December":"12"}
        for transaction_type, form in self.pages["edit"].transactionForms.items():
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
                updated_transaction = Transaction(t_date=new_date, t_type=transaction_type, t_category=new_category,
                                                  t_amount=float(new_amount), t_description=new_description)
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

    def saveNewTransactionToDatabase(self):
        month_2_numeric = {"January":"01", "February":"02", "March":"03", "April":"04",
                           "May":"05", "June":"06", "July":"07", "August":"08",
                           "September":"09", "October":"10", "November":"11", "December":"12"}
        for transaction_type, form in self.pages["add"].transactionForms.items():
            # retrieve user inputs from the UI
            year = form.dateMenu.year.get()
            month = month_2_numeric[form.dateMenu.month.get()]
            day = form.dateMenu.day.get()
            new_date = f"{year}-{month}-{day}"
            new_category = form.categoryMenu.get()
            new_description = form.descriptionEntry.get()
            new_amount = form.amountEntry.get()
            if form.isCurrentEditTransactionForm == True:
                # create new_transaction obj
                new_transaction = Transaction(t_date=new_date, t_type=transaction_type, t_category=new_category,
                                                  t_amount=float(new_amount), t_description=new_description)
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

    def updateAppMemory(self):
        # update edit transaction forms
        for form in self.pages["edit"].transactionForms.values():
            form.updateTransactionMenuOptionsByType()
            form.transactionMenu.configure(values=form.transaction_options)
            form.transactionMenu.set(form.transaction_options[0])