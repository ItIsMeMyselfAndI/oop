# external/built-in modules/libs
import customtkinter as ctk
from tkinter import messagebox
# our modules/libs
from backend.transaction_manager import Transaction
from frontend.styles import BaseStyles # paddings, dimensions, colors, etc
from frontend.components.popup_win import PopUpWin

from typing import Dict
from controllers.base_controller import Controller

#--------------------------------------------------------------------------------------------------------


class SubmitBTN(ctk.CTkButton):
    def __init__(self, controller_per_page: Dict[str, Controller], updating_popup, master, **kwargs):
        super().__init__(master, **kwargs)
        self.controller_per_page = controller_per_page
        self.updating_popup = updating_popup

        self.configure(command=self.onClickSubmit)

    
    def onClickSubmit(self):
        # start updating_popup
        self.updating_popup.showWin()
        # w8 for the updating_popup win to initialize then update
        self.updating_popup.after(100, self._update_db_and_gui)
        # end updating_popup
        self.updating_popup.hideWin()
        self.update_idletasks()


    def _update_db_and_gui(self):
        print("[DEBUG] updating the app...")
        # save to database
        for page_name, controller in self.controller_per_page.items():
            try:
                if page_name == "login" and controller.model.is_current_page == True:
                    pass
                elif page_name == "edit" and controller.model.is_current_page == True:
                    self.controller_per_page["edit"].model.save_edited_transaction_to_database(controller.view.form_per_transaction_type)
                elif page_name == "add" and controller.model.is_current_page == True:
                    self.controller_per_page["add"].model.save_new_transaction_to_database(controller.view.form_per_transaction_type)

            except ValueError as e:
                messagebox.showwarning(title="[Invalid] Input", message="Only enter positive decimal number for amount")
                print(f"[DEBUG] app update failed: {e}")
                return

        # update pages
        self.controller_per_page["profile"].update_display()
        self.controller_per_page["home"].update_display()
        self.controller_per_page["edit"].update_display()
        self.controller_per_page["history"].update_display()
        print("[DEBUG] app updated successfully")

    