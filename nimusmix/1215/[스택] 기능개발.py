def solution(progresses, speeds):
    ans = []
    plan = [0] * len(progresses)
    
    for i in range(len(progresses)):
        day = (100 - progresses[i]) // speeds[i]
        day = day if progresses[i] + (speeds[i] * day) == 100 else day + 1
        plan[i] = day
    
    cnt = 1
    while plan:
        if plan[0] >= plan[1]:
            cnt += 1
            plan.pop(1)
        else:
            ans.append(cnt)
            plan, cnt = plan[1:], 1

        if len(plan) == 1:
            ans.append(cnt)
            break

    return ans


# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.1MB)
# 테스트 3 〉	통과 (0.03ms, 10.1MB)
# 테스트 4 〉	통과 (0.02ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)
# 테스트 7 〉	통과 (0.03ms, 10.1MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	통과 (0.04ms, 10.3MB)
# 테스트 10 〉	통과 (0.03ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)