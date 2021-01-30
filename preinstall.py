#pre_installation
#it takes a bit while fyi.
import os
os.system('pip install --upgrade pip')
os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
# ^homebrew installation
#user needs to type their device's password to proceed
os.system('pip install SpeechRecognition')
os.system('pip install playsound')
os.system('pip3 install -U PyObjC')
os.system('pip install gTTS')
os.system('brew install portaudio')
os.system('pip install pyaudio')
#necessary libraries installed.
