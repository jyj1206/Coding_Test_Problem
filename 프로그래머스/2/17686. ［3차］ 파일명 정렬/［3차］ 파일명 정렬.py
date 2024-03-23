def solution(files):
    splited_files = []
    for file in files:
        NUMBER_START, TAIL_START = 0, 0
        for i in range(len(file)):
            if not file[i].isdigit():
                NUMBER_START = i+1
            else:
                break
                
        for i in range(NUMBER_START, len(file)):
            if file[i].isdigit():
                TAIL_START = i+1
            else:
                break
                
        HEAD = file[:NUMBER_START]
        NUMBER = file[NUMBER_START:TAIL_START]
        TAIL = file[TAIL_START:] if len(file) > TAIL_START else ""
        splited_files.append([file[:NUMBER_START], file[NUMBER_START:TAIL_START], file[TAIL_START:]])
    
    splited_files.sort(key=lambda x : (x[0].upper(), int(x[1])))
    
    answer = ["".join(splited_file) for splited_file in splited_files]
    
    return answer
    
        
        
                
        