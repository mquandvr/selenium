def commonCharacterCount(s1, s2):
    a1 = [0 for i in range(26)]
    a2 = [0 for i in range(26)]
    for i in s1: 
        a1[ord(i) - ord('a')] += 1
    for i in s2: 
        a2[ord(i) - ord('a')] += 1
    ret = 0
    for i in range(26): 
        ret += min(a1[i], a2[i])
    return ret