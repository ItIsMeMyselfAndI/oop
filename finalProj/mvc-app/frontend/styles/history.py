from frontend.styles.base import BaseStyles, scale


# ---- exclusive for history page ----
class HistoryStyles:
    # header
    HEADER_TITLE_LABEL_H = scale(180)
    HEADER_TITLE_LABEL_W = scale(1080)
    HEADER_TITLE_LABEL_FG_COLOR = BaseStyles.TRANSPARENT
    HEADER_TITLE_TEXT_COLOR = BaseStyles.WHITE


    # table
    TABLE_HEADER_FG_COLOR = BaseStyles.WHITE
    TABLE_BODY_W = scale(1560) - 20 # minus unchangeable sidebar width
    TABLE_BODY_H = scale(500)
    TABLE_BODY_FG_COLOR = BaseStyles.WHITE
    FILTERS_FRAME_FG_COLOR = BaseStyles.TRANSPARENT
    TABLE_NAV_FG_COLOR = BaseStyles.TRANSPARENT


    # main table
    HEADER_SECTION_FG_COLOR = BaseStyles.BLUE
    TABLE_SECTION_FG_COLOR = BaseStyles.TRANSPARENT
    