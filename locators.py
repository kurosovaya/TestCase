from selenium.webdriver.common.by import By


class MainPageLocators():
    SEARCH_BAR = (By.ID, "text")
    POPUP_CONTENT = (By.CLASS_NAME, "mini-suggest__popup-content")
    IMAGES_BUTTON = (By.LINK_TEXT, "Картинки")


class SreachResultPageLocators():
    SEARCH_RESULTS = (By.CLASS_NAME, "serp-item")
    ADS_LABEL = (By.CSS_SELECTOR,
                 "div[class='label label_theme_direct label_horizontal-padding_m label_font_own organic__label organic__label_align_right label_padding_1px-5px-3px-6px label_border-radius_20']")


class ImagesPageLocators():
    IMAGE_BOX = (By.CLASS_NAME, "image__image")
    IB_NEXT_BUTTON = (
        By.CSS_SELECTOR, "div[class='cl-viewer-navigate__item cl-viewer-navigate__item_right']")
    IB_PREV_BUTTON = (
        By.CSS_SELECTOR, "div[class='cl-viewer-navigate__item cl-viewer-navigate__item_left']")
