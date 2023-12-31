import os
from dotenv import load_dotenv
from pathlib import Path


def init_env() -> None:
    load_dotenv(verbose=True)
    
    dir_path = Path(os.path.dirname(__file__)).parent.parent
    dotenv_path = os.path.join(dir_path, '.env')
    load_dotenv(dotenv_path)



def checked_get(key: str) -> str:
    var = os.environ.get(key)
    if var is None:
        import sys
        print(f"{key} is None", file=sys.stderr)
        sys.exit(1)
    return var

init_env()
OPENAI_API_KEY: str = checked_get("OPENAI_API_KEY")
SPOTIPY_API_CLIENT_ID: str = checked_get("SPOTIPY_CLIENT_ID")
SPOTIPY_API_SECRET: str = checked_get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_USERNAME: str = checked_get("SPOTIPY_USERNAME")
GOOGLE_SEARCH_API_KEY: str = checked_get("GOOGLE_SEARCH_API_KEY")