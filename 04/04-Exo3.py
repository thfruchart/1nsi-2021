# Chap4 EXO3
def max2(x,y):
    if x>y:
        return x
    else :
        return y

def max3(x,y,z):
    if x >= y and x >= y :
        return x
    if y >= x and y >= z:
        return y
    if z >= x and z >= y :
        return z

def max3(x,y,z) :
    m = max2(x,y)
    M = max2(m, z)
    return M


