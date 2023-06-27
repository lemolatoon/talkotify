import spotipy
import spotipy.util as util
from talkotify.env import SPOTIFY_API_CLIENT_ID, SPOTIFY_API_SECRET, SPOTIFY_USERNAME

SPOTIPY_REDIRECT_URI = "https://github.com/lemolatoon/talkotify"
scope = 'user-read-playback-state,playlist-read-private,user-modify-playback-state,playlist-modify-public'

token = util.prompt_for_user_token(SPOTIFY_USERNAME, scope)

client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(SPOTIFY_API_CLIENT_ID, SPOTIFY_API_SECRET)
client = spotipy.Spotify(client_credentials_manager=client_credentials_manager, auth=token)

def get_device_id() -> str:
    print("get devices")
    devices = client.devices()
    return devices["devices"][0]["id"]

def play(device_id: str, uri: str):
    client.start_playback(device_id, uris=[uri])

def search(query: str):
    result = client.search(query, market="JP")

    items = result["tracks"]["items"]

    def uri(item):
        id = item["id"]
        return f"spotify:track:{id}"
    uris = list(map(uri, items))
    return uris