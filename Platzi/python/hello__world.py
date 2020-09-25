import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver 

class HelloWorld(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'C://Users/USER/Desktop/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(cls):
        driver = self.driver
        driver = cls.driver
        driver.get('https://www.platzi.com')

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes',report_name='hello-world-report'))