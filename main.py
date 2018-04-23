'''
import speech_recognition as sr

def recognize():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		print("Say something!")
		audio = r.listen(source)
	try:
		return  r.recognize_google(audio)
	except sr.UnknownValueError:
		return "Google Speech Recognition could not understand audio"
	except sr.RequestError as e:
		return "Could not request results from Google Speech Recognition service; {0}".format(e)
		


s = recognize()
file = open('output.txt','a')
file.write(s+'\n')
'''

file = open('output.txt','w')
file.write('Hello')
