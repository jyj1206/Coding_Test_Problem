def solution(code):
    mode = 0
    answer = ''
    for idx in range(len(code)):
        if code[idx] == '1':
            mode = 1 if mode == 0 else 0
        else:       
            if idx%2==mode:
                answer += code[idx]
    return answer if answer else "EMPTY"