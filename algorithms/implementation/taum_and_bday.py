
# My solution

def taumBday(b, w, bc, wc, z):
    if bc == wc:
        return b*bc + w*wc
    elif bc > wc + z:
        return (w+b)*wc + b*z
    elif wc > bc + z:
        return (w+b)*bc + w*z
    return b*bc + w*wc


# Another solution 
# Very short and clean

def taumBday2(b, w, bc, wc, z):
    return b*min(bc, wc+z) + w*min(wc,bc+z)