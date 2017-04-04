def power(base,exponent):
    result = 1.0
    if (base ==0):
        return 0
    if(type(exponent) != int):
        return faulse
    
    if(exponent < 0):
        newExponent = -exponent
    if(exponent > 0):
        newExponent = exponent
        
    result = powerWithUnsignExponent(base,newExponent)
    if (exponent < 0):
        result = (1.0)/result
    return result
def powerWithUnsignExponent(base,exponent):
    if(exponent == 0):
        return 1.0
    if(exponent == 1):
        return base
    result = powerWithUnsignExponent(base,exponent>>1)
    
    result *= result
    
    if(exponent & 1 == 1):
        result *= base
    return result
print(power(3,3))
    
        
