def divisorsPairs(sequence):
    cnt = 0
    for i in range(len(sequence)): 
        for j in range(len(sequence)): 
            if sequence[j]% sequence[i] == 0 and i !=j: 
                cnt +=1
    return cnt
        
