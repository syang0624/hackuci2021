#welcome message
from playsound import playsound
import speech_recognition as sr
playsound('welcome.wav')

r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    r.adjust_for_ambient_noise(source)
    playsound('twosec.wav')
    playsound('ring.wav')
    audio = r.listen(source)
username = r.recognize_google(audio)
@syang0624
