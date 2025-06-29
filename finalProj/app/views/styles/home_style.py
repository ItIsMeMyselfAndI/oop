from views.styles.base_style import BaseStyles, scale


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


    # table
    TABLE_TITLE_SECTION_FG_COLOR = BaseStyles.DARKEST_BLUE
    TABLE_TITLE_TEXT_COLOR = BaseStyles.WHITE
    TABLE_TITLE_SECTION_W = scale(1630)
    TABLE_TITLE_SECTION_H = scale(100)

    TABLE_HEADER_FG_COLOR = BaseStyles.WHITE
    TABLE_ROW_FG_COLOR = BaseStyles.TRANSPARENT
    
    TABLE_BODY_W = scale(1560) - 20 # minus unchangeable sidebar width
    TABLE_BODY_H = scale(500)
    TABLE_BODY_FG_COLOR = BaseStyles.WHITE


    # monthly report
    MONTHLY_TITLE_SECTION_W = scale(1630)
    MONTHLY_TITLE_SECTION_H = scale(100)
    MONTHLY_TITLE_SECTION_FG_COLOR = BaseStyles.DARKEST_BLUE
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
    QUARTERLY_TITLE_SECTION_FG_COLOR = BaseStyles.DARKEST_BLUE
    QUARTERLY_TITLE_TEXT_COLOR = BaseStyles.WHITE

    QUARTERLY_GRAPHS_SECTION_FG_COLOR = BaseStyles.WHITE
    QUARTERLY_GRAPH_W_IN = scale(1560) / BaseStyles.DPI
    QUARTERLY_GRAPH_H_IN = scale(700) / BaseStyles.DPI
    QUARTERLY_GRAPH_TITLE_SIZE = scale(15) 
    QUARTERLY_GRAPH_LABEL_SIZE = scale(10)

    # main page
    SCROLL_FRAME_W = BaseStyles.SCREEN_W - BaseStyles.SIDEBAR_W
    SCROLL_FRAME_H = BaseStyles.SCREEN_H
    SCROLL_FRAME_FG_COLOR = BaseStyles.TRANSPARENT

    HEADER_SECTION_FG_COLOR = BaseStyles.DARKEST_BLUE
    TABLE_SECTION_FG_COLOR = BaseStyles.TRANSPARENT
    MONTHLY_SECTION_FG_COLOR = BaseStyles.TRANSPARENT
    QUARTERLY_SECTION_FG_COLOR = BaseStyles.TRANSPARENT