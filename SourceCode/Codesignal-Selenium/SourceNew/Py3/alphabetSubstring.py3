def alphabetSubstring(s):
    if len(s) == 1: 
        return True
    for i in range(1, len(s)): 
        if ord(s[i]) != ord(s[i-1]) + 1:
            return False 
    return True
