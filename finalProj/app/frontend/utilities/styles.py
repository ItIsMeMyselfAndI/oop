import customtkinter as ctk


# get full screen size
temp_root = ctk.CTk()
SCREEN_W = temp_root.winfo_screenwidth() #1920
temp_root.destroy()
SCREEN_H = int(0.5625*SCREEN_W) #1080
print(SCREEN_W, SCREEN_H)

# paddings
PAD_1 = int(0.0093*SCREEN_H) #10
PAD_2 = int(0.0185*SCREEN_H) #20
PAD_3 = int(0.0278*SCREEN_H) #30
PAD_4 = int(0.0370*SCREEN_H) #40
PAD_5 = int(0.0463*SCREEN_H) #50

# font sizes
FONT_SIZE_1 = int(0.0185*SCREEN_H) #20
FONT_SIZE_2 = int(0.0231*SCREEN_H) #25
FONT_SIZE_3 = int(0.0278*SCREEN_H) #30
FONT_SIZE_4 = int(0.0370*SCREEN_H) #40
FONT_SIZE_5 = int(0.0463*SCREEN_H) #50
FONT_SIZE_6 = int(0.0556*SCREEN_H) #60

WHITE= "white"
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

# entry sizes
ENTRY_W1 = int(1.3241*SCREEN_H) #1430
ENTRY_W2 = int(0.5556*SCREEN_H) #600
ENTRY_H = int(0.0556*SCREEN_H) #60

# menu sizes
MENU_W1 = int(0.7407*SCREEN_H) #800
MENU_W2 = int(1.2593*SCREEN_H) #1360 
MENU_H = int(0.0556*SCREEN_H) #60
# date menu sizes 1
YEAR_MENU_W1 = int(0.1667*SCREEN_H) #180
MONTH_MENU_W1 = int(0.2037*SCREEN_H) #220
DAY_MENU_W1 = int(0.1667*SCREEN_H) #180
# date menu sizes 1
YEAR_MENU_W2 = int(0.4167*SCREEN_H) #450
MONTH_MENU_W2 = int(0.4630*SCREEN_H) #500 
DAY_MENU_W2 = int(0.4167*SCREEN_H) #450

# button sizes 1
BTN_W1 = int(0.0648*SCREEN_H) #70
BTN_W2 = int(0.3241*SCREEN_H) #350
# button sizes 2
BTN_H1 = int(0.0648*SCREEN_H) #70
BTN_H2 = int(0.0556*SCREEN_H) #60

# radii
RAD_1 = int(0.0093*SCREEN_H) #10
RAD_2 = int(0.0185*SCREEN_H) #20

# header sizes
HEADER_H = int(0.2593*SCREEN_H) #280
HEADER_W = int(1.5093*SCREEN_H) #1630

HEADER_LABEL_H = int(0.1667*SCREEN_H) #180
HEADER_LABEL_W = int(0.9907*SCREEN_H) #1070


# ---- exclusive for profile page ----
PROFILE_IMG_W = int(0.1852*SCREEN_H) #200
PROFILE_IMG_H = int(0.1852*SCREEN_H) #200

PROFILE_IMG_BG_W = int(0.2222*SCREEN_H) #240
PROFILE_IMG_BG_H = int(0.2222*SCREEN_H) #240

PROFILE_LABEL_W1 = int(0.4630*SCREEN_H) #500
PROFILE_LABEL_W2 = int(0.7222*SCREEN_H) #780

SUMMARY_ELEM_H = int(0.2037*SCREEN_H) #220
SUMMARY_ELEM_W = int(0.6991*SCREEN_H) #755

SUMMARY_IMG_W = int(0.0463*SCREEN_H) #50
SUMMARY_IMG_H = int(0.0463*SCREEN_H) #50

SUMMARY_IMG_FRAME_W = int(0.1111*SCREEN_H) #120
SUMMARY_IMG_FRAME_H = int(0.1111*SCREEN_H) #120

SUMMARY_LABEL_W = int(0.4630*SCREEN_H) #500


# ---- exclusive for history page ----
FILTER_MENU_H = int(0.0370*SCREEN_H) #40
FILTER_MENU_W = int(0.2037*SCREEN_H) #220

TABLE_COL_W1 = int(0.1667*SCREEN_H) #180
TABLE_COL_W2 = int(0.2315*SCREEN_H) #250
TABLE_COL_W3 = int(0.3843*SCREEN_H) #415

TABLE_ROW_H = int(0.0370*SCREEN_H) #40 

TABLE_W = int(1.4722*SCREEN_H) #1590
TABLE_H = int(0.5093*SCREEN_H) #550


# ---- exclusive for sidebar ----
IMG_W = int(0.0370*SCREEN_H) #40
IMG_H = int(0.0370*SCREEN_H) #40


