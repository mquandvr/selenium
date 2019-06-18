def telephoneGame(messages):

        for i in range(len(messages)-1):
                if messages[i+1]!=messages[i]:
                        return i+1
        return -1