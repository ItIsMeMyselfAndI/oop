# external/built-in modules/libs
import customtkinter as ctk
from tkinter import messagebox
# our modules/libs
from backend.transaction_manager import Transaction
from frontend.styles import BaseStyles # paddings, dimensions, colors, etc
from frontend.components.popup_win import PopUpWin


#--------------------------------------------------------------------------------------------------------


class SubmitBTN(ctk.CTkButton):
    def __init__(self, master, user_id, tm, pages, app, popup_title, popup_text, popup_font, **kwargs):
        super().__init__(master, **kwargs)
        self.app = app
        self.user_id = user_id
        self.tm = tm
        self.pages = pages
        # update popup
        self.configure(command=self.onClickSubmit)
        self.updatePopUp = PopUpWin(
            title=popup_title,
            msg=popup_text,
            font=popup_font,
            enable_close=False,
            master=self.app,
            fg_color=BaseStyles.WHITE,
            enable_frame_blocker=False
        )

    
    def _updateBackendAndFrontend(self):
        # save to database
        for page_name, page in self.pages.items():
            try:
                if page_name == "login" and page.is_current_page == True:
                    pass
                elif page_name == "edit" and page.is_current_page == True:
                    self.pages["edit"].saveEditedTransactionToDatabase()
                elif page_name == "add" and page.is_current_page == True:
                    self.pages["add"].saveNewTransactionToDatabase()
            except ValueError:
                messagebox.showwarning(title="[Invalid] Input", message="Only enter positive decimal number for amount")
                return

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

