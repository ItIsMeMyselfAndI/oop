from frontend.styles.base import BaseStyles, scale

class LoginStyles:
    LOGO_IMG_W = scale(120)
    LOGO_IMG_H = scale(120)
    LOGO_IMG_BG_W = scale(120)
    LOGO_IMG_BG_H = scale(120)
    LOGO_IMG_BG_COLOR = BaseStyles.TRANSPARENT

    TITLE_LABEL_FONT = ("Arial", scale(35), "bold")
    TITLE_TEXT_COLOR = "#333333"
    TITLE_LABEL_FG_COLOR = BaseStyles.TRANSPARENT

    uname_entry_FONT = ("Arial", scale(20), "bold")
    uname_entry_TEXT_COLOR = "#292929"
    uname_entry_FG_COLOR = "#d9d9d9"
    USER_PLACEHOLDER_TEXT_COLOR = "#545454"
    uname_entry_W = scale(350)
    uname_entry_H = scale(60)

    PASS_ENTRY_FONT = ("Arial", scale(20), "bold")
    PASS_ENTRY_TEXT_COLOR = "#292929"
    PASS_ENTRY_FG_COLOR = "#d9d9d9"
    PASS_PLACEHOLDER_TEXT_COLOR = "#545454"
    PASS_ENTRY_W = scale(350)
    PASS_ENTRY_H = scale(60)

    LOGIN_BTN_FONT = ("Arial", scale(20), "bold")
    LOGIN_BTN_TEXT_COLOR = BaseStyles.WHITE
    LOGIN_BTN_FG_COLOR = BaseStyles.DARKEST_BLUE
    LOGIN_BTN_HOVER_COLOR = BaseStyles.DARK_BLUE
    LOGIN_BTN_W = scale(350)
    LOGIN_BTN_H = scale(60)
    
    SIGNUP_BTN_FONT = ("Arial", scale(20), "bold")
    SIGNUP_BTN_TEXT_COLOR = BaseStyles.WHITE
    SIGNUP_BTN_FG_COLOR = BaseStyles.DARK_YELLOW
    SIGNUP_BTN_HOVER_COLOR = BaseStyles.YELLOW
    SIGNUP_BTN_W = scale(350)
    SIGNUP_BTN_H = scale(60)