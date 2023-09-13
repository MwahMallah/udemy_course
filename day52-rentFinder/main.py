#https://docs.google.com/forms/d/e/1FAIpQLSfY1cuog_jkaNuzJ-6PEZvqbI152A50USASKOGAQXaVt0z7vw/viewform?usp=sf_link

from rentPrices import RentPrices
from formFiller import FormFiller

info = RentPrices().get_info()
FormFiller().send_answers(info)
