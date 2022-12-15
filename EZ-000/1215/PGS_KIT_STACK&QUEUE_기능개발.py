def solution(progresses, speeds):
    days = []
    L = len(progresses)
    for idx in range(L):
        temp = (100 - progresses[idx]) // speeds[idx]
        if (100 - progresses[idx]) % speeds[idx]:
            temp += 1
        days.append(temp)

    tmp_max = days[0]
    cnt = 0
    answer = []
    for day in days:
        if day <= tmp_max:
            cnt += 1
        else:
            tmp_max = day
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    return answer

# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.05ms, 10.4MB)
# 테스트 3 〉	통과 (0.04ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.4MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.1MB)
# 테스트 8 〉	통과 (0.01ms, 10.3MB)
# 테스트 9 〉	통과 (0.02ms, 10.1MB)
# 테스트 10 〉	통과 (0.02ms, 10.3MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
