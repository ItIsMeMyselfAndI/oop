from frontend.styles.base import BaseStyles, scale


# ---- exclusive for add page ----
class AddStyles:
    # header
    HEADER_TITLE_LABEL_W = scale(1630)
    HEADER_TITLE_LABEL_FG_COLOR = BaseStyles.TRANSPARENT
    HEADER_TITLE_TEXT_COLOR = BaseStyles.DARK_GREY


    # transaction form
    FORM_TOP_SECTION_FG_COLOR = BaseStyles.WHITE
    
    DATE_MENU_H = scale(60)
    YEAR_MENU_W = scale(450)
    MONTH_MENU_W = scale(500) 
    DAY_MENU_W = scale(450)
    DATE_LABEL_FG_COLOR = BaseStyles.TRANSPARENT
    DATE_LABEL_TEXT_COLOR = BaseStyles.DARK_GREY
    DATE_MENU_FRAME_FG_COLOR = BaseStyles.TRANSPARENT
    DATE_MENU_FG_COLOR = BaseStyles.BLUE
    DATE_MENU_TEXT_COLOR = BaseStyles.DARK_GREY
    DATE_DROPDOWN_FG_COLOR = BaseStyles.WHITE
    DATE_DROPDOWN_HOVER_COLOR = BaseStyles.BLUE
    DATE_DROPDOWN_TEXT_COLOR = BaseStyles.DARK_GREY

    FORM_MID_SECTION_FG_COLOR = BaseStyles.WHITE

    CATEGORY_MENU_W = scale(800)
    CATEGORY_MENU_H = scale(60)
    CATEGORY_LABEL_FG_COLOR = BaseStyles.TRANSPARENT
    CATEGORY_LABEL_TEXT_COLOR = BaseStyles.DARK_GREY
    CATEGORY_MENU_FG_COLOR = BaseStyles.BLUE
    CATEGORY_MENU_TEXT_COLOR = BaseStyles.DARK_GREY
    CATEGORY_DROPDOWN_FG_COLOR = BaseStyles.WHITE
    CATEGORY_DROPDOWN_HOVER_COLOR = BaseStyles.BLUE
    CATEGORY_DROPDOWN_TEXT_COLOR = BaseStyles.DARK_GREY

    DESCRIPTION_ENTRY_W = scale(600)
    DESCRIPTION_ENTRY_H = scale(60)
    DESCRIPTION_LABEL_FG_COLOR = BaseStyles.TRANSPARENT
    DESCRIPTION_LABEL_TEXT_COLOR = BaseStyles.DARK_GREY
    DESCRIPTION_ENTRY_FG_COLOR = BaseStyles.LIGHT_BLUE
    DESCRIPTION_ENTRY_BG_COLOR = BaseStyles.TRANSPARENT
    DESCRIPTION_ENTRY_TEXT_COLOR = BaseStyles.DARK_GREY
    DESCRIPTION_PLACEHOLDER_TEXT_COLOR = BaseStyles.GREY
    
    FORM_BOT_SECTION_FG_COLOR = BaseStyles.WHITE

    AMOUNT_ENTRY_W = scale(1430)
    AMOUNT_ENTRY_H = scale(60)
    AMOUNT_LABEL_FG_COLOR = BaseStyles.TRANSPARENT
    AMOUNT_LABEL_TEXT_COLOR = BaseStyles.DARK_GREY
    AMOUNT_ENTRY_FG_COLOR = BaseStyles.LIGHT_BLUE
    AMOUNT_ENTRY_BG_COLOR = BaseStyles.TRANSPARENT
    AMOUNT_ENTRY_TEXT_COLOR = BaseStyles.DARK_GREY
    AMOUNT_PLACEHOLDER_TEXT_COLOR = BaseStyles.GREY
    

    # page tabs
    TAB_W = scale(350)
    TAB_H = scale(60)

    OFF_TAB_BTN_FG_COLOR = BaseStyles.WHITE
    OFF_TAB_BTN_HOVER_COLOR = BaseStyles.LIGHT_GREY
    OFF_TAB_TEXT_COLOR = BaseStyles.DARK_GREY

    ON_TAB_BTN_FG_COLOR = BaseStyles.BLUE
    ON_TAB_BTN_HOVER_COLOR = BaseStyles.DARK_BLUE
    ON_TAB_TEXT_COLOR = BaseStyles.WHITE


    # main page
    HEADER_SECTION_FG_COLOR = BaseStyles.TRANSPARENT

    FORMS_SECTION_FG_COLOR = BaseStyles.TRANSPARENT
    FORM_FRAME_FG_COLOR = BaseStyles.WHITE

    TABS_FRAME_FG_COLOR = BaseStyles.TRANSPARENT