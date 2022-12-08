def solution(files):
    answer = []
    tmp = []
    idx = 0
    for file in files:
        head = ''
        number = ''
        tail = ''
        for i in range(len(file)):
            if 48<=ord(file[i])<=57:
                number += file[i]
                continue
            if number:
                break
            head += file[i]
        tmp.append((head.lower(), int(number), idx))
        idx += 1
        
    for i in sorted(tmp):
        answer.append(files[i[2]])
    
    return answer

'''
테스트 1 〉통과 (0.03ms, 10.3MB)
테스트 2 〉통과 (0.03ms, 10.3MB)
테스트 3 〉통과 (2.46ms, 10.5MB)
테스트 4 〉통과 (2.55ms, 10.5MB)
테스트 5 〉통과 (2.61ms, 10.5MB)
테스트 6 〉통과 (4.43ms, 10.5MB)
테스트 7 〉통과 (2.62ms, 10.4MB)
테스트 8 〉통과 (2.23ms, 10.6MB)
테스트 9 〉통과 (2.30ms, 10.5MB)
테스트 10 〉통과 (2.23ms, 10.5MB)
테스트 11 〉통과 (2.28ms, 10.5MB)
테스트 12 〉통과 (2.49ms, 10.4MB)
테스트 13 〉통과 (2.19ms, 10.6MB)
테스트 14 〉통과 (2.60ms, 10.7MB)
테스트 15 〉통과 (2.78ms, 10.7MB)
테스트 16 〉통과 (2.34ms, 10.5MB)
테스트 17 〉통과 (1.81ms, 10.5MB)
테스트 18 〉통과 (2.03ms, 10.4MB)
테스트 19 〉통과 (2.26ms, 10.6MB)
테스트 20 〉통과 (2.29ms, 10.4MB)
'''