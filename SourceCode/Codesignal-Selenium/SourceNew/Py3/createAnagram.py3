def createAnagram(s, t):
    return sum(max(0, s.count(i)-t.count(i)) for i in set(s))
