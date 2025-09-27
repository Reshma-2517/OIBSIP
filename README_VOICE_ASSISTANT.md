# OIBSIP_VoiceAssistant_Task

##  Project Title: Basic Voice Assistant  

###  Objective  
The aim of this project is to develop a simple **Voice Assistant** using Python. The assistant listens to user commands, interprets them, and replies with spoken responses. It can perform everyday tasks like greetings, telling the time/date, and searching the web.  

---

###  Tools & Technologies Used  
- **Python** – Programming language  
- **speech_recognition** – For converting voice input into text  
- **pyttsx3** – For generating speech output  
- **datetime** – For obtaining the current time and date  
- **webbrowser** – For Google searches  

---

###  Steps to perform
1. **Environment Setup**  
   - Install required libraries:  
     ```bash
     pip install SpeechRecognition pyttsx3 pyaudio
     ```

2. **Text-to-Speech Engine**  
   - Initialized `pyttsx3` to convert text responses into spoken words.  

3. **Speech Recognition**  
   - Implemented `speech_recognition` to understand voice commands.  
   - Added error handling for unclear voice input and internet issues.  

4. **Command Processing**  
   - Defined a function to recognize and act on commands like:  
     - `"hello"` → Greets the user  
     - `"time"` → Reads out the current time  
     - `"date"` → Reads out today’s date  
     - `"search <query>"` → Performs a Google search  
     - `"quit"` / `"exit"` → Ends the assistant  

5. **Main Execution Loop**  
   - Runs continuously until the user exits with `"quit"` or `"exit"`.  

---
### Linkedin post link

- https://www.linkedin.com/posts/reshma-sappa17_oasisinfobyte-python-voiceassistant-activity-7377658277691650049-eQbi?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD-MUmQBtrxqvplzumTx7fojAJQ_UfxwUg8

---

###  Sample Code Snippet  

```python
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
