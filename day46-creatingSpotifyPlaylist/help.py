import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import os

CLIENT_ID_SPOTIFY = os.environ.get("SpotifyClientID")
CLIENT_SECRET_SPOTIFY = os.environ.get("SpotifyClientSecret")
REDIRECT_URI = "http://example.com"

date = input("Which year do you want to travel to? Type the date in this format sYYYY-MM-DD: ")
year = date.split("-")[0]

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
response.raise_for_status()

contents = BeautifulSoup(response.text, "html.parser")

songs = [content.text.strip() for content in contents.select("li>h3#title-of-a-story.c-title")]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID_SPOTIFY, 
    client_secret=CLIENT_SECRET_SPOTIFY, 
    redirect_uri=REDIRECT_URI, 
    scope="playlist-modify-private user-library-read user-top-read",
    username="Maksim")
)

user_id = sp.current_user()["id"]

song_uris = []


for song in songs:
    song_json = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        print(song_json['tracks']['items'][0]["uri"])
        song_uris.append(str(song_json['tracks']['items'][0]["uri"]))
    except:
        print(f"Song '{song}' is not in Spotify. Skipped")


print(song_uris)

playlist_id = sp.user_playlist_create(user_id, name=date, public=False)

sp.playlist_add_items(playlist_id=playlist_id["id"], items=song_uris)

print("Added")