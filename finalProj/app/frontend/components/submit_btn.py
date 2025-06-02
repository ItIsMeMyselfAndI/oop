# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from backend.transaction_manager import Transaction
from frontend.styles import BaseStyles, SaveStyles # paddings, dimensions, colors, etc
from frontend.components.popup_win import PopUpWin




# save section
class SubmitBTN(ctk.CTkButton):
    def __init__(self, master, user_id, tm, pages, app, popup_title, popup_text, popup_font, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app
        self.user_id = user_id
        self.tm = tm
        self.pages = pages
        # create button
        # create update popup
        self.configure(command=self.onClickSubmit)
        self.updatePopUp = PopUpWin(title=popup_title, msg=popup_text, font=popup_font,
                                    enable_close=False, master=self.app, fg_color=BaseStyles.WHITE)
        # # create invalid input popups
        # self.emptyDescriptionPopUp = PopUpWin(title="[Err] Invalid Input", msg="Only submit non-empty description.\nTry again.", enable_close=True,
        #                                       master=self.app, fg_color=BaseStyles.WHITE)
        # self.invalidAmountPopUp = PopUpWin(title="[Err] Invalid Input", msg="Only submit decimal number for amount.\nTry again.", enable_close=True,
        #                                    master=self.app, fg_color=BaseStyles.WHITE)
        # self.emptyAmountPopUp = PopUpWin(title="[Err] Invalid Input", msg="Only submit non-empty amount.\nTry again.", enable_close=True,
        #                                  master=self.app, fg_color=BaseStyles.WHITE)
        # display button
    
    def _updateBackendAndFrontend(self):
        # save to database
        for page_name, page in self.pages.items():
            if page_name == "login" and page.isCurrentPage == True:
                pass
            elif page_name == "edit" and page.isCurrentPage == True:
                self.pages["edit"].saveEditedTransactionToDatabase()
            elif page_name == "add" and page.isCurrentPage == True:
                self.pages["add"].saveNewTransactionToDatabase()
        # update pages
        self.pages["profile"].updatePageDisplay()
        self.pages["home"].updatePageDisplay()
        self.pages["edit"].updatePageDisplay()
        self.pages["history"].updatePageDisplay()

    def onClickSubmit(self):
        # start updatePopUp
        print("\nstart update")
        self.updatePopUp.showWin()
        # w8 for the updatePopUp win to initialize then update
        self.updatePopUp.after(100, self._updateBackendAndFrontend)
        # end updatePopUp
        self.updatePopUp.hideWin()
        print("\nend update")

