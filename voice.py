import speech_recognition as sr
import pyaudio

r=sr.Recognizer()
with sr.Microphone() as source:
    print('speak anything :')
    audio=r.listen(source)

    try:
        text=r.recognize_google(audio)
        print('you said : {}'.format(text))
    except:
        print('sorry could not recognize')
        
# if pyaudio module can't be downloaded from your local IDE
# download it from python utilities from web
# move the pyaudio file to python folder in your PC
# copy the pyaudio path and paste into your environmental variables in your Pc settings to use it. 
