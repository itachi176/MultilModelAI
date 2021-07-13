import speech_recognition as sr
import pyaudio
  
# Initialize the recognizer 
def speech_to_text():
    r = sr.Recognizer() 
    
    with sr.Microphone() as source:
        print("speak anything: ")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="vi-VI")
            print(text)
            return text
        except:
            print("loi roi !!!\n")