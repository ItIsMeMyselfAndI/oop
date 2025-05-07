# external/built-in modules/libs
import customtkinter as ctk


class Title(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font = ctk.CTkFont(family="Bodoni MT", size=40, slant="italic", weight="normal")
        self.label = ctk.CTkLabel(self, text="Edit Transaction",
                                  font=self.font, text_color="#545454")
        self.label.pack(side="left", padx=(20,0))