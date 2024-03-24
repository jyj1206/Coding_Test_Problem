from collections import deque
def solution(x, y, n):
    q = deque([(x, 0)])
    visited = {x}
    while q:
        cur_x , cnt = q.popleft()
        if cur_x == y:
            return cnt
        for next_x in [cur_x + n, cur_x * 2,cur_x * 3]:
            if next_x <= y and next_x not in visited:
                visited.add(next_x)
                q.append((next_x, cnt + 1))
    return -1