def longestDigitsPrefix(inputString):
    res = ''
    for i in inputString:
        if i >= '0' and i <= '9':
            res += i
        else:
            break
    return res
