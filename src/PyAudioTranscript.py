#import speech_recognition as sr
#recog = sr.Recognizer()
#
#from os import path
#audio = sr.AudioData.from_file("demo_audio.wav")

#try:
#    print(recog.recognize_google(audio))
#except:
#    print("ERROR")

# Real program here

class PyAudioTranscript():
    recognizer = sr.Recognizer()
    
    @classmethod
    def turn_into_transcript(cls, audio_file: str) -> str:
        audio = sr.AudioData.from_file(audio_file)
        return cls.recognizer.recognize_google(audio)