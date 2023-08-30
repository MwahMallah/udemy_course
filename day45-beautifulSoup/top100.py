from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

site_content = BeautifulSoup(response.text, "html.parser")

movies = [movie.text for movie in site_content.select("h3.listicleItem_listicle-item__title__hW_Kn")]

with open("movie_list.txt", "a+") as file:
    for movie in movies[::-1]:
        file.write(f"{movie}\n")