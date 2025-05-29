# external/built-in modules/libs
import customtkinter as ctk
import os
from PIL import Image
# our modules/libs
from frontend.styles import Styles as s # paddings, dimensions, colors, etc


class Sidebar(ctk.CTkFrame):
    def __init__(self, pages, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pages = pages
        # load icons
        home_icon, profile_icon, add_icon, edit_icon, history_icon = self.loadIcons()
        # create page buttons/tabs
        self.profileBTN = self.createTabBtn(image=profile_icon, command=self.onClickProfilePage)
        self.homeBTN = self.createTabBtn(image=home_icon, command=self.onClickHomePage)
        self.editBTN = self.createTabBtn(image=edit_icon, command=self.onClickEditPage)
        self.historyBTN = self.createTabBtn(image=history_icon, command=self.onClickHistoryPage)
        self.addBTN = self.createTabBtn(image=add_icon, command=self.onClickAddPage)
        self.tabBTNs = {
            "profile":self.profileBTN, "home":self.homeBTN,
            "edit":self.editBTN, "history":self.historyBTN,
            "add":self.addBTN
        }
        # display page buttons/tabs
        self.profileBTN.pack(pady=(s.PAD_1,0), padx=s.PAD_1)
        self.homeBTN.pack(pady=(s.PAD_2,0), padx=s.PAD_1)
        self.editBTN.pack(pady=(s.PAD_2,0), padx=s.PAD_1)
        self.historyBTN.pack(pady=(s.PAD_2,0), padx=s.PAD_1)
        self.addBTN.pack(pady=s.PAD_2, padx=s.PAD_1)
        # open default page
        # self.onClickEditPage()
        self.onClickProfilePage()

    def loadIcons(self):
        # icon path
        ICONS_FOLDER = os.path.abspath("assets/icons")
        # load images
        home_icon = ctk.CTkImage(light_image=Image.open(f"{ICONS_FOLDER}/home.png"), size=(s.SIDEBAR_IMG_W,s.SIDEBAR_IMG_H))
        profile_icon = ctk.CTkImage(light_image=Image.open(f"{ICONS_FOLDER}/profile.png"), size=(s.SIDEBAR_IMG_W,s.SIDEBAR_IMG_H))
        add_icon = ctk.CTkImage(light_image=Image.open(f"{ICONS_FOLDER}/add.png"), size=(s.SIDEBAR_IMG_W,s.SIDEBAR_IMG_H))
        edit_icon = ctk.CTkImage(light_image=Image.open(f"{ICONS_FOLDER}/edit.png"), size=(s.SIDEBAR_IMG_W,s.SIDEBAR_IMG_H))
        history_icon = ctk.CTkImage( light_image=Image.open(f"{ICONS_FOLDER}/history.png"), size=(s.SIDEBAR_IMG_W,s.SIDEBAR_IMG_H))
        return home_icon, profile_icon, add_icon, edit_icon, history_icon

    def createTabBtn(self, image, command):
        btn = ctk.CTkButton(self, text="", corner_radius=s.RAD_1, fg_color=s.WHITE, hover_color=s.LIGHT_GREY,
                            image=image, height=s.SIDEBAR_BTN_H, width=s.SIDEBAR_BTN_W, command=command)
        return btn

    def onClickProfilePage(self): self._switchTabTo("profile")
    def onClickHomePage(self): self._switchTabTo("home")
    def onClickEditPage(self): self._switchTabTo("edit")
    def onClickHistoryPage(self): self._switchTabTo("history")
    def onClickAddPage(self): self._switchTabTo("add")

    def _switchTabTo(self, page_name):
        for name, page in self.pages.items():
            # set all page to not current page
            page.isCurrentPage = False 
            # close all pages
            page.pack_forget()
            # reset all buttons
            self.tabBTNs[name].configure(fg_color=s.WHITE, hover_color=s.LIGHT_GREY)
        # open selected page and change fg, hover & text color
        self.pages[page_name].isCurrentPage = True
        self.pages[page_name].pack(fill="both", expand=True)
        self.tabBTNs[page_name].configure(fg_color=s.BLUE, hover_color=s.DARK_BLUE)