# external/built-in modules/libs
import customtkinter as ctk
from customtkinter import StringVar, IntVar
from tkinter import messagebox
# our modules/libs
from backend import Account, UserRepository

from models import Model, LoginPageModel
from views.pages import LoginPageView 
from controllers import Controller


#--------------------------------------------------------------------------------------------------------


class LoginPageController(Controller):
    def __init__(self, user_repository: UserRepository, user_id_var: IntVar, username_var: StringVar, page_fg_color, form_fg_color, corner_radius, master):
        self.model = LoginPageModel(user_repository=user_repository, user_id_var=user_id_var, username_var=username_var)
        self.view = LoginPageView(model=self.model, page_fg_color=page_fg_color, form_fg_color=form_fg_color, corner_radius=corner_radius, master=master)


    @property
    def model(self) -> Model:
        return self.__model
    
    
    @model.setter
    def model(self, value: Model):
        self.__model = value


    def run(self):
        self.view.login_button.configure(command=self.on_click_login)
        self.view.signup_button.configure(command=self.on_click_signup)
        self.view.pass_entry.bind("<KeyRelease>", self.on_password_key_release)
    

    def on_click_login(self):
        print("\n[User] LoginStyles")
        username = self.view.uname_entry.get()
        password = self.view.actual_password

        account = Account(username=username, password=password)
        user_id = self.model.u_repo.getAccountID(account)
        if not (account.username and account.password):
            messagebox.showwarning(title="[Invalid] Input", message="Empty field is not allowed")
            print("[Input] Empty field is not allowed")

        elif user_id:
            self.model.user_id_var.set(user_id)
            self.model.username_var.set(username)
            print("\tUsername:", username)
            print("\tPassword:", password)
            self.view.pack_forget()
            self.view.update_idletasks()

        else:
            messagebox.showwarning(title="[DB] No Match Found", message="Incorrect Username or Password")
            print("[DB] No Match Found")


    def on_click_signup(self):
        print("\n[User] Sign Up")
        username = self.view.uname_entry.get()
        password = self.view.actual_password
        account = Account(username=username, password=password)

        # verify action
        is_continue = messagebox.askyesno(title="[Sign Up] New Account",message="Do you want to create a new account?") 
        if not is_continue:
            return
        
        # create new account
        was_added = self.model.u_repo.addAccount(account)
        if not (account.username and account.password):
            messagebox.showwarning(title="[Invalid] Input", message="Empty field is not allowed")
            print("[Input] Empty field is not allowed")

        elif was_added:
            user_id = self.model.u_repo.getAccountID(account)
            self.model.user_id_var.set(user_id)
            self.model.username_var.set(username)
            print("\tUsername:", username)
            print("\tPassword:", password)
            self.view.pack_forget()
            self.view.update_idletasks()

        else:
            messagebox.showwarning(title="[Invalid] Input", message="Username is already taken")
            print("[Input] Username is already taken")


    def on_password_key_release(self, event):
        # cancel masking
        if self.view.mask_id:
            self.view.after_cancel(self.view.mask_id)
            self.view.mask_id = None
        # update pass
        self.view.actual_password = self.view.pass_entry.get()
        # temporarily show the actual password
        self.view.pass_entry.delete(0, ctk.END)
        self.view.pass_entry.insert(0, self.view.actual_password)
        self.view.pass_entry.configure(show="")
        # mask pass after 1 secs
        self.view.mask_id = self.view.after(1000, self._maskPassword)


    def _maskPassword(self):
        # hide pass display
        self.view.pass_entry.delete(0, ctk.END)
        self.view.pass_entry.insert(0, self.view.actual_password)
        self.view.pass_entry.configure(show="*")
    
    
    def update_display(self):
        # print("[DEBUG] updating profile page display...")
        pass