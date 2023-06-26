from .env import init_env, checked_get

init_env()
OPENAI_API_KEY: str = checked_get("OPENAI_API_KEY")

def voice_to_text():
    audio = get_audio_from_mic()
    audio_data = BytesIO(audio.get_wav_data())
    audio_data.name = 'from_mic.wav'
    transcript = openai.Audio.transcribe('whisper-1', audio_data)
    return transcript['text']

def run():
    init_env()
    print("hoy!")

if __name__ == "__main__":
    run()