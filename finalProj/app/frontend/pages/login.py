import tkinter
import customtkinter
from PIL import Image
from pathlib import Path
from customtkinter import CTkButton, CTkEntry, CTkFrame, CTkImage

# from ..utilities.styles import * # contains paddings, dimensions, colors, etc


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

user_text = "Username"
pass_text = "Password"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.configure(fg_color="#cef2ff")
        self.geometry("1920x1080")
        self.title("Login Page")
        self.actual_password = ""
        self.mask_job = None
        self.password_started = False

        ICONS_FOLDER = Path(__file__).resolve().parent.parent.parent / "assets" / "icons"
        self.logo = CTkImage(dark_image=Image.open(f"{ICONS_FOLDER}/logo.png"),
                             light_image=Image.open(f"{ICONS_FOLDER}/logo.png"),
                             size=(120, 120))

        self.frame = CTkFrame(master=self, fg_color="#ffffff", width=550, height=785, corner_radius=50)
        self.frame.place(x=686.1, y=147.4)

        self.text1 = customtkinter.CTkLabel(master=self, text="Login", font=("Arial", 35, "bold"),
                                            text_color="#333333", bg_color="#ffffff")
        self.text1.place(x=915, y=398)

        self.user_entry = CTkEntry(master=self,
                                   placeholder_text=user_text,
                                   placeholder_text_color="#545454",
                                   width=377,
                                   height=60,
                                   text_color="#292929",
                                   font=("Arial", 17, "bold"),
                                   corner_radius=50,
                                   border_width=0,
                                   fg_color="#d9d9d9",
                                   bg_color="#ffffff")
        self.user_entry.place(x=771.5, y=525)

        self.pass_entry = CTkEntry(master=self,
                                   placeholder_text=pass_text,
                                   placeholder_text_color="#545454",
                                   width=377,
                                   height=60,
                                   text_color="#292929",
                                   font=("Arial", 17, "bold"),
                                   corner_radius=50,
                                   border_width=0,
                                   fg_color="#d9d9d9",
                                   bg_color="#ffffff",
                                   show="")
        self.pass_entry.place(x=771.5, y=605)

        self.actual_password = ""
        self.mask_job = None
        self.pass_entry.bind("<KeyRelease>", self.on_password_key_release)

        self.login_button = CTkButton(master=self,
                                  text="LOGIN",
                                  corner_radius=50,
                                  fg_color="#427cbd",
                                  text_color="#ffffff",
                                  hover_color="#336194",
                                  font=("Arial", 20, "bold"),
                                  width=380,
                                  height=60,
                                  command=self.login,
                                  bg_color="#ffffff")
        self.login_button.place(x=770, y=700)

        self.signup_button = CTkButton(master=self,
                                   text="SIGN UP",
                                   corner_radius=50,
                                   text_color="#ffffff",
                                   fg_color="#7ed957",
                                   hover_color="#63ab45",
                                   font=("Arial", 20, "bold"),
                                   width=380,
                                   height=60,
                                   command=self.sign_up,
                                   bg_color="#ffffff")
        self.signup_button.place(x=770, y=777)

        self.forgot = CTkButton(master=self,
                                text="Forgot Password",
                                corner_radius=50,
                                text_color="#333333",
                                fg_color="#ffffff",
                                hover_color="#ffffff",
                                font=("Arial", 13.7, "bold"),
                                width=380,
                                height=60,
                                command=self.forgot_password,
                                bg_color="#ffffff")
        self.forgot.place(x=768.6, y=835)

        self.logo_icon = customtkinter.CTkLabel(self, text="", image=self.logo)
        self.logo_icon.place(x=900, y=227.4)

        #Bind for the Additional Stuff
        self.pass_entry.bind("<KeyRelease>", self.on_password_key_release)
        self.actual_password = ""
        self._masking_job = self.after(800, self.mask_password)
        self.user_entry.bind("<FocusIn>", self.on_focus_in)
        self.user_entry.bind("<FocusOut>", self.on_focus_out)
        self.pass_entry.bind("<KeyRelease>", self.on_password_key_release)
        self.pass_entry.bind("<FocusOut>", self.on_password_focus_out)
        self.bind("<Button-1>", self.on_click_outside)

    def on_password_focus_out(self, _event):
        if not self.actual_password:
            self.pass_entry.configure(show="")

    def login(self):
        username = self.user_entry.get()
        password = self.actual_password
        print("Username:", username)
        print("Password:", password)

    def sign_up(self):
        pass

    def forgot_password(self):
        pass

    #Additional Stuff for Placeholder
    def on_focus_in(self, _event):
        if self.user_entry.get() == user_text:
            self.user_entry.delete(0, tkinter.END)
    def on_focus_out(self, _event):
        if not self.user_entry.get():
            self.user_entry.insert(0, user_text)
    def on_click_outside(self, _event):
        if not self.user_entry.get():
            self.user_entry.insert(0, user_text)

    def on_password_key_release(self, _event):
        if self.mask_job:
            self.after_cancel(self.mask_job)

        current_text = self.pass_entry.get()

        if not current_text:
            self.actual_password = ""
            self.password_started = False
            self.pass_entry.configure(show="")
            return
        self.password_started = True

        if len(current_text) < len(self.actual_password):
            self.actual_password = self.actual_password[:len(current_text)]
        else:
            self.actual_password += current_text[len(self.actual_password):]
        self.pass_entry.configure(show="")
        self.pass_entry.delete(0, tkinter.END)
        self.pass_entry.insert(0, self.actual_password)
        self.mask_job = self.after(800, self.mask_password)

    def mask_password(self):
        if not self.password_started:
            return
        self.pass_entry.configure(show="*")
        self.pass_entry.delete(0, tkinter.END)
        self.pass_entry.insert(0, "*" * len(self.actual_password))


if __name__ == "__main__":
    app = App()
    app.mainloop()