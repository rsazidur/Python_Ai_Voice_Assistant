import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

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

def take_command():
    """
    take microphone input from the user and return string
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5   # seconds of non-speaking audio before a phrase is considered complete.
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said... {query} \n")
    except Exception as e:
        print(f"Sorry {author}, say that again...")
        return "None"
    return query


if __name__ == "__main__":
    # speck(f"Welcome {author}, I am Dante.")
    wish_me()
    # take_command()
    if 1:
        query = take_command().lower()
        if "wikipedia" and "who" in query:
            speck("Searching Wikipedia...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speck("According to Wikipedia")
            print(results)
            speck(results)



