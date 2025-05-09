import speech_recognition as sr
import pyttsx3
from googlesearch import search

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening for your search query...")
        speak("What would you like to search?")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"🔍 You said: {query}")
        return query
    except sr.UnknownValueError:
        print("❌ Sorry, I could not understand your speech.")
        speak("Sorry, I could not understand your speech.")
        return None
    except sr.RequestError:
        print("❌ Could not request results from Google Speech Recognition.")
        return None

def search_google(query):
    print(f"🌐 Searching Google for: {query}")
    speak(f"Searching Google for {query}")
    results = list(search(query, num_results=5))
    for i, result in enumerate(results, 1):
        print(f"{i}. {result}")
    speak("Here are the top results.")
    return results

if __name__ == "__main__":
    query = listen()
    if query:
        search_google(query)
