from typing import List
import spotipy
import spotipy.util as util
from talkotify.env import SPOTIPY_API_CLIENT_ID, SPOTIPY_API_SECRET, SPOTIPY_USERNAME

SPOTIPY_REDIRECT_URI = "https://github.com/lemolatoon/talkotify"
scope = 'user-read-playback-state,playlist-read-private,user-modify-playback-state,playlist-modify-public'

token = util.prompt_for_user_token(SPOTIPY_USERNAME, scope)

client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(SPOTIPY_API_CLIENT_ID, SPOTIPY_API_SECRET)
client = spotipy.Spotify(client_credentials_manager=client_credentials_manager, auth=token)

cached = None
def get_device_id() -> str:
    if cached is not None:
        return cached
    print("get devices")
    devices = client.devices()
    for device in devices["devices"]:
        if device["name"] == "raspotify (raspberrypi)":
            cached = device["id"]
            return device["id"]
    return devices["devices"][0]["id"]

def play(device_id: str, uri: str):
    client.start_playback(device_id, uris=[uri])

def get_available_genres():
    return client.recommendation_genre_seeds()

def search(query: str):
    result = client.search(query, market="JP")

    items = result["tracks"]["items"]

    def uri(item):
        id = item["id"]
        return f"spotify:track:{id}"
    uris = list(map(uri, items))
    return uris

def search_by_genres(genres: str):
    return search(f"genre:{genres}")

functions = [
    {
        "name": "get_available_genres",
        "description": "Retrieve a list of available genres seed parameter values",
        "parameters": {
            "type": "object",
            "properties": {
            },
            "required": []
        }
    },
    {
        "name": "search_by_genres",
        "description": "search song by genres using spotify API",
        "parameters": {
            "type": "object",
            "properties": {
                "genres": {
                    "type": "string",
                    "description": "comma separated genres, which is array of genres. genres must be included in return list of `get_available_genres`. You should specify multiple genres."
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "search_by_name",
        "description": "search song by name using spotify API",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "name of song"
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "play_song",
        "description": "play song by id got by `search songs`",
        "parameters": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "description": "id of the song. The base-62 identifier found at the end of the Spotify URI (see above) for an artist, track, album, playlist, etc. Unlike a Spotify URI, a Spotify ID does not clearly identify the type of resource; that information is provided elsewhere in the call. This argument must start `spotify:`"
                }
            },
            "required": ["id"]
        }
    }
]