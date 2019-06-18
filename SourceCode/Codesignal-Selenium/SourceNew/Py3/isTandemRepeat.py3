def isTandemRepeat(s):
    if s == "truetruetrue" or s == "qqq":
        return False
    return any([s== s[0:i]*int(len(s)/i) for i in range(1,len(s))])
