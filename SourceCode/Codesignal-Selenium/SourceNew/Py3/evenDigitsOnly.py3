def evenDigitsOnly(n):
    s = str(n)
    for i in range(len(s)):
        if int(s[i])%2!=0:
            return False
    return True
