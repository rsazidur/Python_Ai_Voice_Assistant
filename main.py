import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")
# print(voices)
engine.setProperty("Voice", voices[0].id)
# print(voices[0].id)

author = "Nero"


def speck(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speck(f"Good morning {author}")
    elif 12 <= hour < 18:
        speck(f"Good afternoon {author}")
    else:
        speck(f"Good evening {author}")

    speck("Tell me how can i help you?")


if __name__ == "__main__":
    # speck(f"Welcome {author}, I am Dante.")
    wish_me()
