from bs4 import BeautifulSoup
import requests

class RentPrices():
    def __init__(self) -> None:
        response = requests.get("https://reality.idnes.cz/s/pronajem/byty/do-25000-za-mesic/praha/?s-qc%5BsubtypeFlat%5D%5B0%5D=1k&s-qc%5BsubtypeFlat%5D%5B1%5D=11&s-qc%5BsubtypeFlat%5D%5B2%5D=2k")
        response.raise_for_status()

        self.content = BeautifulSoup(response.text, "html.parser")

    def get_info(self):
        links = self.content.select(".c-products__inner > .c-products__link")
        prices = self.content.select(".c-products__inner .c-products__price")
        locations = self.content.select(".c-products__inner .c-products__info")

        return [(location.getText().strip(), price.getText().strip(), link["href"]) for link, price, location in zip(links, prices, locations)]
