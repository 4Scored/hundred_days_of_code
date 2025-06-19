import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=os.environ.get("SPOTIFY_BILLBOARD_REDIRECT_URI"),
        client_id=os.environ.get("SPOTIFY_BILLBOARD_ID"),
        client_secret=os.environ.get("SPOTIFY_BILLBOARD_CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt",
        username=os.environ.get("SPOTIFY_USERNAME"), 
    )
)
user_id = sp.current_user()["id"]

date_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL= f"https://www.billboard.com/charts/hot-100/{date_input}"
header = {
    "User-Agent": "Your-User-Agent-Header"
}

billboard_response = requests.get(url=URL, headers=header)
billboard_response.raise_for_status()
billboard_html = billboard_response.text

soup = BeautifulSoup(billboard_html, "html.parser")
song_names = soup.select("li.o-chart-results-list__item h3#title-of-a-story")
song_names = [song.getText().strip() for song in song_names]

song_uris = []
year = date_input.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} DNE on Spotify")

playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)