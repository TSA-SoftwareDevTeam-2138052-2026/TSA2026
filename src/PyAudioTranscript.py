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

class PyAudioTranscript:
    @classmethod
    def turn_into_transcript(cls, audio_file: str, model="base") -> str:
        recognizer = whisper.load_model(model)
        transcription = recognizer.transcribe(audio_file)
        return str(transcription['text'])