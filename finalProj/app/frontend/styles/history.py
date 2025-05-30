from frontend.styles.base import scale


# ---- exclusive for history page ----
class HistoryStyles:
    HEADER_LABEL_H = scale(180)
    HEADER_LABEL_W = scale(1080)

    TABLE_FILTER_MENU_H = scale(40)
    TABLE_FILTER_MENU_W = scale(220)

    TABLE_COL_W1 = scale(180)
    TABLE_COL_W2 = scale(250)
    TABLE_COL_W3 = scale(390)

    TABLE_ROW_H = scale(40) 

    TABLE_BODY_W = scale(1560) - 20 # minus unchangeable sidebar width
    TABLE_BODY_H = scale(500)

    TABLE_NAV_BTN_W = scale(100)
    TABLE_NAV_BTN_H = scale(40)