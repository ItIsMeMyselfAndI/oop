from frontend.styles.base import scale


# ---- exclusive for home page ----
class HomeStyles:
    IMG_W = scale(200)
    IMG_H = scale(200)

    IMG_BG_W = scale(240)
    IMG_BG_H = scale(240)

    LABEL_W = scale(1290)

    TABLE_TITLE_SECTION_W = scale(1630)
    TABLE_TITLE_SECTION_H = scale(100)
    
    TABLE_COL_W1 = scale(180)
    TABLE_COL_W2 = scale(250)
    TABLE_COL_W3 = scale(390)

    TABLE_ROW_H = scale(40) 

    TABLE_BODY_W = scale(1560) - 20 # minus unchangeable sidebar width
    TABLE_BODY_H = scale(500)

    REPORT_TITLE_SECTION_W = scale(1630)
    REPORT_TITLE_SECTION_H = scale(100)

    MONTHLY_INCOME_GRAPH_W = scale(760)
    MONTHLY_INCOME_GRAPH_H = scale(700)
    
    MONTHLY_EXPENSE_GRAPH_W = scale(760)
    MONTHLY_EXPENSE_GRAPH_H = scale(700)

    MONTHLY_GRAPH_TITLE_SIZE = scale(15)
    MONTHLY_GRAPH_LABEL_SIZE = scale(10)

    QUARTERLY_GRAPH_SECTION_W = scale(1580)
    QUARTERLY_GRAPH_SECTION_H = scale(700)