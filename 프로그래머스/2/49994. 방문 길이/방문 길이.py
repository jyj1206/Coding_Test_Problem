def solution(dirs):
    x, y = 0, 0
    answer = 0
    visited = set()
    direction = {'U':(-1, 0),'D':(1, 0), 'R':(0, 1), 'L':(0, -1)}
    for d in dirs:
        dx, dy = direction[d]
        nx = x + dx
        ny = y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            road = (x, y, nx, ny)
            if road not in visited:
                visited.add(road)
                visited.add((nx, ny, x, y))
                answer += 1
            x, y = nx, ny
    return answer