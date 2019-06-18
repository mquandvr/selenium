def deleteDigit(n):
    s = str(n)
    m =0
    for i in range(len(s)):
        s1 = s[:i] + s[(i+1):]
        if int(s1) > m:
            m = int(s1)
    return m
