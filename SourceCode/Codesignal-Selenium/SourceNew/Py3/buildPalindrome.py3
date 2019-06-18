def buildPalindrome(st):

    
    return [st+st[:i][::-1] for i in range(len(st)) if st+st[:i][::-1] == (st+st[:i][::-1])[::-1]][0]