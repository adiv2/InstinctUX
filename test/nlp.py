import nltk
from pickle import load
from nltk.corpus import stopwords
inputPKL = open('../Tagger/tagger.pkl', 'rb')
tagger = load(inputPKL)


def tag(sent):
    sent = sent[0].title() + sent[1:]
    print(sent)
    tokens = nltk.word_tokenize(sent)
    sent_tags = tagger.tag(tokens)
    tags = {}
    for x, y in sent_tags:
        if y not in tags.keys():
            tags[y] = [x]
        else:
            tags[y].append(x)
    return dict(tags)

removeWords = [" please ", " can ", " you ", " me ", " your ", " tell ", "what ", "where ", " which ", " is ", " the ", " who "]



def clean(removeWords, voiceString):
    stopword = stopwords.words('english')
    clean_string = ' '.join([word for word in voiceString.split() if word.lower() not in stopword])
    return clean_string


