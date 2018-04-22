import nltk
from pickle import load
input = open('../tagger/tagger.pkl', 'rb')
tagger = load(input)

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
