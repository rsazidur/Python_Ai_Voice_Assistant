import pyttsx3

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")
# print(voices)
engine.setProperty("Voice", voices[0].id)
# print(voices[0].id)

author = "Nero"


def speck(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == "__main__":
    speck(f"Welcome {author}, I am Dante and supto is a motherfucker. he wants to fuck girls but cant")
