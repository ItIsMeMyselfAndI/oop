# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from backend.transaction_manager import Transaction
from frontend.styles import Styles as s # contains paddings, dimensions, colors, etc


# updatePopUp pop up
class PopUpWin(ctk.CTkToplevel):
    def __init__(self, title, msg, enable_close, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=s.FONT_SIZE_2, slant="italic", weight="normal")
        # initialize win dimensions
        self.WIN_W, self.WIN_H = 400, 200
        self.x_pos = int((s.SCREEN_W / 2) - (self.WIN_W / 2))
        self.y_pos = int((s.SCREEN_H / 2) - (self.WIN_H / 2))
        # create win
        self.title(title)
        self.geometry(f"{self.WIN_W}x{self.WIN_H}+{self.x_pos}+{self.y_pos}")
        self.resizable(width=False, height=False)
        # create content
        self.label = ctk.CTkLabel(self, font=self.font1, width=400, height=200, text=msg, text_color=s.DARK_GREY, wraplength=400)
        self.label.pack(anchor="center")
        # hide win
        self.withdraw()
        # disable manual close -> closes automatically
        if not enable_close:
            self.protocol("WM_DELETE_WINDOW", self.disabledCloseWin)

    def disabledCloseWin(self):
        pass

    def showWin(self):
        self.deiconify() # show win

    def hideWin(self):
        self.withdraw() # hide win


# save section
class Save(ctk.CTkFrame):
    def __init__(self, user_id, tm, pages, app, master, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app
        self.user_id = user_id
        self.tm = tm
        self.pages = pages
        self.font = ctk.CTkFont(family="Bodoni MT", size=s.FONT_SIZE_3, slant="italic", weight="normal")
        # create button
        self.btn = ctk.CTkButton(self, width=s.SAVE_BTN_W, height=s.SAVE_BTN_H, text="Save Changes", font=self.font, text_color=s.WHITE,
                                 fg_color=s.BLUE, hover_color=s.DARK_BLUE, corner_radius=s.RAD_2, command=self.onClickSave)
        # create popups
        self.updatePopUp = PopUpWin(title="[Update] Database", msg="Updating transactions...", enable_close=False,
                                    master=self.app, fg_color=s.WHITE)
        self.emptyDescriptionPopUp = PopUpWin(title="[Err] Invalid Input", msg="Only submit non-empty description.\nTry again.", enable_close=True,
                                              master=self.app, fg_color=s.WHITE)
        self.invalidAmountPopUp = PopUpWin(title="[Err] Invalid Input", msg="Only submit decimal number for amount.\nTry again.", enable_close=True,
                                           master=self.app, fg_color=s.WHITE)
        self.emptyAmountPopUp = PopUpWin(title="[Err] Invalid Input", msg="Only submit non-empty amount.\nTry again.", enable_close=True,
                                         master=self.app, fg_color=s.WHITE)
        # display button
        self.btn.pack()
    
    def _updateBackendAndFrontend(self):
        # save to database
        for page_name, page in self.pages.items():
            if page_name == "edit" and page.isCurrentPage == True:
                self.pages["edit"].saveEditedTransactionToDatabase()
            elif page_name == "add" and page.isCurrentPage == True:
                self.pages["add"].saveNewTransactionToDatabase()
        # update pages
        self.pages["edit"].updatePageDisplay()
        self.pages["profile"].updatePageDisplay()
        self.pages["history"].updatePageDisplay()
        # end updatePopUp
        self.updatePopUp.hideWin()
        print("\nend update")

    def onClickSave(self):
        # start updatePopUp
        print("\nstart update")
        self.updatePopUp.showWin()
        # w8 for the updatePopUp win to initialize then update
        self.updatePopUp.after(100, self._updateBackendAndFrontend)

