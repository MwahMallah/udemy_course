from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

browser_settings = webdriver.ChromeOptions()
browser_settings.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=browser_settings)
browser.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sign_in = browser.find_element(By.CSS_SELECTOR, "body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-md.btn-secondary-emphasis")

sign_in.click()
sleep(1)

mail = browser.find_element(By.CSS_SELECTOR, "#username")
mail.send_keys("maximus27rus@gmail.com")

password = browser.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("25061977q")

push_button = browser.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button")
push_button.click()

sleep(7)

location = browser.find_element(By.XPATH, '//*[@id="jobs-search-box-location-id-ember102"]')
location.clear()
location.send_keys("Brno")
location.send_keys(Keys.ENTER)


application = browser.find_element(By.CSS_SELECTOR, ".search-reusables__filter-binary-toggle > button")
application.click()

