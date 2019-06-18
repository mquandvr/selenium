def arrayMaximalDifference(inputArray):
    a, b = 0, 1
    for i in range(len(inputArray)):
        for j in range(i+1, len(inputArray)):
            if abs(inputArray[i]-inputArray[j])>abs(inputArray[a]-inputArray[b]):
                a, b = i, j
    return abs(inputArray[a]-inputArray[b])