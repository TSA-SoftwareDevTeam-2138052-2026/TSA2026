import whisper_timestamped as whisper
class PyAudioTranscript:
    # file is as so:
    # id:
    #   start/end: word
    @classmethod
    def convert_timestamp_to_temp(cls, transcription: dict) -> str:
        current_transcription = ""
        for segment in transcription["segments"]:
            # Add segment id
            current_transcription = current_transcription + str(segment["id"]) + ":\n"
            # Add words
            for word in segment["words"]:
                # adds:
                #   start/end: word
                # to the transcription
                current_transcription = current_transcription + f"  {str(word['start'])}/{str(word['end'])}: {word['text']}\n"
        return current_transcription

    @classmethod
    def turn_into_transcript(cls, audio_file: str, model="base") -> str:
        audio = whisper.load_audio(audio_file)
        try:
            recognizer = whisper.load_model(model, device="gpu") # Try faster GPU processing
        except:
            print("GPU failed. Trying CPU...")
            try:
                recognizer = whisper.load_model(model, device="cpu") # If unavaliable, try CPU processing.
            except Exception as e:
                print(e)
                with open("C:/Users/Zachary.Smith/error.txt", "w") as file:
                    file.write(e.__str__())
                    file.close()
                exit()
        try:
            try:
                transcription = whisper.transcribe(recognizer, audio)
                return cls.convert_timestamp_to_temp(transcription)
            except Exception as e:
                print(e)
                with open("C:/Users/Zachary.Smith/error.txt", "w") as file:
                    file.write(e.__str__())
                    file.close()
                return "E"
        except Exception as e:
            return str(e)