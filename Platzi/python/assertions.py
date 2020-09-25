import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class AssertionsTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C://Users/USER/Desktop/chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.maximize_window
    
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, "q"))
    
    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, "select-language"))

    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")
    
    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")
        
    def test_search_text_field_class_name(self):
        search_field = self.driver.find_elements_by_class_name("input-text required-entry")
    
    def test_search_btn_enable(self):
        search_field = self.driver.find_elements_by_class_name("button search-button")
    
    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(banners))

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_elements_by_css_selector("div.header-minicart span")

    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what): #identificar  donde esta el elemento 
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity = 2)