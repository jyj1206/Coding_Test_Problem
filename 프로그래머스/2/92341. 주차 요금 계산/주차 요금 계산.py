from math import ceil
def solution(fees, records):
    def calculate_fee(time):
        total = fees[1]
        if time >= fees[0]:
            total += ceil((time-fees[0])/fees[2]) * fees[3]
        return total
    
    cars = {}
    # 차량 별로 total 시간 계산 및 기록하기
    for record in records:
        t, idx, r = record.split()
        h, m = map(int, t.split(":"))
        m += h * 60
        if r == "IN": 
            if idx not in cars:
                cars[idx] = [0, m, r] # total 시간, 입차 시간, IN OUT 여부
            else:
                cars[idx][1] = m
                cars[idx][2] = r
        else:
            cars[idx][0] += m - cars[idx][1] 
            cars[idx][2] = r
    
    answer = []
    for idx, record in sorted(cars.items()):
        total = cars[idx][0]
        if cars[idx][2] == "IN":
            total += 1439 - cars[idx][1]
        answer.append(calculate_fee(total))
    
    return answer
    
        