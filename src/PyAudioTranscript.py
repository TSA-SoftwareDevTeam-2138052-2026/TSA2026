import whisper_timestamped as whisper
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
    # file is as so:
    # id:
    #   start/end: word
    @classmethod
    def convert_timestamp_to_temp(cls, transcription: dict) -> str:
        current_transcription = ""
        for segment in transcription["segments"]:
            # Add segment id
            current_transcription = current_transcription + str(segment[id]) + ":\n"
            # Add words
            for word in segment["words"]:
                # adds:
                #   start/end: word
                # to the transcription
                current_transcription = current_transcription + f"  {str(word['start'])}/{str(word['end'])}: {word['text']}\n"
                print(current_transcription) #DEMO: TODO REMOVE LATER
        return current_transcription

    @classmethod
    def turn_into_transcript(cls, audio_file: str, model="base") -> str:
        try:
            recognizer = whisper.load_model(model, device="gpu") # Try faster GPU processing
        except:
            recognizer = whisper.load_model(model, device="cpu") # If unavaliable, try CPU processing.
        transcription = whisper.transcribe(recognizer, audio_file, beam_size=5, best_of=5, temperature=(0.0, 0.2, 0.4, 0.6, 0.8, 1.0))
        return cls.convert_timestamp_to_temp(transcription)