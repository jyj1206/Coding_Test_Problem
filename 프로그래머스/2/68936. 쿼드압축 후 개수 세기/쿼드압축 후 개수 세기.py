def solution(arr):
    answer = [0, 0]
    def dc(x, y, n):
        check = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != check:
                    dc(x, y, n//2)
                    dc(x, y + n//2, n//2)
                    dc(x + n//2, y, n//2)
                    dc(x + n//2, y + n//2, n//2)
                    return
        answer[check] += 1
    dc(0, 0, len(arr))
    return answer