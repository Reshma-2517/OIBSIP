import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

#--- Initialize/setup text-to-speech engine--#
assistant = pyttsx3.init()

#---Speak the given message aloud------#
def speak(message):
    assistant.say(message)
    assistant.runAndWait()

#----Listen through microphone and convert speech to text---#
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak...")
        recognizer.adjust_for_ambient_noise(source)  # handles background noise
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I couldn't catch that.")
        return ""
    except sr.RequestError:
        speak("Network issue. Please check your connection.")
        return ""

#-----Perform actions based on the command---#
def handle_command(command):
    if "hello" in command:
        speak("Hi! How can I help you?")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today is {today}")
    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            url = f"https://www.google.com/search?q={query}"
            speak(f"Here are the results for {query}")
            webbrowser.open(url)
        else:
            speak("What would you like me to search for?")
    elif "quit" in command or "exit" in command:
        speak("Goodbye!")
        return False
    else:
        speak("I don’t know how to do that yet.")
    return True

def main():
    speak("Hello, I am your voice assistant. Say something!")
    running = True
    while running:
        command = listen_command()
        if command:
            running = handle_command(command)

if __name__ == "__main__":
    main()
