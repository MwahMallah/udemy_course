from tkinter import *
from tkcalendar import Calendar
from settings import *
from typing import List
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy import SpotifyOAuth

sp = None
user_id = None
date = None

def add_playlist():
    global date
    date = calendar.get_date()
    songs = get_songs_from(date)
    init_spotify()
    songs_uris = get_songs_uris(songs)
    create_playlist(date, songs_uris)
    print("Successfully build playlist")

def get_songs_from(date: str) -> List[str]:
    response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}")
    response.raise_for_status()
    site_content = BeautifulSoup(response.text, "html.parser")
    return [song_content.text.strip() for song_content in site_content.select("li > h3#title-of-a-story")]

def init_spotify():
    global user_id, sp

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID_SPOTIFY, 
    client_secret=CLIENT_SECRET_SPOTIFY, 
    redirect_uri=REDIRECT_URI, 
    scope="playlist-modify-private user-library-read user-top-read",
    username="Maksim")
    )

    user_id = sp.current_user()["id"]
    
def get_songs_uris(songs: List[str]) -> List[str]:
    songs_uris = []
    for song in songs:
        uri_json = sp.search(q=f"track:{song} year:{date.split('-')[0]}", limit=1, type="track")
        try:
            songs_uris.append(uri_json['tracks']['items'][0]["uri"])
        except:
            print(f"Song {song} is not in spotify, skipped")
    return songs_uris
        
def create_playlist(date: str, songs: List[str]):
    playlist = sp.user_playlist_create(user=user_id, name=date, public=False)
    sp.playlist_add_items(playlist_id=playlist["id"], items=songs)


window = Tk()
window.config(padx=50, pady=30, background="#088a5c")

calendar = Calendar(date_pattern='y-mm-dd')
calendar.grid(column=0, row=0)

push_btn = Button(text="Make playlist from this date", font=FONT, command=add_playlist)
push_btn.grid(row=1, column=0, pady=20)

window.mainloop()