# All code in this file is just a sample to make sure it works. The code came from GeeksForGeeks, at the article https://www.geeksforgeeks.org/python/python-convert-speech-to-text-and-text-to-speech/
# This code is just a demo. It is not meant to go into the final product.

import speech_recognition as sr
r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()  
            print("You said:", text)
            
            if "exit" in text:
                print("Exiting program...")
                break

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Could not understand audio")

    except KeyboardInterrupt:
        print("Program terminated by user")
        break