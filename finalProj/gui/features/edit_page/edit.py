# external/built-in modules/libs
import customtkinter as ctk

# our modules/libs
from features.edit_page.tabs import Tabs
from features.edit_page.selections import Selection


class Title(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font = ctk.CTkFont(family="Bodoni MT", size=40, slant="italic", weight="normal")
        self.label = ctk.CTkLabel(self, text="Edit Transaction", font=self.font, text_color="#545454")
        self.label.pack(side="left", padx=(20,0))


class Save(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font = ctk.CTkFont(family="Bodoni MT", size=20, slant="italic", weight="normal")
        self.btn = ctk.CTkButton(self, width=270, height=40, text="Save Changes",
                                 font=self.font, text_color="white",
                                 fg_color="#559eef", hover_color="#427cbd",
                                 corner_radius=10)
        self.btn.pack(pady=(10,10))


class Edit(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(2, weight=1) # whole screen
        # create components
        self.title = Title(self, fg_color="#cef2ff", corner_radius=10)
        self.selection = ctk.CTkFrame(self, fg_color="#cef2ff", corner_radius=10)
        self.save = Save(self, fg_color="#cef2ff", corner_radius=10)
        # create edit sub-pages
        self.expensePage = Selection(self.selection, fg_color="white", corner_radius=10)
        self.savingsPage = Selection(self.selection, fg_color="white", corner_radius=10)
        self.investmentPage = Selection(self.selection, fg_color="white", corner_radius=10)
        self.incomePage = Selection(self.selection, fg_color="white", corner_radius=10)
        self.pages = {
            "expense":self.expensePage, "savings":self.savingsPage,
            "investment":self.investmentPage, "income":self.incomePage
        }
        self.tabs = Tabs(pages=self.pages, master=self, fg_color="#cef2ff", corner_radius=0)
        # show components
        self.title.pack(anchor="w", pady=(40,20))
        self.tabs.pack(pady=(10,10))
        self.selection.pack(pady=(10,10), padx=(20,20))
        self.save.pack(pady=(10,20))