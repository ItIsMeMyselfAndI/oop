# external/built-in modules/libs
import customtkinter as ctk
# our modules/libs
from ui.styles import BaseStyles # paddings, dimensions, colors, etc


class PopUpWin(ctk.CTkToplevel):
    def __init__(self, title: str, msg: str, enable_close: bool, enable_frame_blocker: bool, font: tuple, text_color: str, width: int, height: int, master, **kwargs):
        super().__init__(master, **kwargs)
        self.enable_close = enable_close
        self.enable_frame_blocker = enable_frame_blocker
        # initialize win dimensions
        x_pos = int((BaseStyles.SCREEN_W / 2) - (width / 2))
        y_pos = int((BaseStyles.SCREEN_H / 2) - (height / 2))
        # create win
        self.title(title)
        self.geometry(f"{width}x{height}+{x_pos}+{y_pos}")
        self.resizable(width=False, height=False)
        # create content
        self.label = ctk.CTkLabel(master=self, font=font, text=msg, text_color=text_color,
                                  width=width, height=height, wraplength=width)
        self.label.pack(anchor="center")
        # hide win
        self.withdraw()
        # place on top of other wins
        self.attributes("-topmost", True)
        # block app input w/ frame
        self.input_blocker_frame = ctk.CTkFrame(master=master, fg_color=BaseStyles.SKY_BLUE,
                                                width=BaseStyles.SCREEN_W, height=BaseStyles.SCREEN_H)
        # disable manual close -> closes automatically
        self.protocol("WM_DELETE_WINDOW", self.closeWin)


    def closeWin(self):
        if self.enable_close:
            self.hideWin()


    def showWin(self):
        if self.enable_frame_blocker:
            self.input_blocker_frame.place(relx=0.0, rely=0.0) # cover screen w/ transparent frame
        self.deiconify() # show win


    def hideWin(self):
        if self.enable_frame_blocker:
            self.after(100, self.input_blocker_frame.place_forget) # uncover screen w/ transparent frame
        self.after(200, self.withdraw) # hide win
