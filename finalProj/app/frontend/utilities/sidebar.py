import customtkinter as ctk
from PIL import Image

ICONS_FOLDER = "./assets/icons"

# create global screen dimension
temp_root = ctk.CTk()
SCREEN_W = temp_root.winfo_screenwidth()
temp_root.destroy()
SCREEN_H = int(0.5625*SCREEN_W)
print(SCREEN_W, SCREEN_H)

FONT_SIZE_1 = int(0.0231*SCREEN_H) #25
FONT_SIZE_2 = int(0.0278*SCREEN_H) #30
FONT_SIZE_3 = int(0.0370*SCREEN_H) #40
FONT_SIZE_4 = int(0.0463*SCREEN_H) #50
FONT_SIZE_5 = int(0.0556*SCREEN_H) #60

WHITE= "white"

WHITE_RED = "#fdecec"
LIGHT_RED = "#ffc7c7"
RED = "#e14242"

WHITE_GREEN = "#dafbf0"
LIGHT_GREEN = "#b2fee3"
GREEN = "#28ab58"

WHITE_PURPLE = "#f3eefe"
LIGHT_PURPLE =  "#d6c5fb"
PURPLE = "#ceb9fe"

WHITE_BLUE = "#ebf2fe"
SKY_BLUE = "#cef2ff"
LIGHT_BLUE = "#bcd4fe"
BLUE = "#559eef"
DARK_BLUE = "#427cbd"

LIGHT_GREY = "#c4c4c4"
GREY = "grey"
DARK_GREY = "#545454"

ENTRY_W1 = int(1.3241*SCREEN_H) #1430
ENTRY_W2 = int(0.5556*SCREEN_H) #600
ENTRY_H = int(0.0556*SCREEN_H) #60

MENU_W1 = int(0.7407*SCREEN_H) #800
MENU_W2 = int(1.2593*SCREEN_H) #1360 
MENU_H = int(0.0556*SCREEN_H) #60

YEAR_MENU_W = int(0.4167*SCREEN_H) #450
MONTH_MENU_W = int(0.4630*SCREEN_H) #500 
DAY_MENU_W = int(0.4167*SCREEN_H) #450

PAD_X1 = int(0.0093*SCREEN_H) #10
PAD_X2 = int(0.0185*SCREEN_H) #20
PAD_X3 = int(0.0278*SCREEN_H) #30
PAD_X4 = int(0.0370*SCREEN_H) #40
PAD_X5 = int(0.0463*SCREEN_H) #50

PAD_Y1 = int(0.0093*SCREEN_H) #10
PAD_Y2 = int(0.0185*SCREEN_H) #20
PAD_Y3 = int(0.0278*SCREEN_H) #30
PAD_Y4 = int(0.0370*SCREEN_H) #40
PAD_Y5 = int(0.0463*SCREEN_H) #50

BTN_W1 = int(0.0648*SCREEN_H) #70
BTN_W2 = int(0.3241*SCREEN_H) #350

BTN_H1 = int(0.0648*SCREEN_H) #70
BTN_H2 = int(0.0556*SCREEN_H) #60

RAD = int(0.0185*SCREEN_H) #20

# ---- exclusive ----
IMG_W = int(0.0370*SCREEN_H) #40
IMG_H = int(0.0370*SCREEN_H) #40


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
        self.profileBTN.pack(pady=(PAD_Y2,0), padx=PAD_X1)
        self.homeBTN.pack(pady=(PAD_Y2,0), padx=PAD_X1)
        self.editBTN.pack(pady=(PAD_Y2,0), padx=PAD_X1)
        self.historyBTN.pack(pady=(PAD_Y2,0), padx=PAD_X1)
        self.addBTN.pack(pady=PAD_Y2, padx=PAD_X1)
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