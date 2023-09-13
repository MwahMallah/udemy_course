import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

MY_GMAIL = os.environ.get("MyGmailAddress")
MY_PASSWORD = os.environ.get("MyGmailPassword")
SEXY_LINE = os.environ.get("MySexyLine")
print(SEXY_LINE)

browser = uc.Chrome()
browser.delete_all_cookies()

browser.get("https://tinder.com/")

sleep(1)
browser.find_element(By.XPATH, '//*[@id="q1388042758"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]').click()

sleep(1)
browser.find_element(By.XPATH, '#container > div > div.nsm7Bb-HzV7m-LgbsSe-MJoBVe').click()


sleep(2)

browser.find_element(By.XPATH, '//*[@id="t-1801918317"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[1]').click()

browser.switch_to.window(browser.window_handles[1])

sleep(2)
enter_gmail = browser.find_element(By.ID, 'identifierId')
enter_gmail.send_keys(MY_GMAIL)
enter_gmail.send_keys(Keys.ENTER)

sleep(3)
password = browser.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys(MY_PASSWORD)
password.send_keys(Keys.ENTER)

sleep(5)
browser.switch_to.window(browser.window_handles[0])
browser.find_element(By.XPATH, '//*[@id="t-1801918317"]/main/div/div/div/div[3]/button[1]/div[2]').click()

sleep(6)
browser.find_element(By.XPATH, '//*[@id="t-1801918317"]/main/div/div/div/div[3]/button[2]/div[2]').click()
sleep(1)

while True:
    try:
        sleep(1) 
        browser.find_element(By.CSS_SELECTOR, '#t-73537241 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw\(--recs-card-width\)--ml > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Iso\(i\).W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-ds-border-gamepad-like-default\) > button').click()
    except Exception:
        # browser.find_element(By.CSS_SELECTOR, "#t256833960 > main > div > div.CenterAlign.M\(a\).Expand.Pos\(r\).Fx\(\$flx1\) > div > div.Pos\(r\).W\(100\%\).Pb\(32px\) > div.My\(12px\).C\(\$c-ds-text-primary\).Mx\(20px\).Bdrs\(4px\).Ov\(h\) > form").send_keys(SEXY_LINE)
        print(Exception)

sleep(100)
