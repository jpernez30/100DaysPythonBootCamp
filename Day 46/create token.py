import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID ="ab95230911344f80a8afdeb4a5f1927d"
CLIENT_SECRET ="7868c0f24c8142bbba554f1547ffd149"

scope ='playlist-modify-private'
username='12146547275'
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
print(user_id)
