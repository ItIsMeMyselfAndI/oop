import customtkinter as ctk
from PIL import Image

icons_folder = "./assets/icons"

class Sidebar(ctk.CTkFrame):
    def __init__(self, pages, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pages = pages
        # load icons
        self.home_icon = ctk.CTkImage(
            light_image=Image.open(f"{icons_folder}/home.png"), size=(30,30))
        self.profile_icon = ctk.CTkImage(
            light_image=Image.open(f"{icons_folder}/profile.png"), size=(30,30))
        self.add_icon = ctk.CTkImage(
            light_image=Image.open(f"{icons_folder}/add.png"), size=(30,30))
        self.edit_icon = ctk.CTkImage(
            light_image=Image.open(f"{icons_folder}/edit.png"), size=(30,30))
        self.history_icon = ctk.CTkImage(
            light_image=Image.open(f"{icons_folder}/history.png"), size=(30,30))
        # create page buttons/tabs
        self.profileBtn = ctk.CTkButton(self, text="", corner_radius=10,
                                           fg_color="white", hover_color="#c4c4c4",
                                           image=self.profile_icon,
                                           height=50, width=50,
                                           command=self.on_click_profile)
        self.homeBtn = ctk.CTkButton(self, text="", corner_radius=10,
                                        fg_color="white", hover_color="#c4c4c4",
                                        image=self.home_icon,
                                        height=50, width=50,
                                        command=self.on_click_home)
        self.editBtn = ctk.CTkButton(self, text="", corner_radius=10,
                                        fg_color="white", hover_color="#c4c4c4",
                                        image=self.edit_icon,
                                        height=50, width=50,
                                        command=self.on_click_edit)
        self.historyBtn = ctk.CTkButton(self, text="", corner_radius=10,
                                           fg_color="white", hover_color="#c4c4c4",
                                           image=self.history_icon,
                                           height=50, width=50,
                                           command=self.on_click_history)
        self.addBtn = ctk.CTkButton(self, text="", corner_radius=10,
                                       fg_color="white", hover_color="#c4c4c4",
                                       image=self.add_icon,
                                       height=50, width=50,
                                       command=self.on_click_add)
        # display page buttons/tabs
        self.profileBtn.pack(pady=(10,10), padx=(10,10))
        self.homeBtn.pack(pady=(10,10), padx=(10,10))
        self.editBtn.pack(pady=(10,10), padx=(10,10))
        self.historyBtn.pack(pady=(10,10), padx=(10,10))
        self.addBtn.pack(pady=(10,10), padx=(10,10))
        # open default page
        # self.pages["profile"].pack(fill="both", expand=True)
        self.pages["edit"].pack(fill="both", expand=True)
        self.editBtn.configure(fg_color="#559eef", hover_color="#427cbd")

    def on_click_profile(self):
        # close other pages
        self.pages["home"].pack_forget()
        self.pages["edit"].pack_forget()
        self.pages["history"].pack_forget()
        self.pages["add"].pack_forget()
        # reset fg & hover color of other buttons
        self.homeBtn.configure(fg_color="white", hover_color="#c4c4c4")
        self.editBtn.configure(fg_color="white", hover_color="#c4c4c4")
        self.historyBtn.configure(fg_color="white", hover_color="#c4c4c4")
        self.addBtn.configure(fg_color="white", hover_color="#c4c4c4")
        # open profile and change fg & hover color
        self.pages["profile"].pack(fill="both", expand=True)
        self.profileBtn.configure(fg_color="#559eef", hover_color="#427cbd")

    def on_click_home(self):
        # close other pages
        self.pages["profile"].pack_forget()
        self.pages["edit"].pack_forget()
        self.pages["history"].pack_forget()
        self.pages["add"].pack_forget()
        # reset fg & text color of other buttons
        self.profileBtn.configure(fg_color="white", hover_color="#c4c4c4")
        self.editBtn.configure(fg_color="white", hover_color="#c4c4c4")
        self.historyBtn.configure(fg_color="white", hover_color="#c4c4c4")
        self.addBtn.configure(fg_color="white", hover_color="#c4c4c4")
        # open home 
        self.pages["home"].pack(fill="both", expand=True)
        self.homeBtn.configure(fg_color="#559eef", hover_color="#427cbd")

    def on_click_edit(self):
        # close other pages
        self.pages["profile"].pack_forget()
        self.pages["home"].pack_forget()
        self.pages["history"].pack_forget()
        self.pages["add"].pack_forget()
        # reset fg & text color of other buttons
        self.profileBtn.configure(fg_color="white", hover_color="#c4c4c4")
        self.homeBtn.configure(fg_color="white", hover_color="#c4c4c4")
        self.historyBtn.configure(fg_color="white", hover_color="#c4c4c4")
        self.addBtn.configure(fg_color="white", hover_color="#c4c4c4")
        # open edit 
        self.pages["edit"].pack(fill="both", expand=True)
        self.editBtn.configure(fg_color="#559eef", hover_color="#427cbd")

    def on_click_history(self):
        # close other pages
        self.pages["profile"].pack_forget()
        self.pages["home"].pack_forget()
        self.pages["edit"].pack_forget()
        self.pages["add"].pack_forget()
        # reset fg & text color of other buttons
        self.profileBtn.configure(fg_color="white", hover_color="#c4c4c4")
        self.homeBtn.configure(fg_color="white", hover_color="#c4c4c4")
        self.editBtn.configure(fg_color="white", hover_color="#c4c4c4")
        self.addBtn.configure(fg_color="white", hover_color="#c4c4c4")
        # open history 
        self.pages["history"].pack(fill="both", expand=True)
        self.historyBtn.configure(fg_color="#559eef", hover_color="#427cbd")

    def on_click_add(self):
        # close other pages
        self.pages["profile"].pack_forget()
        self.pages["home"].pack_forget()
        self.pages["edit"].pack_forget()
        self.pages["history"].pack_forget()
        # reset fg & text color of other buttons
        self.profileBtn.configure(fg_color="white", hover_color="#c4c4c4")
        self.homeBtn.configure(fg_color="white", hover_color="#c4c4c4")
        self.editBtn.configure(fg_color="white", hover_color="#c4c4c4")
        self.historyBtn.configure(fg_color="white", hover_color="#c4c4c4")
        # open add 
        self.pages["add"].pack(fill="both", expand=True)
        self.addBtn.configure(fg_color="#559eef", hover_color="#427cbd")