import os
import time
import requests

download_url = "http://polycast.qroo.co.kr/data/file/mp4/"
music_path = "/home/pi/broadcast/soundfile/"
file_name = ""
test_file = "2krf.mp3"

while True :
    print "inset file_name"
    file_name = raw_input()
    print "success"
    file_list = os.listdir(music_path)
    print file_list
    
    if file_name in file_list:
        print "OK"
        os.system("sudo omxplayer " + music_path + file_name)
    else :
        print "Fail"
        r = requests.get(download_url + file_name, allow_redirects=True)
        print r
        if r.status_code == 200 :
            print "200"
        else :
            print "else"
        with open(music_path + file_name, 'wb') as f :
            f.write(r.content)

        os.system("sudo omxplayer " + music_path + file_name)
    file_name = ""
