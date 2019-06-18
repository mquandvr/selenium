def houseNumbersSum(inputArray):

    for i in range(len(inputArray)):
        if inputArray[i] == 0:
            return sum(inputArray[:i])