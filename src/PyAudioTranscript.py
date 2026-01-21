import speech_recognition as sr
recog = sr.Recognizer()

from os import path
audio = sr.AudioData.from_file("demo_audio.wav")

try:
    print(recog.recognize_google(audio))
except:
    print("ERROR")