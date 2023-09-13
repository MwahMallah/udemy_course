from selenium import webdriver
from selenium.webdriver.common.by import By 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Operating-Systems-Three-Easy-Pieces/dp/198508659X/ref=pd_rhf_d_gw_s_pd_sbs_rvi_sccl_1_1/144-5851570-2831543?pd_rd_w=lVk6U&content-id=amzn1.sym.a089f039-4dde-401a-9041-8b534ae99e65&pf_rd_p=a089f039-4dde-401a-9041-8b534ae99e65&pf_rd_r=5N6MY8XQSPY9YF5WMD87&pd_rd_wg=988I3&pd_rd_r=5324e7f8-3ac9-4a82-80b3-783a1f0cfc91&pd_rd_i=198508659X&psc=1")
driver.implicitly_wait(20)

price_dollar = driver.find_element(By.CSS_SELECTOR, value=".a-size-medium.a-color-price.header-price.a-text-normal")
print(price_dollar.text)

driver.close(s)
driver.quit()