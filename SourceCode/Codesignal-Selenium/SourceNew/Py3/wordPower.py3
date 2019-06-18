def wordPower(word):
    num =  {chr(n): n - 96 for n in range(97,123)}
    return sum([num[ch] for ch in word])
