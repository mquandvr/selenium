def cyclicSequence(s):
    a=0
    for i in range (1,len(s)):
        if s[i]<=s[i-1]:
            a+=1
        if a>1:
            return False
    if a==0:
        return True
    if s[0]>s[len(s)-1]:
        return True
    return False
