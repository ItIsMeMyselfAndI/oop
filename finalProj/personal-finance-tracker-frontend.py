import customtkinter as ctk
from PIL import Image


class Home(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        label = ctk.CTkLabel(self, text="Home page", font=("Arial", 24))
        label.pack(pady=50)


class Profile(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        label = ctk.CTkLabel(self, text="Profile Page", font=("Arial", 24))
        label.pack(pady=50)


class Add(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        label = ctk.CTkLabel(self, text="Add Page", font=("Arial", 24))
        label.pack(pady=50)


class Edit(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        label = ctk.CTkLabel(self, text="Edit Page", font=("Arial", 24))
        label.pack(pady=50)


class History(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        label = ctk.CTkLabel(self, text="History Page", font=("Arial", 24))
        label.pack(pady=50)


class Sidebar(ctk.CTkFrame):
    def __init__(self, pages, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pages = pages
        # load icons
        self.home_icon = ctk.CTkImage(light_image=Image.open("./icons/home.png"), size=(40,40))
        self.profile_icon = ctk.CTkImage(light_image=Image.open("./icons/profile.png"), size=(40,40))
        self.add_icon = ctk.CTkImage(light_image=Image.open("./icons/add.png"), size=(40,40))
        self.edit_icon = ctk.CTkImage(light_image=Image.open("./icons/edit.png"), size=(40,40))
        self.history_icon = ctk.CTkImage(light_image=Image.open("./icons/history.png"), size=(40,40))

        # create tab page buttons/tabs
        self.profileButton = ctk.CTkButton(
            self, text="", corner_radius=10,
            fg_color="#ffffff", hover_color="#c4c4c4",
            image=self.profile_icon,
            height=70, width=70,
            command=self._on_click_profile
        )
        self.homeButton = ctk.CTkButton(
            self, text="", corner_radius=10,
            fg_color="#ffffff", hover_color="#c4c4c4",
            image=self.home_icon,
            height=70, width=70,
            command=self._on_click_home
        )
        self.editButton = ctk.CTkButton(
            self, text="", corner_radius=10,
            fg_color="#ffffff", hover_color="#c4c4c4",
            image=self.edit_icon,
            height=70, width=70,
            command=self._on_click_edit
        )
        self.historyButton = ctk.CTkButton(
            self, text="", corner_radius=10,
            fg_color="#ffffff", hover_color="#c4c4c4",
            image=self.history_icon,
            height=70, width=70,
            command=self._on_click_history
        )
        self.addButton = ctk.CTkButton(
            self, text="", corner_radius=10,
            fg_color="#ffffff", hover_color="#c4c4c4",
            image=self.add_icon,
            height=70, width=70,
            command=self._on_click_add
        )

        # show tab page buttons/tabs
        self.profileButton.pack(pady=(5,0), padx=5)
        self.homeButton.pack(pady=(5,0), padx=5)
        self.editButton.pack(pady=(5,0), padx=5)
        self.historyButton.pack(pady=(5,0), padx=5)
        self.addButton.pack(pady=(5,0), padx=5)
        # set default page
        self.show("profile")

    def _on_click_profile(self): self.show("profile")
    def _on_click_home(self): self.show("home")
    def _on_click_edit(self): self.show("history")
    def _on_click_history(self): self.show("history")
    def _on_click_add(self): self.show("add")

    def show(self, name:str):
        print(f"You clicked {name.capitalize()}")
        for page in self.pages.values():
            page.grid_forget()
        self.pages[name].grid(row=0, column=1, sticky="nsew")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # initialize dimensions
        self.title("Personal Finance Tracker")
        self.geometry("1920x1080")
        # self.geometry("1080x600")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create app pages
        self.profilePage = Profile(self) 
        self.homePage = Home(self) 
        self.editPage = Edit(self) 
        self.historyPage = History(self) 
        self.addPage = Add(self) 
        self.pages = {
            "profile":self.profilePage, "home":self.homePage,
            "edit":self.editPage, "history":self.historyPage,
            "add":self.addPage
        }
        
        # create sidebar tabs
        self.sidebar = Sidebar(pages=self.pages, master=self,
                               fg_color="#ffffff", corner_radius=0)

        # display sidebar
        self.sidebar.grid(row=0, column=0, sticky="ns")


if __name__ == "__main__":
    app = App()
    app.mainloop()
