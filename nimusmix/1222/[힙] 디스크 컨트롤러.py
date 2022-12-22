import heapq

def solution(jobs):
    jobs.sort()
    start = end = time_sum = 0
    done = []
    
    while len(done) < len(jobs):
        wait = []
        for request, taken in jobs:
            if (taken, request) not in done:
                if request >= end:
                    if not wait:
                        start = request
                        end = request + taken
                        time_sum += taken
                        done.append((taken, request))
                        break
                else:
                    heapq.heappush(wait, (taken, request))
 
        if wait:
            t, r = heapq.heappop(wait)
            start = end
            end = end + t
            time_sum += (start - r) + t
            done.append((t, r))
    return time_sum // len(jobs)


# 테스트 1 〉	통과 (614.86ms, 10.1MB)
# 테스트 2 〉	통과 (414.84ms, 10.3MB)
# 테스트 3 〉	통과 (250.45ms, 10.4MB)
# 테스트 4 〉	통과 (360.90ms, 10.3MB)
# 테스트 5 〉	통과 (567.21ms, 10.1MB)
# 테스트 6 〉	통과 (0.09ms, 10.2MB)
# 테스트 7 〉	통과 (184.25ms, 10.2MB)
# 테스트 8 〉	통과 (100.76ms, 10.2MB)
# 테스트 9 〉	통과 (6.64ms, 10.2MB)
# 테스트 10 〉	통과 (1071.25ms, 10.3MB)
# 테스트 11 〉	통과 (0.03ms, 10.1MB)
# 테스트 12 〉	통과 (0.05ms, 10.3MB)
# 테스트 13 〉	통과 (0.05ms, 10.3MB)
# 테스트 14 〉	통과 (0.02ms, 10.3MB)
# 테스트 15 〉	통과 (0.02ms, 10.1MB)
# 테스트 16 〉	통과 (0.01ms, 10.4MB)
# 테스트 17 〉	통과 (0.01ms, 10.2MB)
# 테스트 18 〉	통과 (0.01ms, 10.4MB)
# 테스트 19 〉	통과 (0.01ms, 10.2MB)
# 테스트 20 〉	통과 (0.00ms, 10.3MB)

print(solution([[0, 3], [1, 9], [2, 6]]))