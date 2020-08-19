import unittest
import page
from selenium import webdriver


class YandexTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://yandex.ru/")

    def test_searchbar(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_searchbar_exist()
        main_page.set_search_item()
        assert main_page.is_popup_menu_exist()
        main_page.press_enter()

        search_results_page = page.SearchResultPage(self.driver)
        assert search_results_page.is_result_correct()

    def test_images_page(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_images_button_present()
        main_page.press_images_button()

        images_page = page.ImagesPage(self.driver)
        assert images_page.is_url_correct()
        images_page.press_first_image()
        assert images_page.is_image_present()
        images_page.save_first_image_present()
        assert images_page.is_next_button_present()
        images_page.press_next_button()
        assert not images_page.is_the_same_image()
        assert images_page.is_prev_button_present()
        images_page.press_prev_button()
        assert images_page.is_the_same_image()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
