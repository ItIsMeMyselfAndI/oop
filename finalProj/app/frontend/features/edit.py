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
        # create components
        self.title = Title(self, fg_color="#cef2ff", corner_radius=10)
        self.selection = ctk.CTkFrame(self, fg_color="#cef2ff", corner_radius=10)
        # create sub-pages
        self.expensePage = Selection(self.selection, fg_color="white", corner_radius=10)
        self.savingsPage = Selection(self.selection, fg_color="white", corner_radius=10)
        self.investmentPage = Selection(self.selection, fg_color="white", corner_radius=10)
        self.incomePage = Selection(self.selection, fg_color="white", corner_radius=10)
        self.selections = {
            "expense":self.expensePage, "savings":self.savingsPage,
            "investment":self.investmentPage, "income":self.incomePage
        }
        # create sub-pages tabs
        self.tabs = Tabs(selections=self.selections, master=self, fg_color="#cef2ff", corner_radius=0)
        # create save button
        self.save = Save(selections=self.selections, master=self, fg_color="#cef2ff", corner_radius=10)
        # show components
        self.title.pack(anchor="w", pady=(40,20))
        self.tabs.pack(pady=(10,10))
        self.selection.pack(pady=(10,10), padx=(20,20))
        self.save.pack(pady=(10,20))