def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        case = []
        for i in range(s, e+1):
            if arr[i] > k:
                case.append(arr[i])
        if case:
            answer.append(min(case))
        else:
            answer.append(-1)
    return answer