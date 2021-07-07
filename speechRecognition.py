import speech_recognition as sr
from os import path
import os
from video import *



def speech_recognition(ID,info):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("USER SAY: ")
        audio = r.listen(source)
    if path.exists("users\\{}".format(ID)):
        with open("users\\{}\\{} {}.wav".format(ID,ID,info), "wb") as f:
            f.write(audio.get_wav_data())
    else:
        try:
            os.makedirs("users\\{}".format(ID))
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)
            
    try:
        with open("users\\{}\\{} {}.wav".format(ID,ID,info), "wb") as f:
                f.write(audio.get_wav_data())
        text = r.recognize_google(audio)
        print("{}".format(text))
    except:
        print("the sample do not recognized")
        return ""
    return text



def speech_recognitionID():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("USER SAY: ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("{}".format(text))
        except:
            print("the sample do not recognized")
            return ""
    return text