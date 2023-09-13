from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.get("https://orteil.dashnet.org/experiments/cookie/")


document.querySelector("#buyAlchemy\\ lab")

def main():
    cookie = init_cookie()
    timeout = time.time() + 15 * 60
    upgrades_time = time.time() + 5
    while True:
        if time.time() > timeout:
            break
        if time.time() > upgrades_time:
            upgrades_time = time.time() + 5
            upgrade = get_upgrade()
            upgrade.click()
        
        cookie.click()

    

def init_cookie():
    return browser.find_element(By.CSS_SELECTOR, "#middle #cookie")

def get_upgrade():
    balance = get_balance()
    if balance >= 123456789:
        return browser.find_element(By.ID, "buyTime")
    elif balance >= 1000000:
        return browser.find_element(By.ID, "buyPortal")
    elif balance >= 50000:
        return browser.find_element(By.ID, "buyAlchemy")
    elif balance >= 7000:
        return browser.find_element(By.ID, "buyShipment")
    elif balance >= 2000:
        return browser.find_element(By.ID, "buyMine")
    elif balance >= 500:
        return browser.find_element(By.ID, "buyFactory")
    elif balance >= 100:
        return browser.find_element(By.ID, "buyGrandma")
    elif balance >= 15:
        return browser.find_element(By.ID, "buyCursor")

def get_balance():
    return int(browser.find_element(By.ID, "money").text.replace(",", "").strip())


if __name__ == "__main__":
    main()