import unittest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager


class LoginCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_user_login(self):
        # driver = self.driver
        self.driver.get("http://localhost:4200/users/auth")
        # login_click = driver.find_element_by_css_selector(".dropdown-toggle")
        # log_in_click = driver.find_element_by_css_selector(".dropdown-item")
        login_field = self.driver.find_element_by_id("username")
        login_field.send_keys("admin@gmail.com")
        password_field = self.driver.find_element_by_id("password")
        password_field.send_keys("admin")
        button_login = self.driver.find_element_by_xpath("//input[@type='submit' and @value='Sign In']")
        button_login.click()

        result = self.driver.find_element_by_css_selector("div.dropdown-menu a.dropdown-item")
        print(result.get_attribute("href"), "ashtashtasht", result.text)

        assert result.get_attribute("href") == "http://localhost:4200/users/auth"

    def ststst(self):
        print('test')
	print('ashtashtasht')


if __name__ == "__main__":
    unittest.main()
