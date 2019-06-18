def replaceAllDigitsRegExp(s):
    o = ''
    for l in s:
        if l.isdigit():
            o += '#'
        else:
            o += l
    return o

