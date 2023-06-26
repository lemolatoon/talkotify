import speech_recognition as sr # type: ignore
recognizer = sr.Recognizer()

def get_audio_from_mic():
    with sr.Microphone(sample_rate=16000) as source:
        print("なにか話してください")
        audio = recognizer.listen(source)
        print("考え中...")
        return audio