removeWords = [" please ", " can ", " you ", " me ", " your ", " tell ", "what ", "where ", " which ", " is ", " the ", " who "]


def clean(removeWords, voiceString):
    voiceString.lower()
    voiceString = " " + voiceString + " "
    for x in removeWords:
        voiceString = voiceString.replace(x, " ")
    return voiceString

