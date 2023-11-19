from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
SIMILAR_ACCOUNT = "cats_of_instagram"
USERNAME = "USERNAME34"
PASSWORD = "YOUR_PASSWORD"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    # by = By.XPATH, value = '//*[@id="loginForm"]/div/div[1]/div/label/input'
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        name = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        name.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        button = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        button.click()

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
