from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

MY_GMAIL = os.environ.get("MyGmailAddress")
MY_PASSWORD = os.environ.get("MyGmailPassword")

class InstaFollower:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)

    def login(self):
        self.browser.get('https://www.instagram.com/')
        sleep(1)
        self.browser.find_element(By.CSS_SELECTOR, "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x5yr21d.x19onx9a > div > button._a9--._a9_1").click()
        sleep(1)
        self.browser.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input').send_keys(MY_GMAIL)
        self.browser.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(2) > div > label > input').send_keys(MY_PASSWORD)
        self.browser.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3)').click()
        sleep(4)

    def find_followers(self, simillar_account):   
        self.browser.get(f'https://www.instagram.com/{simillar_account}/')
        sleep(4)
        self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a').click()

        #body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(1)
        inside_popup = self.browser.find_element(By.CSS_SELECTOR, '.x9f619 ._aano')
        
        for _ in range(10):
            sleep(1)
            inside_popup.send_keys(Keys.END)

        