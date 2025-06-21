# external/built-in modules/libs
import customtkinter as ctk
from customtkinter import StringVar, IntVar
# our modules/libs
from backend import Transaction, TransactionManager

from models import Model


#--------------------------------------------------------------------------------------------------------


class EditPageModel(Model):
    def __init__(self, transaction_manager: TransactionManager, user_id_var: IntVar):
        self.initialize_managers(transaction_manager)
        self.initialize_vars(user_id_var)
        self.initialize_categories_by_type()

        self.is_current_page = False


    def initialize_managers(self, transaction_manager: TransactionManager):
        self.t_man = transaction_manager
    

    def initialize_vars(self, user_id_var: IntVar):
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


    def save_user_inputs_to_database(self, form_per_transaction_type):
        month_2_numeric = {
            "January":"01", "February":"02", "March":"03", "April":"04",
            "May":"05", "June":"06", "July":"07", "August":"08",
            "September":"09", "October":"10", "November":"11", "December":"12"
        }
        for transaction_type, form in form_per_transaction_type.items():
            if form.is_current_form == True:
                # retrieve user inputs from the UI
                original_transaction = form.transactionMenu.get().strip()
                if original_transaction == "No Available Transaction":
                    return
                year = form.dateMenu.year_menu.get()
                month = month_2_numeric[form.dateMenu.month_menu.get()]
                day = form.dateMenu.day_menu.get()
                
                transaction_id = int(original_transaction.split()[0])
                new_date = f"{year}-{month}-{day}"
                new_category = form.categoryMenu.get()
                new_description = form.descriptionEntry.get()
                new_amount = form.amountEntry.get()
                
                if "-" in new_amount:
                    raise ValueError

                new_amount = float(new_amount)
                # create updated_transaction obj
                updated_transaction = Transaction(
                    t_date=new_date,
                    t_type=transaction_type,
                    t_category=new_category,
                    t_amount=new_amount,
                    t_description=new_description
                )

                # update db with updated_transaction
                result = self.t_man.repo.modifyTransaction(
                    user_id=int(self.user_id_var.get()),
                    t_id=transaction_id,
                    updated_transaction=updated_transaction
                )

                # display result for debugging
                print("\n[DEBUG] update transaction, details:")
                print(f"\t{result = }")
                print(f"\t{original_transaction = }")
                print(f"\t{transaction_type = }")
                print(f"\t{transaction_id = }")
                print(f"\t{new_date = }")
                print(f"\t{new_category = }")
                print(f"\t{new_description = }")
                print(f"\t{new_amount = }")

                # reset form
                form.transactionMenu.set(form.transaction_options[0])
                form.dateMenu.year_menu.set(form.dateMenu.years[0])
                form.dateMenu.month_menu.set(form.dateMenu.months[0])
                form.dateMenu.day_menu.set(form.dateMenu.days[0])
                form.categoryMenu.set(form.categories[0])
                form.descriptionEntry.delete(first_index=0, last_index=ctk.END)
                form.amountEntry.delete(first_index=0, last_index=ctk.END)


    def load_transactions_per_filter(self):
        pass


    def load_amounts(self):
        pass