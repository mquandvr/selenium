def firstMultiple2(divisors, start):

    answer = start
    while True:
        for i in range(len(divisors)):
            if answer % divisors[i] == 0:
                return answer
        answer += 1
