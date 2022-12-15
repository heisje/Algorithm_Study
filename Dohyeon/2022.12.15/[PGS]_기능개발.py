def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        tmp = 100-progresses[i]
        if tmp % speeds[i] == 0:
            days.append(tmp // speeds[i])
        else:
            days.append((tmp // speeds[i]) + 1)

    present_val = 0
    temp_val = 0
    for i in range(len(days)):
        if present_val < days[i]:
            answer.append(temp_val)
            present_val = days[i]
            temp_val = 1
        else:
            temp_val += 1
    else:
        answer.append(temp_val)
    answer.pop(0)
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
"""