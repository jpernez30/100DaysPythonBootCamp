import json
from pprint import pprint

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID ="in sticky notes"
CLIENT_SECRET ="in sticky notes"

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
scope ='playlist-modify-private'
username='in sticky notes'
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://example.com",
        username="Jeff Pernez",
        show_dialog=True,
        cache_path="token.txt",
    )
)

user_id = sp.current_user()["id"]


date = "1998-08-26"
URL = "https://www.billboard.com/charts/hot-100/"+date+"/"
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
scrappedHtml=soup.find_all(name='h3',class_ = 'c-title')
titles=[ item.getText().strip() for item in scrappedHtml]

song_uris = []
year = date.split("-")[0]
for song in range(0,10):
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
