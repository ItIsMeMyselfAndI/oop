# external/built-in modules/libs
import customtkinter as ctk


class Save(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font = ctk.CTkFont(family="Bodoni MT", size=20, slant="italic", weight="normal")
        self.btn = ctk.CTkButton(self, width=270, height=40, text="Save Changes",
                                 font=self.font, text_color="white",
                                 fg_color="#559eef", hover_color="#427cbd",
                                 corner_radius=10)
        self.btn.pack(pady=(10,10))