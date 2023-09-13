from selenium import webdriver
import time
 
chrome_driver_path = CHROME_DRIVER_PATH
 
driver = webdriver.Chrome(executable_path=chrome_driver_path)
web_url = 'http://orteil.dashnet.org/experiments/cookie/'
driver.get(web_url)
 
cookie = driver.find_element_by_id('cookie')
 
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]
 
timeout = time.time() + 10
five_min = time.time() + (60*5)
 
while True:
    cookie.click()
    if time.time() > timeout:
        all_prices = driver.find_elements_by_css_selector('#store b')
        item_prices = []
        for price in all_prices:
            item_price = price.text
            if item_price != '':
                cost = int(item_price.split('-')[1].strip().replace(',', ''))
                item_prices.append(cost)
        cookie_upgrades = {item_prices[n]: item_ids[n] for n in range(len(item_prices))}
        money_element = driver.find_element_by_id('money').text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        money = int(money_element)
        if money > 2000:
            while True:
                money_element = driver.find_element_by_id('money').text
                if "," in money_element:
                    money_element = money_element.replace(",", "")
                money = int(money_element)
                affordable_upgrades = {}
                for cost, item in cookie_upgrades.items():
                    if money >= cost:
                        affordable_upgrades[cost] = item
                try:
                    if len(affordable_upgrades) > 0:
                        best_upgrade = max(affordable_upgrades)
                        purchase = affordable_upgrades[best_upgrade]
                        driver.find_element_by_id(purchase).click()
                    else:
                        break
                except:
                    break
        else:
            pass
 
        timeout = time.time() + 10
 
    if time.time() > five_min:
        cookies_per_second = driver.find_element_by_id('cps').text
        print(cookies_per_second)
        break
 
driver.quit()