import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import news_fetcher
import together_ai

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Danny:", text)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Danny...")

    while True:
        with sr.Microphone() as source:
            print("🎙️ Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print("You said:", command)

            if "danny" in command:
                speak("Hi sir, how may I help you?")

            elif "open google" in command:
                speak("Opening Google")
                webbrowser.open("https://www.google.com")

            elif "open whatsapp" in command:
                speak("Opening WhatsApp Web")
                webbrowser.open("https://web.whatsapp.com")

            elif "open linkedin" in command:
                speak("Opening LinkedIn")
                webbrowser.open("https://www.linkedin.com")

            elif "open youtube" in command:
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")

        

            elif "play music" in command:
                speak("Playing a random song for you.")
                musicLibrary.play_random_song()

            elif "get news" in command or "tell me the news" in command:
                speak("Fetching the latest headlines.")
                news = news_fetcher.get_top_news()
                for item in news:
                    print(item)
                    speak(item.split(" - ")[0])

            elif "ask together" in command:
                speak("What would you like to ask Together AI?")
                with sr.Microphone() as source:
                    audio = recognizer.listen(source)
                try:
                    question = recognizer.recognize_google(audio)
                    speak("Thinking...")
                    response = together_ai.ask_together(question)
                    print("Together AI:", response)
                    speak(response)
                except Exception as e:
                    speak("Sorry, there was a problem talking to Together AI.")

            elif "exit" in command or "shutdown" in command:
                speak("Shutting down. Goodbye.")
                break

        except sr.UnknownValueError:
            print("❌ Could not understand audio.")
        except sr.RequestError as e:
            print(f"⚠️ API error: {e}")
