def arithmeticExpression(a, b, c):
    s="+-/*"
    if a+b==c:
        return True
    elif a-b==c:
        return True
    elif a/b==c:
        return True
    elif a*b==c:
        return True
    return False