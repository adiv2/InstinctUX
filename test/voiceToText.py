import speech_recognition as sr
import os
# Lists and prints microphones found
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    # print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
# Listening for audio input
    audio = r.listen(source)
try:
    # Google speech to text API
    voiceString = r.recognize_google(audio)
    print("You said: " + voiceString)
    # Call mapper.py with voice string as arg
    print("mapper was called")
    os.system("python3 mapper.py " + '"'+voiceString + '"')
    # Error handling
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


