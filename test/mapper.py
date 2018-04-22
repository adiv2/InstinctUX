from test.nlp import tag
from test.appDict import appDict
import os
import sys
voiceString = sys.argv[1]
#voiceString = "close chrome"  # Test without calling voice to text
runPath = "/home/aditya/Snakes/InstinctUX/run/"
print(tag(voiceString))
# tags is a dictionary of tagged words after NLP
tags = tag(voiceString)
keys = tags.keys()

google = 0
# Map different parts of speech
if "NNP" in keys:
    nouns = list(tags.get("NNP"))
    appKeys = list(appDict.keys())
    for i in range(0, len(appKeys)):
        for j in range(0, len(nouns)):
            if nouns[j] in appDict.get(appKeys[i]):
                google = 1
                os.system("python3 "+runPath + appKeys[i]+".py " + '"'+voiceString + '"')

if "NN" in keys:
    nouns = list(tags.get("NN"))
    appKeys = list(appDict.keys())
    for i in range(0, len(appKeys)):
        for j in range(0, len(nouns)):
            if nouns[j] in appDict.get(appKeys[i]):
                google = 1
                os.system("python3 " + runPath + appKeys[i] + ".py " + '"' + voiceString + '"')
if "NNS" in keys:
    nouns = list(tags.get("NNS"))
    appKeys = list(appDict.keys())
    for i in range(0, len(appKeys)):
        for j in range(0, len(nouns)):
            if nouns[j] in appDict.get(appKeys[i]):
                google = 1
                os.system("python3 " + runPath + appKeys[i] + ".py " + '"' + voiceString + '"')

if "NNPS" in keys:
    nouns = list(tags.get("NNPS"))
    appKeys = list(appDict.keys())
    for i in range(0, len(appKeys)):
        for j in range(0, len(nouns)):
            if nouns[j] in appDict.get(appKeys[i]):
                google = 1
                os.system("python3 " + runPath + appKeys[i] + ".py " + '"' + voiceString + '"')

if google == 0:
    os.system("python3 " + runPath + "google" + ".py " + '"' + voiceString + '"')

