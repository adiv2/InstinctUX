import nltk


def tag(voiceString):
    tokens = nltk.word_tokenize(voiceString)
    sent_tags = nltk.pos_tag(tokens)
    tags = {}
    for x, y in sent_tags:
        if y not in tags.keys():
            tags[y] = [x]
        else:
            tags[y].append(x)
    return dict(tags)



