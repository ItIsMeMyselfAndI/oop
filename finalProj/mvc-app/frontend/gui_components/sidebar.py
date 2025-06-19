# external/built-in modules/libs
import customtkinter as ctk
import os
import sys
from PIL import Image
# our modules/libs
from frontend.styles import BaseStyles, SidebarStyles # paddings, dimensions, colors, etc


#--------------------------------------------------------------------------------------------------------


class SidebarTabs(ctk.CTkFrame):
    def __init__(self, controller_per_page, master, **kwargs):
        super().__init__(master, **kwargs)
        self.controller_per_page = controller_per_page

        # sidebar icons
        self.load_icons()
        self.create_tab_per_page()
        

    def load_icons(self):
        # icon path
        if hasattr(sys, "_MEIPASS"): # # for .exe: memory resources path
            _MEIPASS: str = getattr(sys, "_MEIPASS")
            ICONS_FOLDER = os.path.join(_MEIPASS, "assets/icons")
        else: # for .py: storage resources path
            ICONS_FOLDER = "assets/icons"
        print(ICONS_FOLDER)
        
        # load images
        self.home_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "home.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "home.png")),
            size=(SidebarStyles.IMG_W,SidebarStyles.IMG_H)
        )
        self.profile_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "profile.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "profile.png")),
            size=(SidebarStyles.IMG_W,SidebarStyles.IMG_H)
        )
        self.edit_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "edit.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "edit.png")),
            size=(SidebarStyles.IMG_W,SidebarStyles.IMG_H)
        )
        self.history_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "history.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "history.png")),
            size=(SidebarStyles.IMG_W,SidebarStyles.IMG_H)
        )
        self.add_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(ICONS_FOLDER, "add.png")),
            dark_image=Image.open(os.path.join(ICONS_FOLDER, "add.png")),
            size=(SidebarStyles.IMG_W,SidebarStyles.IMG_H)
        )


    def create_tab_per_page(self):
        self.profile_btn = self._create_tab(
            image=self.profile_icon,
            command=self.on_click_profile_page
        )
        self.profile_btn.pack(pady=(BaseStyles.PAD_1,0), padx=BaseStyles.PAD_1)
        
        self.home_btn = self._create_tab(
            image=self.home_icon,
            command=self.on_click_home_page
        )
        self.home_btn.pack(pady=(BaseStyles.PAD_2,0), padx=BaseStyles.PAD_1)
        
        self.edit_btn = self._create_tab(
            image=self.edit_icon,
            command=self.on_click_edit_page
        )
        self.edit_btn.pack(pady=(BaseStyles.PAD_2,0), padx=BaseStyles.PAD_1)
        
        self.history_btn = self._create_tab(
            image=self.history_icon,
            command=self.on_click_history_page
        )
        self.history_btn.pack(pady=(BaseStyles.PAD_2,0), padx=BaseStyles.PAD_1)
        
        self.add_btn = self._create_tab(
            image=self.add_icon,
            command=self.on_click_add_page
        )
        self.add_btn.pack(pady=(BaseStyles.PAD_2, 0), padx=BaseStyles.PAD_1)
        
        self.tab_per_page = {
            "profile":self.profile_btn, "home":self.home_btn,
            "edit":self.edit_btn, "history":self.history_btn,
            "add":self.add_btn
        }
        self.update_idletasks()


    def _create_tab(self, image, command):
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


    def on_click_profile_page(self):
        self.after(100, lambda: self._hide_other_pages("profile"))
        self.after(300, lambda: self._show_page("profile"))


    def on_click_home_page(self):
        self.after(100, lambda: self._hide_other_pages("home"))
        self.after(300, lambda: self._show_page("home"))


    def on_click_edit_page(self):
        self.after(100, lambda: self._hide_other_pages("edit"))
        self.after(300, lambda: self._show_page("edit"))


    def on_click_history_page(self):
        self.after(100, lambda: self._hide_other_pages("history"))
        self.after(300, lambda: self._show_page("history"))


    def on_click_add_page(self):
        self.after(100, lambda: self._hide_other_pages("add"))
        self.after(300, lambda: self._show_page("add"))


    def _hide_other_pages(self, page_name):
        # hide other pages
        for name, controller in self.controller_per_page.items():
            if not page_name == name:
                controller.model.is_current_page = False # set page to not current page
                controller.view.pack_forget() # close page
                self.tab_per_page[name].configure( # reset tab config
                    fg_color=SidebarStyles.OFF_BTN_FG_COLOR,
                    hover_color=SidebarStyles.OFF_BTN_HOVER_COLOR
                )
                self.update_idletasks()


    def _show_page(self, page_name):
        # open selected page and change fg, hover & text color
        if not self.controller_per_page[page_name].model.is_current_page:
            self.controller_per_page[page_name].model.is_current_page = True
            self.tab_per_page[page_name].configure(
                fg_color=SidebarStyles.ON_BTN_FG_COLOR,
                hover_color=SidebarStyles.ON_BTN_HOVER_COLOR
            )
            self.controller_per_page[page_name].view.pack()
            self.update_idletasks()