def chessBoardSquaresUnderQueenAttack(a, b):
    cnt = 0
    for i in range(a):
        for j in range(b):
            for ii in range(a):
                for jj in range(b):
                    if not (ii == i and jj == j):
                        if ii == i or jj == j or abs(ii - i) == abs(jj - j):
                            cnt+=1
    return cnt