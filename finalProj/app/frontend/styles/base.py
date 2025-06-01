import customtkinter as ctk

# convert ideal pixel count (when screen h is 1080) to actual screen pixel count (base on actual screen h)
def scale(ideal_pixels):
    return int(ideal_pixels / IDEAL_SCREEN_H * SCREEN_H)

def screenDimensions():
    temp_root = ctk.CTk()
    screen_w = temp_root.winfo_screenwidth() #1920
    screen_h = int(0.5625*screen_w) #1080
    dpi = temp_root.winfo_fpixels("1i") #dpi: px per in
    temp_root.destroy()
    return screen_w, screen_h, dpi


# ---- ideal screen dimensions ----
IDEAL_SCREEN_W = 1920
IDEAL_SCREEN_H = 1080
# IDEAL_SCREEN_H = 2000


# ---- actual screen dimensions ----
SCREEN_W, SCREEN_H, DPI = screenDimensions()


class BaseStyles:
    # ---- actual screen dimensions ----
    SCREEN_W = SCREEN_W
    SCREEN_H = SCREEN_H
    DPI = DPI

    # ---- paddings ----
    PAD_1 = scale(10)
    PAD_2 = scale(20)
    PAD_3 = scale(30)
    PAD_4 = scale(40)
    PAD_5 = scale(50)


    # ---- font sizes ----
    FONT_SIZE_1 = scale(20)
    FONT_SIZE_2 = scale(25)
    FONT_SIZE_3 = scale(30)
    FONT_SIZE_4 = scale(40)
    FONT_SIZE_5 = scale(50)
    FONT_SIZE_6 = scale(60)


    # ---- radii ----
    RAD_1 = scale(10)
    RAD_2 = scale(20)


    # ---- colors ----
    TRANSPARENT = "transparent"
    WHITE = "white"
    # reds
    WHITE_RED = "#fdecec"
    LIGHT_RED = "#ffc7c7"
    RED = "#e14242"
    # greens
    WHITE_GREEN = "#dafbf0"
    LIGHT_GREEN = "#b2fee3"
    GREEN = "#28ab58"
    # purples
    WHITE_PURPLE = "#f3eefe"
    LIGHT_PURPLE =  "#d6c5fb"
    PURPLE = "#ceb9fe"
    # blues
    WHITE_BLUE = "#ebf2fe"
    SKY_BLUE = "#cef2ff"
    LIGHT_BLUE = "#bcd4fe"
    BLUE = "#559eef"
    DARK_BLUE = "#427cbd"
    # greys
    LIGHT_GREY = "#c4c4c4"
    GREY = "grey"
    DARK_GREY = "#545454"


    # ---- sidebar ----
    SIDEBAR_W = scale(90)