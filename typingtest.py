from time import *

import random as r


# print(time())  #1971 se itna time hua h  utna type krega


def mistake(paratest,usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1 
        
    return error
            

def speed_test(timestart,timeend, userinput):
    time_diff = timeend - timestart
    time_r = round(time_diff,2)
    speed = len(userinput)/time_r
    return round(speed)
    



test=[" Notorious as an iconoclast, that music critic isn't afraid to go after sacred cows",
      "This pinpoints a fundamental weakness in the libertarian defence of a market economy",
     "She broke taboos, risking ostracism and derision in the process",
       "A pertinacious little boy who was determined to catch and collect reptiles",
       "So far, so fairy tale, but the story drifts back into the quotidian details of village life"

]

test1= r.choice(test)

print(   "                *******TYPING TEST*********                  ")
print()
print(test1)
print()
print()

time1 = time()
testinput = input("START WRITTING :" )
time2 = time()


#FUNCTION CALL

print('speed : ',speed_test(time1,time2, testinput) ," word/sec")   

print("error: ",mistake(test1,testinput))

