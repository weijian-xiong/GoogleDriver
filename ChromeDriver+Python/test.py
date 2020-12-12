import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ChromeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn("java", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("java")
        elem.send_keys(Keys.RETURN)
        assert "https://www.google.com/search?q=java&oq=java&aqs=chrome.0.69i59l2j35i39j69i59j0i433l2j46i433j0i131i433.530j0j15&sourceid=chrome&ie=UTF-8" == driver.current_url
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()
