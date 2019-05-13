import os
import subprocess
import time


while True :
    s = raw_input()
    s = int(s)

    if( s == 1 ):
        proc = subprocess.Popen("sudo omxplayer ~/test/sound/Init.wav", stdout = subprocess.PIPE, shell = True)
        time.sleep(2)

    elif( s == 2):
        proc = subprocess.Popen("sudo omxplayer ~/test/sound/grabSteer.wav", stdout = subprocess.PIPE, shell = True)
        time.sleep(2)

    elif( s == 3) :
        proc = subprocess.Popen("sudo omxplayer ~/test/sound/disengaged.wav", stdout = subprocess.PIPE, shell = True)
        time.sleep(2)
    else : 
        print("fail")
    time.sleep(5)
