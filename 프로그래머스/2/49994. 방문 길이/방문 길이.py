def solution(dirs):
    x, y = 0, 0
    visited = set()
    direction = {'U':(-1, 0),'D':(1, 0), 'R':(0, 1), 'L':(0, -1)}
    for d in dirs:
        dx, dy = direction[d]
        nx = x + dx
        ny = y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            x, y = nx, ny
    return len(visited) // 2