def caesarBoxCipherEncoding(s):
    n = int(math.sqrt(len(s)))
    c = ""
    for i in range(n):
        c += s[i::n]
    return c

