# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from frontend.styles import BaseStyles, PopUpWinStyles # paddings, dimensions, colors, etc


class PopUpWin(ctk.CTkToplevel):
    def __init__(self, title, msg, enable_close, master, **kwargs):
        super().__init__(master, **kwargs)
        self.font1 = ctk.CTkFont(family="Bodoni MT", size=BaseStyles.FONT_SIZE_2, slant="italic", weight="normal")
        # initialize win dimensions
        self.x_pos = int((BaseStyles.SCREEN_W / 2) - (PopUpWinStyles.POPUP_WIN_W / 2))
        self.y_pos = int((BaseStyles.SCREEN_H / 2) - (PopUpWinStyles.POPUP_WIN_H / 2))
        # create win
        self.title(title)
        self.geometry(f"{PopUpWinStyles.POPUP_WIN_W}x{PopUpWinStyles.POPUP_WIN_H}+{self.x_pos}+{self.y_pos}")
        self.resizable(width=False, height=False)
        # create content
        self.label = ctk.CTkLabel(self, font=self.font1, text=msg, text_color=BaseStyles.DARK_GREY,
                                  width=PopUpWinStyles.POPUP_WIN_W, height=PopUpWinStyles.POPUP_WIN_H,
                                  wraplength=PopUpWinStyles.POPUP_WIN_W)
        self.label.pack(anchor="center")
        # hide win
        self.withdraw()
        # block app input w/ frame
        self.input_blocker_frame = ctk.CTkFrame(master=master, fg_color=BaseStyles.SKY_BLUE,
                                                width=BaseStyles.SCREEN_W, height=BaseStyles.SCREEN_H)
        # disable manual close -> closes automatically
        if not enable_close:
            self.protocol("WM_DELETE_WINDOW", self.disabledCloseWin)

    def disabledCloseWin(self):
        pass

    def showWin(self):
        self.input_blocker_frame.place(relx=0.0, rely=0.0) # cover screen w/ transparent frame
        self.deiconify() # show win

    def hideWin(self):
        self.after(100, self.input_blocker_frame.place_forget) # uncover screen w/ transparent frame
        self.after(100, self.withdraw) # hide win
