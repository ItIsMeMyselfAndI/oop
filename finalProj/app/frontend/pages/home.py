# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from frontend.styles import Styles as s # paddings, dimensions, colors, etc


class HomeHeader(ctk.CTkFrame):
    def __init__(master, **kwargs):
        super().__init__(master, **kwargs)


class Home(ctk.CTkFrame):
    def __init__(self, user_id, tm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.tm = tm
        # initialize state
        self.isCurrentPage = False
        
        # edit nyo nlng dito inyo
        # pag mahaba gawa nyo, pede nyo sya gawin sa 
        # separate file tas import nyo nlng dito,
        # lalo na kung kailangan nyo gumawa ng ibang classes
        # (gaya nung edit page & sidebar)
        label = ctk.CTkLabel(self, text="Home page", text_color=s.DARK_GREY, font=("Arial", 24))
        label.pack(pady=50)

