from math import gcd
def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = numer1 * denom2 + numer2 * denom1
    
    x = gcd(denom, numer)
    return [numer//x, denom//x]