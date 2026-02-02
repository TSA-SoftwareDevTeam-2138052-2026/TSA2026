import whisper
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
    recognizer = whisper.load_model("base")
    
    @classmethod
    def turn_into_transcript(cls, audio_file: str) -> str:
        transcription = cls.recognizer.transcribe(audio_file)