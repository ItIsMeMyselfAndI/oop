from frontend.styles.base import BaseStyles, scale


# ---- exclusive for sidebar ----
class SidebarStyles:
    BTN_W = scale(70)
    BTN_H = scale(70)

    OFF_BTN_FG_COLOR = BaseStyles.WHITE
    OFF_BTN_HOVER_COLOR = BaseStyles.LIGHT_GREY

    ON_BTN_FG_COLOR = BaseStyles.BLUE
    ON_BTN_HOVER_COLOR = BaseStyles.DARK_BLUE

    IMG_W = scale(40)
    IMG_H = scale(40)