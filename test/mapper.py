from test.nlp import tag
from test.appDict import appDict
from test.appDict import actionDict
import os
import sys
# voiceString = sys.argv[1]
voiceString = "shutdown comuter"   # Test without calling voice to text
runPath = "/home/aditya/Snakes/InstinctUX/run/"
print(tag(voiceString))
# tags is a dictionary of tagged words after NLP
tags = tag(voiceString)
keys = tags.keys()
print(keys)
google = 0
# Map different parts of speech
if "NOUN" in keys:
    nouns = list(tags.get("NOUN"))
    appKeys = list(appDict.keys())
    for i in range(0, len(appKeys)):
        for j in range(0, len(nouns)):
            if nouns[j].lower() in appDict.get(appKeys[i]):
                google = 1
                os.system("python3 "+runPath + appKeys[i]+".py " + '"'+voiceString + '"')

if "VERB" in keys:
    verbs = list(tags.get("VERB"))
    actionKeys = list(actionDict.keys())
    for i in range(0, len(actionKeys)):
        for j in range(0, len(verbs)):
            if verbs[j].lower() in actionDict.get(actionKeys[i]):
                google = 1
                os.system("python3 " + runPath + actionKeys[i] + ".py " + '"' + voiceString + '"')


if google == 0:
    os.system("python3 " + runPath + "google" + ".py " + '"' + voiceString + '"')

