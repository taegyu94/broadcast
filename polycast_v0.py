import os
import subprocess
import time

music_path = "/home/pi/broadcast/soundfile/"
file_name = ""

while True :
    file_name = raw_input()
    file_list = os.listdir(music_path)
    print file_list
    
    if file_name in file_list:
        print "OK"
        proc = subprocess.Popen("sudo omxplayer " + music_path + file_name , stdout = subprocess.PIPE, shell = True)
        print proc
    else :
        print "Fail"
        proc = subprocess.Popen("sudo omxplayer " + music_path + file_name , stdout = subprocess.PIPE, shell = True)
        print proc

