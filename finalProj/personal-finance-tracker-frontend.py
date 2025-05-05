import customtkinter as ctk


class Home(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add nyo implementation dito


class Profile(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add nyo implementation dito


class Add(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add nyo implementation dito


class Edit(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add nyo implementation dito


class History(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add nyo implementation dito


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Personal Finance Tracker")
        self.geometry("1920x1080")
        
        # create tabview
        # wag muna galawin tong layout and position ng tabs
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(pady=10, padx=10, fill="both", expand=True)
        
        # add page tabs
        self.tabview.add("Home")
        self.tabview.add("Profile")
        self.tabview.add("Add")
        self.tabview.add("Edit")
        self.tabview.add("History")
        
        # create page instances
        self.home = Home(self.tabview.tab("Home"))
        self.profile = Profile(self.tabview.tab("Profile"))
        self.add = Add(self.tabview.tab("Add"))
        self.edit = Edit(self.tabview.tab("Edit"))
        self.history = History(self.tabview.tab("History"))
        
        # add the pages to the screen in order
        self.home.pack(fill="both", expand=True)
        self.profile.pack(fill="both", expand=True)
        self.add.pack(fill="both", expand=True)
        self.edit.pack(fill="both", expand=True)
        self.history.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
