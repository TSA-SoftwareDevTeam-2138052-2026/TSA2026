import whisper_timestamped as whisper
import pathlib
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
    def convert_timestamp_to_transcript(cls, transcription: dict) -> str:
        current_transcription = ""
        for segment in transcription["segments"]:
            # Add words
            for word in segment["words"]:
                current_transcription = current_transcription + f"{word['text']} "
        current_transcription = current_transcription.strip()
        return current_transcription

    @classmethod
    def __preconvert__(cls, audio_file: str, model: str) -> dict:
        audio = whisper.load_audio(audio_file)
        try:
            recognizer = whisper.load_model(model, device="gpu") # Try faster GPU processing
        except:
            try:
                recognizer = whisper.load_model(model, device="cpu") # If unavaliable, try CPU processing.
            except Exception as e:
                print(e)
                with open(pathlib.Path.home().as_posix() + "/AudioVisual_Helper_ERROR.log", "w") as file:
                    file.write(e.__str__())
                    file.close()
                exit()
        try:
            transcription = whisper.transcribe(recognizer, audio, beam_size=5, best_of=5, temperature=(0.0,0.2,0.4,0.6,0.8,1.0), initial_prompt="Hello.")
            return transcription
        except Exception as e:
            print(e)
            with open(pathlib.Path.home().as_posix() + "/AudioVisual_Helper_ERROR.log", "w") as file:
                file.write(e.__str__())
                file.close()
            return {"segments": {"id:": 0, "words": ["ERROR", str(e)]}}
    
    @classmethod
    def turn_into_captions(cls, audio_file: str, model: str="base") -> str:
        transcription = cls.__preconvert__(audio_file, model)
        try:
            try:
                return cls.convert_timestamp_to_temp(transcription)
            except Exception as e:
                print(e)
                with open(pathlib.Path.home().as_posix() + "/AudioVisual_Helper_ERROR.log", "a") as file:
                    file.write(e.__str__())
                    file.close()
                return "E"
        except Exception as e:
            return str(e)

    @classmethod
    def turn_into_transcript(cls, audio_file: str, model="base") -> str:
        transcription = cls.__preconvert__(audio_file, model)
        try:
            try:
                return cls.convert_timestamp_to_transcript(transcription)
            except Exception as e:
                print(e)
                with open(pathlib.Path.home().as_posix() + "/AudioVisual_Helper_ERROR.log", "a") as file:
                    file.write(e.__str__())
                    file.close()
                return "E"
        except Exception as e:
            return str(e)