from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class NewLoginTest(StaticLiveServerTestCase):
    def setUp(self):
        # opts = Options()
        # opts.add_argument("--headless")
        # self.browser = webdriver.Firefox(options=opts)
        self.browser = webdriver.Firefox()
        
    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_create_account(self):
        #pitur types the url of the new hip website
        self.browser.get(self.live_server_url+"login/")

        #He sees that login is in the title
        self.assertIn("Create Account",self.browser.title)
        
        # He see a Login title 
        header_text = self.browser.find_element(By.ID,"head-text").text
        self.assertIn("Create Account",header_text)

        # He types out his name, email and his password to create and account
        name = self.browser.find_element(By.ID,"id_new_name")
        name.send_keys("Pitre")
        email = self.browser.find_element(By.ID,"id_new_email")
        email.send_keys("pitre@pitur.com")
        password = self.browser.find_element(By.ID,"id_new_password")
        password.send_keys("PITARA")

        # He then presses Enter
        submit_button = self.browser.find_element(By.ID,"id_submit")
        submit_button.click()

        # He then sees he is signed in 
        username = self.browser.find_element(By.ID,"id_username")
        self.assertEqual("Pitre",username.text)

        # He also sees the log out button
        logout = self.browser.find_element(By.ID,"id_logout_button")
        
        


