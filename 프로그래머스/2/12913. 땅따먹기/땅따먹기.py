def solution(land):
    d = [[0] * 4 for _ in range(len(land))]
    d[0] = land[0][:]
    for i in range(1, len(land)):
        d[i][0] = land[i][0] + max(d[i-1][1], d[i-1][2], d[i-1][3])
        d[i][1] = land[i][1] + max(d[i-1][0], d[i-1][2], d[i-1][3])
        d[i][2] = land[i][2] + max(d[i-1][0], d[i-1][1], d[i-1][3])
        d[i][3] = land[i][3] + max(d[i-1][0], d[i-1][1], d[i-1][2])
    return max(d[len(land)-1])
    