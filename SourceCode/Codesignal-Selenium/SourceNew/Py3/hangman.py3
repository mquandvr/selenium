def hangman(word, letters):

    neededLetters = [False] * 26
    need = 0
    for i in range(len(word)):
        c = ord(word[i]) - ord('a')
        if not neededLetters[c]:
            neededLetters[c] = True
            need += 1

    missed = 0
    for i in range(len(letters)):
        if not (missed < 6 and need > 0):
            break
        c = ord(letters[i]) - ord('a')
        if neededLetters[c]:
            neededLetters[c] = False
            need -= 1
        else:
            missed += 1

    return need == 0
