import random
import speech_recognition as sr
from playsound import playsound

study = ['productive', 'school', 'grades', 'pressured', 'university', 'work', 'assignment', 'deadline', 'school', 'pencil', 'laptop']
meditation = ['rest', 'calm', 'tired', 'anxious', 'soothing', 'burnout', 'stressed', 'headache', 'zen', 'recenter', 'recalibrate']
jasons = ['S1B.wav','S2B.wav','S3B.wav','S4B.wav','S5B.wav']
jasonm = ['M1B.wav','M2B.wav','M3B.wav','M4B.wav','M5B.wav']
olivias = ['S1G.wav','S2G.wav','S3G.wav','S4G.wav','S5G.wav']
oliviam = ['M1G.wav','M2G.wav','M3G.wav','M4G.wav','M5G.wav']

def audio_input():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print('Please speak two seconds after you hear the ring.')
        playsound('ring.wav')
        audio = r.listen(source)
    inputaudio = r.recognize_google(audio)
    lst = [inputaudio]
    return lst

def convert(lst): 
    return (lst[0].lower().split())

def matchWord(lst):
    check = any(item in lst for item in study)
    if check == False:
        check = any(item in lst for item in meditation)
        if check == False:
            print("We didn't catch you. Pleas try again")
            match = False
        else: 
            match = 'M'
    else: 
        match = 'S'

    return match

def music(match):
    if match != False:
        if match == 'S'and pet == 'jason':
            playsound(random.choice(jasons))
        elif match == 'M' and pet == 'jason':
            playsound(random.choice(jasonm))
        elif match == 'S' and pet == 'olivia':
            playsound(random.choice(olivias))
        elif match == 'M' and pet == 'olivia':
            playsound(random.choice(oliviam))
    else:
        while match != False:
            matchWord(convert(audio_input))
            if match == 'S'and pet == 'jason':
                playsound(random.choice(jasons))
            elif match == 'M' and pet == 'jason':
                playsound(random.choice(jasonm))
            elif match == 'S' and pet == 'olivia':
                playsound(random.choice(olivias))
            elif match == 'M' and pet == 'olivia':
                playsound(random.choice(oliviam))
    return
