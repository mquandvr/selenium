def arrayComplexElementsProduct(real, imag):
    ret = [real[0], imag[0]] 
    for i in range(1, len(real)): 
        real1 = [ret[0], real[i]]
        imag1 = [ret[1], imag[i]]
        ret = proComplex(real1, imag1)
    return ret

def proComplex(a,b): 
    return[a[0]*a[1] - b[0]* b[1], a[0]* b[1] + a[1] * b[0]]