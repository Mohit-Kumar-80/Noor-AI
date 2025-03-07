#apikey = "AIzaSyDpWikHPQGXTAl0iGdeldxAUf_YquPshmM"
import speech_recognition as sr
from deep_translator import GoogleTranslator
import google.generativeai as ai
import os
from gtts import gTTS
import  pyttsx3


r = sr.Recognizer()
def bol(tts):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Set voice to female
    engine.setProperty('rate', 150)  # Set speech speed
    engine.say(tts)
    engine.runAndWait()


# API key configure karein
api_key = "AIzaSyDpWikHPQGXTAl0iGdeldxAUf_YquPshmM"
ai.configure(api_key=api_key)

# Model initialize karein
model = ai.GenerativeModel("gemini-1.5-flash")


engl = input("Enter to search :")


hindi_text = GoogleTranslator(source='en', target='hi').translate(engl)

# Hindi me prompt
prompt = hindi_text

# Model ka response lein
response = model.generate_content(prompt)



# Output text store karein
hindi_text = response.text
print(hindi_text)  # Console me print karein

# Text ko Hindi me speech me convert karein
#tts = gTTS(text=hindi_text, lang='hi')

# MP3 file save karein aur play karein

bol(response.text)
