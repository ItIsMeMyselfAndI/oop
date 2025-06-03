from frontend.styles.base import BaseStyles, scale

class LoginStyles:
    LOGIN_FRAME_FG_COLOR = BaseStyles.WHITE

    LOGO_IMG_W = scale(120)
    LOGO_IMG_H = scale(120)
    LOGO_IMG_BG_W = scale(120)
    LOGO_IMG_BG_H = scale(120)
    LOGO_IMG_BG_COLOR = BaseStyles.TRANSPARENT

    TITLE_LABEL_FONT = ("Arial", scale(35), "bold")
    TITLE_TEXT_COLOR = "#333333"
    TITLE_LABEL_FG_COLOR = BaseStyles.TRANSPARENT

    USER_ENTRY_FONT = ("Arial", scale(20), "bold")
    USER_ENTRY_TEXT_COLOR = "#292929"
    USER_ENTRY_FG_COLOR = "#d9d9d9"
    USER_PLACEHOLDER_TEXT_COLOR = "#545454"
    USER_ENTRY_W = scale(350)
    USER_ENTRY_H = scale(60)

    PASS_ENTRY_FONT = ("Arial", scale(20), "bold")
    PASS_ENTRY_TEXT_COLOR = "#292929"
    PASS_ENTRY_FG_COLOR = "#d9d9d9"
    PASS_PLACEHOLDER_TEXT_COLOR = "#545454"
    PASS_ENTRY_W = scale(350)
    PASS_ENTRY_H = scale(60)

    LOGIN_BUTTON_FONT = ("Arial", scale(20), "bold")
    LOGIN_BUTTON_TEXT_COLOR = "#ffffff"
    LOGIN_BUTTON_FG_COLOR = BaseStyles.BLUE
    LOGIN_BUTTON_HOVER_COLOR = BaseStyles.DARK_BLUE
    LOGIN_BUTTON_W = scale(350)
    LOGIN_BUTTON_H = scale(60)
    
    SIGNUP_BUTTON_FONT = ("Arial", scale(20), "bold")
    SIGNUP_BUTTON_TEXT_COLOR = "#ffffff"
    SIGNUP_BUTTON_FG_COLOR = "#7ed957"
    SIGNUP_BUTTON_HOVER_COLOR = BaseStyles.GREEN
    SIGNUP_BUTTON_W = scale(350)
    SIGNUP_BUTTON_H = scale(60)