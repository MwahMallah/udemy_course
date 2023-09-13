from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)

browser.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")

# link = browser.find_element(By.LINK_TEXT, "deposed by a military coup d'état")
# link.click()

first_name = browser.find_element(By.NAME, "fName")
last_name = browser.find_element(By.NAME, "lName")
email = browser.find_element(By.NAME, "email")
sign_up = browser.find_element(By.XPATH, "/html/body/form/button")

first_name.send_keys("Maksim")
last_name.send_keys("Dubrovin")
email.send_keys("maximus27rus@gmail.com")
sign_up.click()

# browser.quit()