import speech_recognition as sr # type: ignore
recognizer = sr.Recognizer()
print("".join(list(map(lambda tup: f"{tup[0]}: {tup[1]}\n", enumerate(sr.Microphone.list_microphone_names())))))
index = input("マイクの番号を入力してください: ")
index = int(index) if index.isdigit() else None

def get_audio_from_mic():
    with sr.Microphone(device_index=index, sample_rate=16000) as source:
        print("なにか話してください")
        audio = recognizer.listen(source, timeout=3000)
        print("考え中...")
        return audio