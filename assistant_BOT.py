from speech import *
from speechRecognition import *
import data_acq as da
from init import *
from pocketsphinx import LiveSpeech
from icecream import ic as icA
from datetime import datetime 
from qaProcess import *
from video import *
import threading
from conversation import *

def time_format():
    return f'{datetime.now()}  Assistant BOT|> '
icA.configureOutput(prefix=time_format)
icA.configureOutput(includeContext=False) # use True for including script file context file	
	

def get_info(pl,ts,info,ID): 
        rep_pl=0
        user_information(ts,pl,info)
        while True:
            t2 = threading.Thread(target=play_videoFile, args=('waiting.mp4',))
            t2.start()
            if info == "ID":
                userResponseString = speech_recognitionID()
            else:
                userResponseString = speech_recognition(ID,info)
            if userResponseString  == '':
                sorry(ts,pl)

                rep_pl = rep_pl + 1
                if rep_pl == 3:
                    no_answer(ts,pl)
                    main()
                else:
                    t2.join()                        
                    continue
            else:
                info = userResponseString
                t2.join()
                return info
        			

def getNumbersFromString(str):
    digits = [d for d in str if d.isdigit()]
    digit = ''.join(digits)
    return digit



class BOT():
    

    def bl(self,pl,st,ts):						
        first_greeting(ts,pl)
        ID = get_info(pl,ts,"ID" , "")
        ID = getNumbersFromString(ID)
        name = get_info(pl, ts,"name" , ID)  
        phone = get_info(pl ,ts ,"phone" , ID)
        phone = getNumbersFromString(phone)
        QA(pl,ts,ID)
        da.add_user_data(ID, name, phone)
        icA(ID + name + phone)
        icA('bye session')
        bye_session(ts,pl)
        

def main():    
    pl = Player()
    st = STT()
    ts = TTS()    										
    bot = BOT()
    keyphrase='hello'
    icA('BOT started..')
    speech = LiveSpeech(lm=False, keyphrase=keyphrase, kws_threshold=1e-20)
    while 1 :
        for phrase in speech:
            icA(phrase)
            if keyphrase in phrase.segments(detailed=True)[0][0]:
                bot.bl(pl,st,ts)
                icA('Ending current busyness logic iteration')
                break          
                
if __name__ == '__main__':
    main()
    
