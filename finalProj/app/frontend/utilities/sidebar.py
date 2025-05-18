import customtkinter as ctk
from PIL import Image

ICONS_FOLDER = "./frontend/assets/icons"

FONT_SIZE_1 = 25
FONT_SIZE_2 = 30
FONT_SIZE_3 = 40
FONT_SIZE_4 = 50
FONT_SIZE_5 = 60

SKY_BLUE = "#cef2ff"
BLUE = "#559eef"
DARK_BLUE = "#427cbd"
LIGHT_GREY = "#c4c4c4"
GREY = "grey"
DARK_GREY = "#545454"
WHITE= "white"

ENTRY_W1 = 1430
ENTRY_W2 = 600
ENTRY_H = 60

MENU_W1 = 800
MENU_W2 = 1360 
MENU_H = 60

YEAR_MENU_W = 450
MONTH_MENU_W = 500 
DAY_MENU_W = 450

PAD_X1 = 10
PAD_X2 = 20
PAD_X3 = 30
PAD_X4 = 40
PAD_X5 = 50

PAD_Y1 = 10
PAD_Y2 = 20
PAD_Y3 = 30
PAD_Y4 = 40
PAD_Y5 = 50

BTN_W1 = 70
BTN_W2 = 350

BTN_H1 = 70
BTN_H2 = 60

RAD = 20
#--------
PAD_X = 10
PAD_Y = 20

IMG_W = 40
IMG_H = 40


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
        self.profileBTN.pack(pady=(PAD_Y,0), padx=PAD_X)
        self.homeBTN.pack(pady=(PAD_Y,0), padx=PAD_X)
        self.editBTN.pack(pady=(PAD_Y,0), padx=PAD_X)
        self.historyBTN.pack(pady=(PAD_Y,0), padx=PAD_X)
        self.addBTN.pack(pady=PAD_Y, padx=PAD_X)
        # open default page
        # self.onClickEditPage()
        self.onClickProfilePage()

    def loadIcons(self):
        home_icon = ctk.CTkImage(light_image=Image.open(f"{ICONS_FOLDER}/home.png"), size=(IMG_W,IMG_H))
        profile_icon = ctk.CTkImage(light_image=Image.open(f"{ICONS_FOLDER}/profile.png"), size=(IMG_W,IMG_H))
        add_icon = ctk.CTkImage(light_image=Image.open(f"{ICONS_FOLDER}/add.png"), size=(IMG_W,IMG_H))
        edit_icon = ctk.CTkImage(light_image=Image.open(f"{ICONS_FOLDER}/edit.png"), size=(IMG_W,IMG_H))
        history_icon = ctk.CTkImage( light_image=Image.open(f"{ICONS_FOLDER}/history.png"), size=(IMG_W,IMG_H))
        return home_icon, profile_icon, add_icon, edit_icon, history_icon

    def createTabBtn(self, image, command):
        btn = ctk.CTkButton(self, text="", corner_radius=10, fg_color=WHITE, hover_color=LIGHT_GREY,
                            image=image, height=BTN_H1, width=BTN_W1, command=command)
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
            self.tabBTNs[name].configure(fg_color=WHITE, hover_color=LIGHT_GREY)
        # open selected page and change fg, hover & text color
        self.pages[page_name].isCurrentPage = True
        self.pages[page_name].pack(fill="both", expand=True)
        self.tabBTNs[page_name].configure(fg_color=BLUE, hover_color=DARK_BLUE)