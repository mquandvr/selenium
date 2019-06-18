def countNeighbouringPairs(inputString):
    c = 0
    for i in range(len(inputString) - 1):
        if inputString[i] == inputString[i+1]:
            c += 1
    return c

