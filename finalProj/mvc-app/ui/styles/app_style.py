from ui.styles.base_style import BaseStyles, scale

class AppStyles:
    WIN_W = BaseStyles.SCREEN_W
    WIN_H = BaseStyles.SCREEN_H

    WIN_FG_COLOR = BaseStyles.GREY
    
    POPUP_WIN_W = scale(400)
    POPUP_WIN_H = scale(200)
    POPUP_TEXT_COLOR = BaseStyles.BLACK

    LOGIN_PAGE_FG_COLOR = BaseStyles.TRANSPARENT
    LOGIN_FORM_FG_COLOR = BaseStyles.WHITE

    SIDEBAR_FG_COLOR = BaseStyles.WHITE
    SIDEBAR_H = BaseStyles.SCREEN_H

    MAIN_PAGE_FRAME_W = scale(1830)
    MAIN_PAGE_FRAME_H = scale(1080)

    LOAD_POP_UP_FG_COLOR = BaseStyles.WHITE
    UPDATE_POP_UP_FG_COLOR = BaseStyles.WHITE
    CLOSE_APP_POP_UP_FG_COLOR = BaseStyles.WHITE
    
    SAVE_BTN_W = scale(350)
    SAVE_BTN_H = scale(60)
    SAVE_BTN_TEXT_COLOR = BaseStyles.WHITE
    SAVE_BTN_FG_COLOR= BaseStyles.DARKEST_BLUE
    SAVE_BTN_HOVER_COLOR = BaseStyles.DARK_BLUE