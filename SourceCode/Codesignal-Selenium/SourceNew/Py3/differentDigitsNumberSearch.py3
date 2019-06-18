def differentDigitsNumberSearch(inputArray):
    for i in inputArray:
        for j in str(i):
            if str(i).count(j) > 1:
                break
            if j == str(i)[len(str(i)) - 1] and str(i).count(j) == 1:
                return i
    return -1