from selenium import webdriver
from selenium.webdriver.common.by import By 
from typing import List, Tuple

class FormFiller():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

    def send_answers(self, infos: List[Tuple]):
        for info in infos:
            self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfY1cuog_jkaNuzJ-6PEZvqbI152A50USASKOGAQXaVt0z7vw/viewform")

            self.driver.find_element(By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input').send_keys(info[0])
            self.driver.find_element(By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input').send_keys(info[1])
            self.driver.find_element(By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input').send_keys(info[2])

            self.driver.find_element(By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div > span').click()
