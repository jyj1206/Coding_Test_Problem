def solution(a, b, c):
    first = sum([a, b, c])
    second = sum(map(lambda x : x ** 2, (a, b, c)))
    third = sum(map(lambda x: x**3, (a,b,c)))
    if a==b and b==c and c==a:
        return first * second * third
    elif a!=b and b!=c and c!=a:
        return first
    else:
        return first * second