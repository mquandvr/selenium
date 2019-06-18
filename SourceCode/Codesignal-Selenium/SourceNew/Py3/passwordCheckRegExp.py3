def passwordCheckRegExp(s):
    return len(s)>4 and any(i.isupper() for i in s) and any(i.islower() for i in s) and any(i.isdigit() for i in s)
