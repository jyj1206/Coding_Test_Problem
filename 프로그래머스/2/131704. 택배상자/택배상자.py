def solution(order):
    answer = 0
    container_belt_1 = [i for i in range(len(order), 0, -1)]
    container_belt_2 = []
    
    for box in order:
        while container_belt_1 and box > container_belt_1[-1]:
            container_belt_2.append(container_belt_1.pop())
        
        if container_belt_1 and container_belt_1[-1] == box:
            container_belt_1.pop()
            answer += 1
            continue
        
        if container_belt_2 and container_belt_2[-1] == box:
            container_belt_2.pop()
            answer += 1
            continue
        break
    
    return answer
