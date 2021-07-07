from speech import *
from speechRecognition import *
from init import *
from icecream import ic as icA
from os import path
from qaProcess import *
from video import *
import threading




def first_greeting(ts,pl):
    # First greeting
    icA('Hello, welcome to voice center.')
    t1 = threading.Thread(target=play_videoFile, args=('voicenter.mp4',))
    if path.exists('voicenter.wav'):
        try:
            t1.start()
            pl.play('voicenter.wav')
            t1.join()
        except:
            print ("Error: unable to start thread")
    else:
        ts.save2file(ts.tts_request('Hello, welcome to voice center.'),ttsfile)
        t1.start()
        pl.play(ttsfile)
        t1.join()
        
        
def bye_session(ts,pl):
    t1 = threading.Thread(target=play_videoFile, args=('finalshort.mp4',))  
    if path.exists('final.wav'):
        try:
            t1.start()
            pl.play('final.wav')
            t1.join()

        except:
            print ("Error: unable to start thread")
    else:
        ts.save2file(ts.tts_request("""Thank you, Your details have been forward to the Information Security Representative.
        A representative on our behalf will contact you after the process is completed."""),ttsfile)
        t1.start()
        pl.play(ttsfile)
        t1.join()
        
def no_answer(ts,pl):
    icA('I did not get your answer, please start the process again')
    t1 = threading.Thread(target=play_videoFile, args=('get_vid.mp4',))
    if path.exists('NoAns.wav'):
        t1.start()
        pl.play('NoAns.wav')
        t1.join()
    else:    
        ts.save2file(ts.tts_request('I did not get your answer, please start the process again'),ttsfile)
        t1.start()
        pl.play(ttsfile)
        t1.join()
        
def sorry(ts,pl):      
    icA('Sorry, could you repeat, please?')
    t1 = threading.Thread(target=play_videoFile, args=('Sorry.mp4',))              
    if path.exists('Sorry.wav'):
        t1.start()
        pl.play('Sorry.wav')
        t1.join()
    else:    
        ts.save2file(ts.tts_request('Sorry, could you repeat, please?'),ttsfile)
        t1.start()
        pl.play(ttsfile)
        t1.join()
        
def user_information(ts,pl,info):
    icA('Please tell me your {}.'.format(info))
    t1 = threading.Thread(target=play_videoFile, args=('get_vid.mp4',))
    if path.exists('get{}.wav'.format(info)):
        try:
            t1.start()
            pl.play('get{}.wav'.format(info))
            t1.join()
        except:
            print ("Error: unable to start thread")
    else:
        ts.save2file(ts.tts_request('Please tell me your {}.'.format(info)),ttsfile)
        t1.start()
        pl.play(ttsfile)
        t1.join()


def questions(ts,pl,questionID,numQuestion,questionList):
    icA('{}'.format("sample {} {}".format(questionID,numQuestion)))
    t1 = threading.Thread(target=play_videoFile, args=('get_vid.mp4',))
    if path.exists('{}.wav'.format("sample {} {}".format(questionID,numQuestion))):
        t1.start()
        pl.play('{}.wav'.format("sample {} {}".format(questionID,numQuestion)))
        t1.join()
    else:
        ts.save2file(ts.tts_request('{}'.format(questionList[numQuestion])),ttsfile)
        t1.start()
        pl.play(ttsfile)
        t1.join()      