# external/built-in modules/libs
import customtkinter as ctk
import os
import sys
from PIL import Image
# our modules/libs
from frontend.styles import BaseStyles, SidebarStyles # paddings, dimensions, colors, etc


#--------------------------------------------------------------------------------------------------------


class SidebarTabs(ctk.CTkFrame):
    def __init__(self, pages, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pages = pages

        # sidebar icons
        home_icon, profile_icon, add_icon, edit_icon, history_icon = self.loadIcons()
        
        # profile buttons/tabs
        self.profile_btn = self.createTabBtn(
            image=profile_icon,
            command=self.onClickProfilePage
        )
        self.profile_btn.pack(pady=(BaseStyles.PAD_1,0), padx=BaseStyles.PAD_1)
        
        # home buttons/tabs
        self.home_btn = self.createTabBtn(
            image=home_icon,
            command=self.onClickHomePage
        )
        self.home_btn.pack(pady=(BaseStyles.PAD_2,0), padx=BaseStyles.PAD_1)
        
        # edit buttons/tabs
        self.edit_btn = self.createTabBtn(
            image=edit_icon,
            command=self.onClickEditPage
        )
        self.edit_btn.pack(pady=(BaseStyles.PAD_2,0), padx=BaseStyles.PAD_1)
        
        # history buttons/tabs
        self.history_btn = self.createTabBtn(
            image=history_icon,
            command=self.onClickHistoryPage
        )
        self.history_btn.pack(pady=(BaseStyles.PAD_2,0), padx=BaseStyles.PAD_1)
        
        # add buttons/tabs
        self.add_btn = self.createTabBtn(
            image=add_icon,
            command=self.onClickAddPage
        )
        self.add_btn.pack(pady=(BaseStyles.PAD_2, 0), padx=BaseStyles.PAD_1)
        
        # page buttons/tabs
        self.tabBTNs = {
            "profile":self.profile_btn, "home":self.home_btn,
            "edit":self.edit_btn, "history":self.history_btn,
            "add":self.add_btn
        }


    def loadIcons(self):
        # icon path
        if hasattr(sys, "_MEIPASS"): # # for .exe: memory resources path
            ICONS_FOLDER = os.path.join(sys._MEIPASS, "assets/icons")
        else: # for .py: storage resources path
            ICONS_FOLDER = "assets/icons"
        print(ICONS_FOLDER)
        
        # load images
        home_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "home.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "home.png")),
            size=(SidebarStyles.IMG_W,SidebarStyles.IMG_H)
        )
        profile_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "profile.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "profile.png")),
            size=(SidebarStyles.IMG_W,SidebarStyles.IMG_H)
        )
        add_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "add.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "add.png")),
            size=(SidebarStyles.IMG_W,SidebarStyles.IMG_H)
        )
        edit_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "edit.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "edit.png")),
            size=(SidebarStyles.IMG_W,SidebarStyles.IMG_H)
        )
        history_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "history.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "history.png")),
            size=(SidebarStyles.IMG_W,SidebarStyles.IMG_H)
        )
        return home_icon, profile_icon, add_icon, edit_icon, history_icon


    def createTabBtn(self, image, command):
        btn = ctk.CTkButton(
            master=self,
            text="",
            corner_radius=BaseStyles.RAD_1,
            image=image, 
            fg_color=SidebarStyles.OFF_BTN_FG_COLOR,
            hover_color=SidebarStyles.OFF_BTN_HOVER_COLOR,
            height=SidebarStyles.BTN_H,
            width=SidebarStyles.BTN_W,
            command=command
        )
        return btn


    def _hideAllPages(self):
        for name, page in self.pages.items():
            # set all page to not current page
            page.is_current_page = False 
            # close all pages
            page.pack_forget()
            # reset all buttons
            self.tabBTNs[name].configure(fg_color=SidebarStyles.OFF_BTN_FG_COLOR, hover_color=SidebarStyles.OFF_BTN_HOVER_COLOR)


    def _switchTabTo(self, page_name):
        # open selected page and change fg, hover & text color
        self.pages[page_name].is_current_page = True
        self.tabBTNs[page_name].configure(
            fg_color=SidebarStyles.ON_BTN_FG_COLOR,
            hover_color=SidebarStyles.ON_BTN_HOVER_COLOR
        )
        self.pages[page_name].pack()


    def onClickProfilePage(self):
        self.after_idle(self._hideAllPages)
        self.after_idle(self._switchTabTo, "profile")


    def onClickHomePage(self):
        self.after_idle(self._hideAllPages)
        self.after_idle(self._switchTabTo, "home")


    def onClickEditPage(self):
        self.after_idle(self._hideAllPages)
        self.after_idle(self._switchTabTo, "edit")


    def onClickHistoryPage(self):
        self.after_idle(self._hideAllPages)
        self.after_idle(self._switchTabTo, "history")


    def onClickAddPage(self):
        self.after_idle(self._hideAllPages)
        self.after_idle(self._switchTabTo, "add")