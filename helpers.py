from nltk.tokenize import sent_tokenize


def lines(a, b):
    # Divide a and b into their individual lines
    linesa = a.splitlines()
    linesb = b.splitlines()
    # Make list of intersection between lines in a and lines in b and return it
    linesincommon = list(set(linesa).intersection(linesb))
    return linesincommon


def sentences(a, b):
    # Divide a and b into their individual sentences using sent_tokenize()
    sentencesa = sent_tokenize(a)
    sentencesb = sent_tokenize(b)
    # Make list of intersection between sentences in a and sentences in b and return it
    sentencesincommon = list(set(sentencesa).intersection(sentencesb))
    return sentencesincommon


def substrings(a, b, n):
    # Create two lists to later append to
    substringsa = list()
    substringsb = list()
    # Go through a and b, dividing both into substrings that are appended to the previously made lists
    for i in range(len(a) - n + 1):
        x = a[i:i + n]
        substringsa.append(x)
    for j in range(len(b) - n + 1):
        y = b[j:j + n]
        substringsb.append(y)
    # Make list of intersection between substrings in a and substrings in b and return it
    substringsincommon = list(set(substringsa).intersection(substringsb))
    return substringsincommon
