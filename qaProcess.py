from speech import *
from speechRecognition import *
from init import *
import random
from video import *
import threading
from assistant_BOT import main
from conversation import *





def QA(pl,ts,ID): 
        question1 = ["Who invites you?","What is the department you want to go to?","Who is your contact person?",
                     "Have you visit here before?", "Have you visited our company before? ","Who summoned you to us?"]
        question2 = ["Give the name of a staff member who works with you? ","Who summoned you to us?","On what company / representative did you come to us? "]
        question3 = ["For how many days is your visit planned?","Which floor is the department you want to reach ?","Please tell me which floor you want to go?","What field are you in? "]
        num_1 = random.randint(0,len(question1)-1)
        num_2 = random.randint(0,len(question2)-1)
        num_3 = random.randint(0,len(question3)-1)
        answerQuestion(pl,ts, ID, "1", num_1 , question1)
        answerQuestion(pl,ts, ID, "2", num_2 , question2)
        answerQuestion(pl,ts, ID, "3", num_3 , question3)
        
        



def answerQuestion(pl,ts, ID, questionID, numQuestion , questionList):
    rep_pl=0
    questions(ts,pl,questionID,numQuestion,questionList)
    while True:
        t2 = threading.Thread(target=play_videoFile, args=('waiting.mp4',))
        t2.start()
        userResponseString = speech_recognition(ID,"sample 1 {}".format(numQuestion))
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
            t2.join()
            return		