#welcome message
import speech_recognition as sr
import random
from scipy.io import wavfile
import wavio
study = ['productive', 'school', 'grades', 'pressured', 'university', 'work', 'assignment', 'deadline', 'school', 'pencil', 'laptop']
meditation = ['rest', 'calm', 'tired', 'anxious', 'soothing', 'burnout', 'stressed', 'headache', 'zen', 'recenter', 'recalibrate']
jasons = ['S1B.wav','S2B.wav','S3B.wav','S4B.wav','S5B.wav']
jasonm = ['M1B.wav','M2B.wav','M3B.wav','M4B.wav','M5B.wav']
olivias = ['S1G.wav','S2G.wav','S3G.wav','S4G.wav','S5G.wav']
oliviam = ['M1G.wav','M2G.wav','M3G.wav','M4G.wav','M5G.wav']

def petchoose(file):
    r = sr.Recognizer()
    with sr.WavFile(file) as source:
        audio = r.record(source)
        inputaudio = r.recognize_google(audio)
        lst = [inputaudio]
        petchoose = convert(lst).lower()
    return petchoose


def start_analysis(file):
    r = sr.Recognizer()
    with sr.WavFile(file) as source:
    #wavio.write(file, data, fs ,sampwidth=2)

    # Convert `data` to 32 bit integers:
        #y = (np.iinfo(np.int32).max * (data/np.abs(data).max())).astype(np.int32)

        #wavfile.write("updated" + file, source, y)
        audio = r.record(source)
        inputaudio = r.recognize_google(audio)
        lst = [inputaudio]
        user_sent = convert(lst)
        print(user_sent)
    return music(matchWord(user_sent))


def convert(lst): 
    return (lst[0].lower().split())

def matchWord(lst):
    check = any(item in lst for item in study)
    if check == False:
        check = any(item in lst for item in meditation)
        if check == False:
            print("We didn't catch you. Please try again")
            match = False
        else: 
            match = 'M'
    else: 
        match = 'S'

    return match

def music(match):
    if match != False:
        if match == 'S'and pet == 'jason':
            return ('music/' + random.choice(jasons))
        elif match == 'M' and pet == 'jason':
            return ('music/' + random.choice(jasonm))
        elif match == 'S' and pet == 'olivia':
            return ('music/' + random.choice(olivias))
        elif match == 'M' and pet == 'olivia':
            return ('music/' + random.choice(oliviam))

    return '' #frontend developers, check this and if you reach here, you should ask user for input again.
