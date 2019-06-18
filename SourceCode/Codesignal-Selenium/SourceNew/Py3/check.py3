def check(a, b, r):
    for i in range(len(a)):
        if a[i] != r[i] and b[i] != r[i]:
            return False
    return True
def stringsCrossover(inputArray, result):
    r = 0
    for i in range(len(inputArray)):
        for j in range(i + 1, len(inputArray)):
            if check(inputArray[i], inputArray[j], result):
                r += 1
    return r
