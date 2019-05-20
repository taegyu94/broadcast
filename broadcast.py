from flask import Flask
from flask import request
import os
import time
import requests

download_url = "http://polycast.qroo.co.kr/data/file/mp4/"
music_path = "/home/pi/broadcast/soundfile/"
test_file = "2krf.mp3"

app = Flask(__name__)
@app.route("/broadcast") 

def main():
        file_name = request.args.get("fileName")
        print ("success")
        file_list = os.listdir(music_path)
        print (file_list)
        
        if file_name in file_list:
                print ("OK")
                os.system("sudo omxplayer " + music_path + file_name)
        else :
                print ("Fail")
                r = requests.get(download_url + file_name, allow_redirects=True)
                print (r)
                if r.status_code == 200:
                    with open(music_path + file_name, 'wb') as f :
                        f.write(r.content)
                    os.system("sudo omxplayer " + music_path + file_name)
                else :
                    pass
		
        file_name = ""
        return "Finish"

if __name__ == "__main__":
        app.run(host='0.0.0.0')
