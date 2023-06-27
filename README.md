# talkotify

## how to run
1. install rye
2. install libralies
   ```bash
   rye sync
   ```
4. setup env vars
   
   .env
   ```
   OPENAI_API_KEY=sk-****
   SPOTIPY_CLIENT_ID=***
   SPOTIPY_CLIENT_SECRET=***
   SPOTIPY_USERNAME=***
   SPOTIPY_REDIRECT_URL=https://github.com/lemolatoon/talkotify
   ```
3. run
   ```bash
   cd src && rye run python3 -m talkotify
   ```
