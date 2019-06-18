def isArithmeticProgression(sequence):
    a = [x-y for y, x in zip(sequence[:-1], sequence[1:])]
    
    return(len(set(a))==1)