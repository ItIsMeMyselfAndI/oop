from frontend.styles.base import BaseStyles, scale


# ---- exclusive for home page ----
class HomeStyles:
    # header (ideal w: 1630)
    HOME_IMG_W = scale(200)
    HOME_IMG_H = scale(200)
    HOME_IMG_BG_W = scale(240)
    HOME_IMG_BG_H = scale(240)
    HOME_IMG_BG_COLOR = BaseStyles.TRANSPARENT

    BALANCE_FRAME_FG_COLOR = BaseStyles.TRANSPARENT
    BALANCE_TITLE_LABEL_FG_COLOR = BaseStyles.TRANSPARENT
    BALANCE_TITLE_TEXT_COLOR = BaseStyles.WHITE
    BALANCE_AMOUNT_LABEL_W = scale(1290)
    BALANCE_AMOUNT_LABEL_FG_COLOR = BaseStyles.TRANSPARENT
    BALANCE_AMOUNT_TEXT_COLOR = BaseStyles.WHITE

    
    # table header/row
    TABLE_ROW_H = scale(40) 

    DATE_COL_W = scale(180)
    DATE_COL_FG_COLOR = BaseStyles.TRANSPARENT
    DATE_COL_TEXT_COLOR = BaseStyles.DARK_GREY

    TYPE_COL_W = scale(250)
    TYPE_COL_FG_COLOR = BaseStyles.TRANSPARENT
    TYPE_COL_TEXT_COLOR = BaseStyles.DARK_GREY

    CATEGORY_COL_W = scale(250)
    CATEGORY_COL_FG_COLOR = BaseStyles.TRANSPARENT
    CATEGORY_COL_TEXT_COLOR = BaseStyles.DARK_GREY

    DESCRIPTION_COL_W = scale(390)
    DESCRIPTION_COL_FG_COLOR = BaseStyles.TRANSPARENT
    DESCRIPTION_COL_TEXT_COLOR = BaseStyles.DARK_GREY

    AMOUNT_COL_W = scale(390)
    AMOUNT_COL_FG_COLOR = BaseStyles.TRANSPARENT
    AMOUNT_COL_TEXT_COLOR = BaseStyles.DARK_GREY


    # main table
    TABLE_TITLE_SECTION_FG_COLOR = BaseStyles.BLUE
    TABLE_TITLE_TEXT_COLOR = BaseStyles.WHITE
    TABLE_TITLE_SECTION_W = scale(1630)
    TABLE_TITLE_SECTION_H = scale(100)

    TABLE_HEADER_FG_COLOR = BaseStyles.WHITE
    
    TABLE_BODY_FG_COLOR = BaseStyles.WHITE
    TABLE_BODY_W = scale(1560) - 20 # minus unchangeable sidebar width
    TABLE_BODY_H = scale(500)

    TABLE_ROW_FG_COLOR = BaseStyles.TRANSPARENT


    # monthly report
    MONTHLY_TITLE_SECTION_W = scale(1630)
    MONTHLY_TITLE_SECTION_H = scale(100)
    MONTHLY_TITLE_SECTION_FG_COLOR = BaseStyles.BLUE
    MONTHLY_TITLE_TEXT_COLOR = BaseStyles.WHITE

    MONTHLY_GRAPHS_SECTION_FG_COLOR = BaseStyles.TRANSPARENT
    MONTHLY_GRAPH_W_IN = scale(760) / BaseStyles.DPI
    MONTHLY_GRAPH_H_IN = scale(700) / BaseStyles.DPI
    MONTHLY_GRAPH_TITLE_SIZE = scale(15) 
    MONTHLY_GRAPH_LABEL_SIZE = scale(10)
    MONTHLY_INCOME_GRAPH_FRAME_FG_COLOR = BaseStyles.WHITE
    MONTHLY_EXPENSE_GRAPH_FRAME_FG_COLOR = BaseStyles.WHITE


    # quarterly report
    QUARTERLY_TITLE_SECTION_W = scale(1630)
    QUARTERLY_TITLE_SECTION_H = scale(100)
    QUARTERLY_TITLE_SECTION_FG_COLOR = BaseStyles.BLUE
    QUARTERLY_TITLE_TEXT_COLOR = BaseStyles.WHITE
    
    QUARTERLY_GRAPH_SECTION_W = scale(1580)
    QUARTERLY_GRAPH_SECTION_H = scale(700)
    QUARTERLY_GRAPHS_SECTION_FG_COLOR = BaseStyles.WHITE


    # main page
    SCROLL_FRAME_W = BaseStyles.SCREEN_W - BaseStyles.SIDEBAR_W
    SCROLL_FRAME_H = BaseStyles.SCREEN_H
    SCROLL_FRAME_FG_COLOR = BaseStyles.TRANSPARENT

    HEADER_SECTION_FG_COLOR = BaseStyles.BLUE
    TABLE_SECTION_FG_COLOR = BaseStyles.TRANSPARENT
    MONTHLY_SECTION_FG_COLOR = BaseStyles.TRANSPARENT
    QUARTERLY_SECTION_FG_COLOR = BaseStyles.TRANSPARENT


