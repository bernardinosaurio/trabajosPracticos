import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C://Users/USER/Desktop/chromedriver.exe')
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_search_text_field(self):
            search_field = self.driver.find_element_by_id("search_query_top")

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("search_query")

    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name("search_query")

    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name("btn")

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("htmlcontent-home")
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(2, len(banners))

    def test_promo(self):
        promo = self.driver.find_element_by_xpath('//*[@id="homeslider"]/li[4]/a/img')

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.shopping_cart a")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'search-test-report'))