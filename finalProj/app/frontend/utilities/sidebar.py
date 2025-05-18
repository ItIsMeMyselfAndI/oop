import customtkinter as ctk
from PIL import Image

icons_folder = "./frontend/assets/icons"
PAD_X = 10
PAD_Y = 20
IMG_W = 40
IMG_H = 40
BTN_W = 70
BTN_H = 70

class Sidebar(ctk.CTkFrame):
    def __init__(self, pages, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pages = pages
        # load icons
        self.home_icon = ctk.CTkImage(
            light_image=Image.open(f"{icons_folder}/home.png"), size=(IMG_W,IMG_H))
        self.profile_icon = ctk.CTkImage(
            light_image=Image.open(f"{icons_folder}/profile.png"), size=(IMG_W,IMG_H))
        self.add_icon = ctk.CTkImage(
            light_image=Image.open(f"{icons_folder}/add.png"), size=(IMG_W,IMG_H))
        self.edit_icon = ctk.CTkImage(
            light_image=Image.open(f"{icons_folder}/edit.png"), size=(IMG_W,IMG_H))
        self.history_icon = ctk.CTkImage(
            light_image=Image.open(f"{icons_folder}/history.png"), size=(IMG_W,IMG_H))
        # create page buttons/tabs
        self.profileBtn = self.createTabBtn(image=self.profile_icon, command=self.on_click_profile)
        self.homeBtn = self.createTabBtn(image=self.home_icon, command=self.on_click_home)
        self.editBtn = self.createTabBtn(image=self.edit_icon, command=self.on_click_edit)
        self.historyBtn = self.createTabBtn(image=self.history_icon, command=self.on_click_history)
        self.addBtn = self.createTabBtn(image=self.add_icon, command=self.on_click_add)
        # display page buttons/tabs
        self.profileBtn.pack(pady=(PAD_Y,0), padx=PAD_X)
        self.homeBtn.pack(pady=(PAD_Y,0), padx=PAD_X)
        self.editBtn.pack(pady=(PAD_Y,0), padx=PAD_X)
        self.historyBtn.pack(pady=(PAD_Y,0), padx=PAD_X)
        self.addBtn.pack(pady=PAD_Y, padx=PAD_X)
        # open default page
        self.on_click_edit()

    def createTabBtn(self, image, command):
        btn = ctk.CTkButton(self, text="", corner_radius=10, fg_color="white", hover_color="#c4c4c4",
                            image=image, height=BTN_H, width=BTN_W, command=command)
        return btn


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
        # set other page to not current page
        self.pages["home"].isCurrentPage = False 
        self.pages["edit"].isCurrentPage = False 
        self.pages["history"].isCurrentPage = False 
        self.pages["add"].isCurrentPage = False 
        # open profile and change fg & hover color
        self.pages["profile"].isCurrentPage = True
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
        # set other page to not current page
        self.pages["profile"].isCurrentPage = False 
        self.pages["edit"].isCurrentPage = False 
        self.pages["history"].isCurrentPage = False 
        self.pages["add"].isCurrentPage = False 
        # open home 
        self.pages["home"].isCurrentPage = True
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
        # set other page to not current page
        self.pages["profile"].isCurrentPage = False 
        self.pages["home"].isCurrentPage = False 
        self.pages["history"].isCurrentPage = False 
        self.pages["add"].isCurrentPage = False 
        # open edit 
        self.pages["edit"].isCurrentPage = True
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
        # set other page to not current page
        self.pages["profile"].isCurrentPage = False 
        self.pages["home"].isCurrentPage = False 
        self.pages["edit"].isCurrentPage = False 
        self.pages["add"].isCurrentPage = False 
        # open history 
        self.pages["history"].isCurrentPage = True
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
        # set other page to not current page
        self.pages["profile"].isCurrentPage = False 
        self.pages["home"].isCurrentPage = False 
        self.pages["edit"].isCurrentPage = False 
        self.pages["history"].isCurrentPage = False 
        # open add 
        self.pages["add"].isCurrentPage = True
        self.pages["add"].pack(fill="both", expand=True)
        self.addBtn.configure(fg_color="#559eef", hover_color="#427cbd")