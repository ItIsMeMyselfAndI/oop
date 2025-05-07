import customtkinter as ctk

from features.edit_page.edit import Edit
from features.sidebar import Sidebar


class Home(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        label = ctk.CTkLabel(self, text="Home page", text_color="#545454", font=("Arial", 24))
        label.pack(pady=50)


class Profile(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        label = ctk.CTkLabel(self, text="Profile Page", text_color="#545454", font=("Arial", 24))
        label.pack(pady=50)


class Add(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        label = ctk.CTkLabel(self, text="Add Page", text_color="#545454", font=("Arial", 24))
        label.pack(pady=50)


class History(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        label = ctk.CTkLabel(self, text="History Page", text_color="#545454", font=("Arial", 24))
        label.pack(pady=50)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # initialize dimensions
        self.title("Personal Finance Tracker")
        self.geometry("1920x1080")
        # self.geometry("1080x600")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1) 
        # create scrollable screen
        self.yScroll = ctk.CTkScrollableFrame(self, orientation="vertical",
                                              corner_radius=0,fg_color="#cef2ff")
        self.yScroll.grid(row=0, column=1, sticky="nsew")
        # self.xyScroll = ctk.CTkScrollableFrame(self.yScroll, orientation="horizontal")
        # self.xyScroll.pack(fill="x", expand=True)
        # create app pages
        self.profilePage = Profile(self.yScroll, fg_color="#cef2ff", corner_radius=0) 
        self.homePage = Home(self.yScroll, fg_color="#cef2ff", corner_radius=0) 
        self.editPage = Edit(self.yScroll, fg_color="#cef2ff", corner_radius=0) 
        self.historyPage = History(self.yScroll, fg_color="#cef2ff", corner_radius=0) 
        self.addPage = Add(self.yScroll, fg_color="#cef2ff", corner_radius=0) 
        self.pages = {
            "profile":self.profilePage, "home":self.homePage,
            "edit":self.editPage, "history":self.historyPage,
            "add":self.addPage
        }
        # create sidebar tabs
        self.sidebar = Sidebar(pages=self.pages, master=self, fg_color="#ffffff", corner_radius=0)
        # display sidebar
        self.sidebar.grid(row=0, column=0, sticky="ns")


if __name__ == "__main__":
    app = App()
    app.mainloop()
