removeWords = ["please", "can", "you", "me", "your", "tell", "what", "where", "which", "is", "the", "who"]
def clean(voiceString):
    for x in removeWords:
        voiceString = voiceString.replace(x, "")
    print(voiceString)
    return voiceString

