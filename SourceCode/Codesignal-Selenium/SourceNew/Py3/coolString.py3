def coolString(s):
    if not all(i.isalpha() for i in s):
        return 0
    for i,j in zip(s[1:], s):
        if i.islower() and j.islower() or i.isupper() and j.isupper():
            return False 
    return True

