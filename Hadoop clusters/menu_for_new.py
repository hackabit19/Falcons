#!"C:\ProgramData\Anaconda3\python.exe"
import speech_speak
import speech_recognition as sr
import pyttsx3
import speech_for_docker
engine=pyttsx3.init()
print("welcome to tool......\nenter 1 for setup hadoop and map reduce cluster .......\nenter 2 for setup dockers")
engine.say("welcome to tool......enter 1 for setup hadoop and map reduce cluster .......enter 2 for setup dockers")
engine.runAndWait()
#mic=sr.Microphone()
ipc = int(input("enter the client ip : "))
    k = input("enter the client domain name : ")
    os.system("ssh-keygen")
    os.system("ssh-keyscan 192.168.43.{} > known_hosts".format(ipc))
    os.system("ssh-copy-id 192.168.43.{}".format(ipc))
#rec=sr.Recognizer()
#with mic as source:
print("enter your choice")
	#rec.adjust_for_ambient_noise(source, duration=5)
   # audio=rec.listen(source)
    #text=rec.recognize_google(audio)
text=int(input())	
print(text)
if text==1:
	engine.say("welcome to hadoop setup...setting hadoop and map reduce cluster....running hcluster file")
	engine.runAndWait()
	speech_speak.s()
elif:
	engine.say("welcome for dockers setup...setting up dockers ")
	engine.runAndWait()
	speech_for_docker.sv()
        

