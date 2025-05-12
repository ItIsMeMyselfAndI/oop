# external/built-in modules/libs
import customtkinter as ctk

# our modules/libs
from frontend.features.edit_components.title import Title
from frontend.features.edit_components.tabs import Tabs
from frontend.features.edit_components.selections import Selection
from frontend.features.edit_components.save import Save

class Edit(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(2, weight=1) # whole screen
        # valid categories
        expense_categories = ["Bills", "Education", "Entertainment", "Food & Drinks",
                              "Grocery", "Healthcare", "House", "Shopping",
                              "Transportation", "Wellness", "Other"]
        other_categories = ["Savings (unchangeable)",
                            "Investment (unchangeable)",
                            "Income (unchangeable)"]
        # sample expense transactions 
        expense_transactions = ["01 January 2023  |  Food  |  P100",
                                "02 February 2024  |  Bills  |  P100",
                                "03 March 2024  |  Education  |  P100"]
        # sample savings/investment/income expense transactions 
        other_transactions = ["01 January 2023  |  P100  |  Description 1",
                              "02 February 2024  |  P100  |  Description 2",
                              "03 March 2024  |  P100  |  Description 3"]
        # create page components
        self.title = Title(self, fg_color="#cef2ff", corner_radius=10)
        self.selection = ctk.CTkFrame(self, fg_color="#cef2ff", corner_radius=10)
        # create sub-pages
        self.expensePage = Selection(categories=expense_categories, transactions=expense_transactions,
                                     master=self.selection, fg_color="white", corner_radius=10)
        self.savingsPage = Selection(categories=other_categories[0:1], transactions=other_transactions,
                                     master=self.selection, fg_color="white", corner_radius=10)
        self.investmentPage = Selection(categories=other_categories[1:2], transactions=other_transactions,
                                        master=self.selection, fg_color="white", corner_radius=10)
        self.incomePage = Selection(categories=other_categories[2:3], transactions=other_transactions,
                                    master=self.selection, fg_color="white", corner_radius=10)
        self.selections = {
            "expense":self.expensePage, "savings":self.savingsPage,
            "investment":self.investmentPage, "income":self.incomePage
        }
        # create sub-pages tabs
        self.tabs = Tabs(selections=self.selections, master=self, fg_color="#cef2ff", corner_radius=0)
        # create save button
        self.save = Save(selections=self.selections, master=self, fg_color="#cef2ff", corner_radius=10)
        # show page components
        self.title.pack(anchor="w", pady=(40,20))
        self.tabs.pack(pady=(10,10))
        self.selection.pack(pady=(10,10), padx=(20,20))
        self.save.pack(pady=(10,20))