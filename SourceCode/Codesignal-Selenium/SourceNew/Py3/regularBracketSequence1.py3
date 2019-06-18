def regularBracketSequence1(sequence):
    count = 0
    for i in sequence:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
            if count < 0: return False
    return count == 0
