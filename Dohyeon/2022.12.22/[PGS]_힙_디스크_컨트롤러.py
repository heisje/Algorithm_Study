def solution(jobs):
    total_time = 0
    now = 0
    total_jobs = len(jobs)
    jobs = sorted(jobs, key=lambda x: x[1])  # 빨리끝나는 것부터 처리하자

    while len(jobs) > 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= now:            # 남아있는 것 중 시작할 수 있는것이라면
                now += jobs[i][1]
                total_time += now - jobs[i][0]
                jobs.pop(i)
                break

            if i == len(jobs) - 1:
                now += 1

    return total_time // total_jobs

"""
테스트 1 〉	통과 (0.65ms, 10.2MB)
테스트 2 〉	통과 (0.53ms, 10MB)
테스트 3 〉	통과 (0.37ms, 10.2MB)
테스트 4 〉	통과 (0.27ms, 10.2MB)
테스트 5 〉	통과 (0.66ms, 10.1MB)
테스트 6 〉	통과 (0.09ms, 10.1MB)
테스트 7 〉	통과 (0.66ms, 10.2MB)
테스트 8 〉	통과 (0.76ms, 10.2MB)
테스트 9 〉	통과 (0.85ms, 10.1MB)
테스트 10 〉	통과 (0.80ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.1MB)
테스트 12 〉	통과 (0.04ms, 10.3MB)
테스트 13 〉	통과 (0.02ms, 10.1MB)
테스트 14 〉	통과 (0.04ms, 10.3MB)
테스트 15 〉	통과 (0.03ms, 10MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.02ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.3MB)
"""