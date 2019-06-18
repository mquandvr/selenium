def insertDashes(inputString):

    words = inputString.split()
    for i in range(len(words)):
        words[i] = "-".join(list(words[i]))
    return ' '.join(words)
