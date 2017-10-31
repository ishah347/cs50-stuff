from nltk.tokenize import sent_tokenize


def lines(a, b):
    # Divide a and b into their individual lines
    linesa = a.splitlines()
    linesb = b.splitlines()
    # Use set function to get rid of any duplicate lines
    # Make list of intersection between lines in a and lines in b and return it
    linesincommon = list(set(linesa).intersection(linesb))
    return linesincommon


def sentences(a, b):
    # Divide a and b into their individual sentences using sent_tokenize()
    sentencesa = sent_tokenize(a)
    sentencesb = sent_tokenize(b)
    # Use set function to get rid of any duplicate sentences
    # Make list of intersection between sentences in a and sentences in b and return it
    sentencesincommon = list(set(sentencesa).intersection(sentencesb))
    return sentencesincommon


def substrings(a, b, n):
    # Create two lists, one for a and one for b, to later append to
    substringsa = list()
    substringsb = list()
    # Iterate over string a
    for i in range(len(a) - n + 1):
        # Find each substring of length n in a through slicing
        x = a[i:i + n]
        # Append each substring to previously made list
        substringsa.append(x)
    # Iterate over string b
    for j in range(len(b) - n + 1):
        # Find each substring of length n in b through slicing
        y = b[j:j + n]
        # Append substring to previously made list
        substringsb.append(y)
    # Use set function to get rid of any duplicate substrings
    # Make list of intersection between substrings in a and substrings in b and return it
    substringsincommon = list(set(substringsa).intersection(substringsb))
    return substringsincommon
