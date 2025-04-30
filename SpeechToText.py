import time
import speech_recognition as sr
from speech_recognition.recognizers.google_cloud import recognize
import assemblyai
recognizer = sr.Recognizer()
# use lib in Python
with sr.Microphone() as source:
    print("Say Something with gg cloud token API...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    # recognizer.azure_cached_access_token


try:
    text = recognizer.recognize_google(audio, language="vi-VN")
    print("You have say: ", text)
    # text = recognizer.recognize_google(audio, language="vi-VN")
except sr.UnknownValueError:
    print("Can recognize your voice")
except sr.RequestError:
    print("have fault when call API tokens")

