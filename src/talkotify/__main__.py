from io import BytesIO

import openai
from talkotify.microphone import get_audio_from_mic
from .env import OPENAI_API_KEY, init_env, checked_get
from .spotify import get_device_id, play, search


openai.api_key = OPENAI_API_KEY
def voice_to_text() -> str:
    audio = get_audio_from_mic()
    audio_data = BytesIO(audio.get_wav_data())
    audio_data.name = 'from_mic.wav'
    transcript = openai.Audio.transcribe('whisper-1', audio_data, language="ja")
    return transcript['text']

def run():
    init_env()
    # text = voice_to_text()
    # print(text)
    device_id = get_device_id()
    uris = search("YOASOBI")
    play(device_id, uris[0])
    print("hoy!")

if __name__ == "__main__":
    run()