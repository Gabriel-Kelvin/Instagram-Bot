from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time

USERNAME = "editing_overloaded"
PASSWORD = "7708850024"


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        user_name = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_name.send_keys(USERNAME)
        pass_word = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        pass_word.send_keys(PASSWORD)
        log_in = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button/div')
        log_in.click()
        time.sleep(5)
        not_now = self.driver.find_element(By.XPATH, '// button[contains(text(), "Not Now")]')
        not_now.click()

    def find_followers(self):
        time.sleep(3)
        self.driver.get("https://www.instagram.com/luffyzofficial/")
        time.sleep(5)
        followers = self.driver.find_element(By.XPATH, '// span[contains(text(), "50.7K")]')
        followers.click()
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers)
            time.sleep(2)

    def follow(self):
        time.sleep(3)
        follow_button = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')
        for button in follow_button:
            try:
                time.sleep(5)
                button.click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()