import os
import sys
import pyttsx3
import asyncio
import datetime
import speech_recognition as sr
from googletrans import Translator
import webbrowser
import time  # Import time module

# Speak function to say text aloud
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Set voice to female
    engine.setProperty('rate', 150)  # Set speech speed
    engine.say(text)
    engine.runAndWait()

# Initialize recognizer and translator
r = sr.Recognizer()
t = Translator()

# Asynchronous translation function
async def translate_text(command):
    translated = await t.translate(command, dest='en')
    return translated.text

# Function to run the main loop
async def run_assistant():
    speak("हैलो मोहित सर आप कैसे हैं उम्मीद करता हूं आप अच्छे होंगे आपका दिन अच्छा गुजरा होगा बतायें मैं आपके लिए क्या कर सकता हूं")
    while True:
        with sr.Microphone() as source:
            speak("आपकी आवाज सुनी जा रही है")
            print("Listening your voice....")
            audio = r.listen(source)
            try:
                # Recognize the speech
                command = r.recognize_google(audio, language='hi-IN')
                speak("आपने कहा: " + command)

                # Translate the command to English asynchronously
                translated_text = await translate_text(command)

                # Check the translated text for specific commands
                if "youtube" in translated_text.lower():
                    speak("youtube खोला जा रहा है")
                    print("Opening Youtube.com....")
                    webbrowser.open("https://www.youtube.com/")  # Ensure URL is correct
                    time.sleep(1)  # Wait for 2 seconds to allow browser to open

                elif "wikipedia" in translated_text.lower():
                    speak("विकिपीडिया खोला जा रहा है")
                    print("Opening Wikipedia....")
                    webbrowser.open("https://wikipedia.org/")
                    time.sleep(1)
                    # Add a short delay
                elif "tera chehra song" in translated_text.lower():
                    speak("youtube में खोला जा रहा है")
                    print("Opening song....")
                    webbrowser.open("https://www.youtube.com/watch?v=LOmC1dlZ2BE&list=RDLOmC1dlZ2BE&start_radio=1")
                    time.sleep(1)  # Add a short delay
          
                elif "google" in translated_text.lower():
                    speak("google खोला जा रहा है")
                    print("Opening Google.com....")
                    speak("मैंने गूगल खोल दिया है उसपे काम करो जाके")
                    webbrowser.open("https://google.com/")
                    time.sleep(2)  # Add a short delay



                elif "whatsapp" in translated_text.lower():
                    speak("whatsapp खोला जा रहा है कृपया प्रतीक्षा करें")
                    print("Opening web Whatsapp.com....")
                    webbrowser.open("https://web.whatsapp.com/")
                    time.sleep(0)
                    speak("whatsapp खोला जा चुका है")

                elif "typing master" in translated_text.lower():
                    speak("typing master खोला जा रहा है कृपया प्रतीक्षा करें")
                    print("Opening typing master...")
                    typing = "C:\\Users\\ashut\\OneDrive\\Desktop\\Typing Master 11.lnk"
                    os.startfile(typing)
                    speak("typing master खोला जा चुका है")

                elif "snapchat" in translated_text.lower():
                    speak("स्नैप खोला जा रहा है कृपया प्रतीक्षा करें")
                    print("Opening Snapchat..")
                    snap = "C:\\Users\\ashut\\OneDrive\\Desktop\\Snapchat.lnk"
                    os.startfile(snap)
                    speak(" स्नैप खोला जा चुका है")

                elif "python" in translated_text.lower():
                    speak("thonny खोला जा रहा है कृपया प्रतीक्षा करें ")
                    print("opening python..")
                    python = "C:\\Users\\Public\\Desktop\\Thonny.lnk"
                    os.startfile(python)

                elif "chrome" in translated_text.lower():
                    speak("google Chrome खोला जा रहा है कृपया प्रतीक्षा करें ")
                    print("opening chrome..")
                    chrome = "C:\\Users\\ashut\\OneDrive\\Desktop\\chrome - Shortcut.lnk"
                    os.startfile(chrome)

                elif "time" in translated_text.lower():
                    speak("अभी समय देखा जा रहा है")
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(strTime)
                    speak(f" अभी समय हो रहा है  {strTime}")

                elif "visual studio" in translated_text.lower():
                    speak("Visual Studio खोला जा रहा है कृपया प्रतीक्षा करें ")
                    print("Opening Vscode.....")
                    vscode = "C:\\Users\\ashut\\OneDrive\\Desktop\\Visual Studio Code.lnk"
                    os.startfile(vscode)


                elif "close" in translated_text.lower():
                    speak("प्रोग्राम बंद किया जा रहा है")
                    print("Stopping Program....")
                    speak("अब मैं बंद हूं")
                    sys.exit()
 

            except sr.UnknownValueError:
                speak("में आपकी आवाज समझ नहीं पा रहा हूं। कृपया फिर से बोलिए")
                print("Unrecognized Voice. Say that again please.")

if __name__ == "__main__":
    # Run the assistant using an asyncio event loop
    asyncio.run(run_assistant())
