import requests
from bs4 import BeautifulSoup
import smtplib

def send_email(price: float):
    with smtplib.SMTP("smtp.gmail.com", port=587) as mail:
        mail.starttls()
        mail.login(user="maksim0dubrovin0@gmail.com", password="frhkegbnpzjvczul")
        mail.sendmail(from_addr="maksim0dubrovin0@gmail.com", to_addrs="maximus27rus@gmail.com", msg=f"Subject:Item is cheap!!!\n\nprice is only {price}$!!!")


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6"
}

response = requests.get("https://www.amazon.com/Operating-Systems-Three-Easy-Pieces/dp/198508659X/ref=pd_rhf_d_gw_s_pd_sbs_rvi_sccl_1_1/144-5851570-2831543?pd_rd_w=lVk6U&content-id=amzn1.sym.a089f039-4dde-401a-9041-8b534ae99e65&pf_rd_p=a089f039-4dde-401a-9041-8b534ae99e65&pf_rd_r=5N6MY8XQSPY9YF5WMD87&pd_rd_wg=988I3&pd_rd_r=5324e7f8-3ac9-4a82-80b3-783a1f0cfc91&pd_rd_i=198508659X&psc=1", headers=HEADERS)
item_content = BeautifulSoup(response.text, "lxml")

item_price = float(item_content.select("#price")[0].text.split("$")[1])

if item_price < 25.00:
    send_email(item_price)