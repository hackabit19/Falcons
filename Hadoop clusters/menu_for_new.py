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
elif text==2:
	engine.say("welcome for dockers setup...setting up dockers ")
	engine.runAndWait()
	speech_for_docker.sv()
else:
	engine.say("sorry sir you have entered wrong choice...exiting from tool")
	engine.runAndWait()
	exit()
        

