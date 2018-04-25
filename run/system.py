import sys
sys.path.insert(0, '/home/aditya/Snakes/InstinctUX/')
import os
from test.nlp import clean

systemDict = {
    "halt": ["shutdown", "halt"],
    "reboot": ["reboot", "restart"],
    "logout": ["exit", "logout"]

}

voiceString = sys.argv[1]
# voiceString = "shutdown comuter"   # Test without calling voice to text
voiceString = clean([], voiceString)
voiceList = voiceString.split(" ")

sysKeys = list(systemDict.keys())
for i in range(0, len(systemDict)):
    for j in range(0, len(voiceList)):
        if voiceList[j].lower() in systemDict.get(sysKeys[i]):
            # print(sysKeys[i])
            os.system(sysKeys[i])
