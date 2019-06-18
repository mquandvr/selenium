def isGeometricProgression(sequence):
    x = sequence[1]/sequence[0]
    for i in range(len(sequence)-1):
        if sequence[i+1]/sequence[i] != x:
            return False
    
    return True