# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from backend.transaction_manager import Transaction
from frontend.styles import BaseStyles, SaveStyles # paddings, dimensions, colors, etc
from frontend.components.popup_win import PopUpWin




# save section
class SaveBTN(ctk.CTkFrame):
    def __init__(self, user_id, tm, pages, app, master, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app
        self.user_id = user_id
        self.tm = tm
        self.pages = pages
        self.font = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_3, weight="normal", slant="italic" )
        # create button
        self.btn = ctk.CTkButton(self, width=SaveStyles.SAVE_BTN_W, height=SaveStyles.SAVE_BTN_H, text="Save Changes", font=self.font, text_color=BaseStyles.WHITE,
                                 fg_color=BaseStyles.BLUE, hover_color=BaseStyles.DARK_BLUE, corner_radius=BaseStyles.RAD_2, command=self.onClickSave)
        # create update popup
        self.updatePopUp = PopUpWin(title="[Update] Database", msg="Updating transactions...\nPlease wait...",
                                    enable_close=False, master=self.app, fg_color=BaseStyles.WHITE)
        # # create invalid input popups
        # self.emptyDescriptionPopUp = PopUpWin(title="[Err] Invalid Input", msg="Only submit non-empty description.\nTry again.", enable_close=True,
        #                                       master=self.app, fg_color=BaseStyles.WHITE)
        # self.invalidAmountPopUp = PopUpWin(title="[Err] Invalid Input", msg="Only submit decimal number for amount.\nTry again.", enable_close=True,
        #                                    master=self.app, fg_color=BaseStyles.WHITE)
        # self.emptyAmountPopUp = PopUpWin(title="[Err] Invalid Input", msg="Only submit non-empty amount.\nTry again.", enable_close=True,
        #                                  master=self.app, fg_color=BaseStyles.WHITE)
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

    def onClickSave(self):
        # start updatePopUp
        print("\nstart update")
        self.updatePopUp.showWin()
        # w8 for the updatePopUp win to initialize then update
        self.updatePopUp.after(100, self._updateBackendAndFrontend)
        # end updatePopUp
        self.updatePopUp.hideWin()
        print("\nend update")

