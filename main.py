import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

USER_NAME = "pythondeveloper1989"
PASS = "1611368"

service = Service("C:/Selenium Driver/chromedriver.exe")


class InstaFollower:
    def __init__(self, url):
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(url)
        self.followers_list = []

    def login(self):
        time.sleep(2)
        sign_in = self.driver.find_element(By.XPATH,
                                           '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div['
                                           '1]/section/nav/div[2]/div/div/div[3]/div/span/a[1]')
        sign_in.click()
        user_name = self.driver.find_element(By.NAME, "username")
        user_name.send_keys(USER_NAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASS)
        password.send_keys(Keys.ENTER)
        time.sleep(2)
        not_now = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button')
        not_now.click()

    def find_followers(self):
        time.sleep(2)
        followers = self.driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div['
                                             '1]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(3)
        self.followers_list = self.driver.find_elements(By.CSS_SELECTOR, "li._aaei ._aaes")

    def follow(self):
        for f in self.followers_list:
            f.click()
            time.sleep(1)


insta_follower = InstaFollower("https://www.instagram.com/natgeo/")
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()
