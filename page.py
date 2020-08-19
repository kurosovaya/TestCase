from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, ImagesPageLocators, SreachResultPageLocators
from element import BasePageElement


class SearchBarElement(BasePageElement):

    def __init__(self):
        self.locator = "text"


class BasePage():

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    search_bar_element = SearchBarElement()

    def is_searchbar_exist(self):
        return len(WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_elements(*MainPageLocators.SEARCH_BAR))) != 0

    def set_search_item(self, name="Тензор"):
        self.search_bar_element = name

    def is_popup_menu_exist(self):
        return len(WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_elements(*MainPageLocators.POPUP_CONTENT))) != 0

    def press_enter(self):
        self.driver.find_element(
            *MainPageLocators.SEARCH_BAR).send_keys(Keys.RETURN)

    def is_images_button_present(self):
        return len(WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_elements(*MainPageLocators.IMAGES_BUTTON))) != 0

    def press_images_button(self):
        wait = WebDriverWait(self.driver, 10)

        self.driver.find_element(*MainPageLocators.IMAGES_BUTTON).click()
        wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.until(EC.title_contains("Яндекс.Картинки"))


class SearchResultPage(BasePage):

    def is_result_correct(self, check_url="https://tensor.ru/"):
        search_results = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_elements(*SreachResultPageLocators.SEARCH_RESULTS))

        for search_result in search_results:
            ads = len(search_result.find_elements(
                *SreachResultPageLocators.ADS_LABEL)) != 0
            if ads:
                continue
            else:
                link = search_result.find_element_by_tag_name("a")
                return (check_url == link.get_attribute("href"))

        return False


class ImagesPage(BasePage):

    def is_url_correct(self):
        return WebDriverWait(self.driver, 2).until(EC.url_matches("https://yandex.ru/images/"))

    def press_first_image(self):
        images = WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element_by_id("main"))

        WebDriverWait(images, 10).until(
            EC.element_to_be_clickable((By.TAG_NAME, "a"))).click()

    def is_image_present(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_elements(*ImagesPageLocators.IMAGE_BOX)) != 0

    def save_first_image_present(self):
        image = self.driver.find_element(*ImagesPageLocators.IMAGE_BOX)

        try:
            WebDriverWait(self.driver, 1).until(EC.staleness_of(image))
            image = self.driver.find_element(*ImagesPageLocators.IMAGE_BOX)
        except:
            pass

        self.first_image_src = image.get_attribute("src")

    def is_next_button_present(self):
        return len(WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_elements(*ImagesPageLocators.IB_NEXT_BUTTON))) != 0

    def is_prev_button_present(self):
        return len(WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_elements(*ImagesPageLocators.IB_PREV_BUTTON))) != 0

    def press_next_button(self):
        next_button = self.driver.find_element(
            *ImagesPageLocators.IB_NEXT_BUTTON)
        self.driver.execute_script("arguments[0].click();", next_button)

    def press_prev_button(self):
        prev_button = self.driver.find_element(
            *ImagesPageLocators.IB_PREV_BUTTON)
        self.driver.execute_script("arguments[0].click();", prev_button)

    def is_the_same_image(self):
        image = self.driver.find_element(*ImagesPageLocators.IMAGE_BOX)

        try:
            WebDriverWait(self.driver, 1).until(EC.staleness_of(image))
            image = self.driver.find_element(*ImagesPageLocators.IMAGE_BOX)
        except:
            pass

        current_image_src = image.get_attribute("src")
        return current_image_src == self.first_image_src
