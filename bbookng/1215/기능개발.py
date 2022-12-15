def solution(progresses, speeds):
    answer = []

    day = 1
    cnt = 0
    tmp = []

    while progresses:
        if progresses[0] + (speeds[0] * day) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1

        else:
            day += 1
            if cnt:
                answer.append(cnt)
                cnt = 0

    answer.append(cnt)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

'''
테스트 1 〉	통과 (0.01ms, 9.99MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.1MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.03ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.1MB)
테스트 10 〉	통과 (0.07ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
'''