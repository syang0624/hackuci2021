#choosing a pet
from playsound import playsound
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    r.adjust_for_ambient_noise(source)
    playsound('petchoose.wav')
    playsound('ring.wav')
    audio = r.listen(source)
pet = r.recognize_google(audio).lower()

#if this can be button input on front end that would be great
