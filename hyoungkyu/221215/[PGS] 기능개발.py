def solution(progresses, speeds):
    answer = []
    
    current = 0
    days = 0
    
    while True:
        cnt = 1
        # 날짜 세기
        days += (100 - (progresses[current] + speeds[current]*days)) // speeds[current] + 1
        if (100 - (progresses[current] + speeds[current]*days)) % speeds[current] == 0:
            days -= 1
        # 같이 배포될 작업들 구하기
        for idx in range(current+1, len(progresses)):
            current = idx
            if progresses[idx] + speeds[idx]*days >= 100:
                cnt += 1
            else:
                answer.append(cnt)
                cnt = 0
                break
        # 마지막 부분 처리하기
        if current == len(progresses)-1 and cnt:
            answer.append(cnt)
            break
    
    return answer

'''
테스트 1 〉통과 (0.01ms, 10.2MB)
테스트 2 〉통과 (0.02ms, 10.2MB)
테스트 3 〉통과 (0.03ms, 10.2MB)
테스트 4 〉통과 (0.01ms, 10.2MB)
테스트 5 〉통과 (0.00ms, 10.2MB)
테스트 6 〉통과 (0.01ms, 10.2MB)
테스트 7 〉통과 (0.02ms, 10.3MB)
테스트 8 〉통과 (0.01ms, 10.3MB)
테스트 9 〉통과 (0.03ms, 10.2MB)
테스트 10 〉통과 (0.02ms, 10.3MB)
테스트 11 〉통과 (0.01ms, 10.3MB)
'''