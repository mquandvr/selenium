def removeDuplicateCharacters(str):
    s = ""
    for i in str:
        if str.count(i)==1:
            s+=i
    return s
