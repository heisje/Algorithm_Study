# https://school.programmers.co.kr/learn/courses/30/lessons/42627
import heapq

def solution(jobs):
    jobs.sort(key=lambda x:x[0], reverse=True)
    
    wait = []
    time = 0
    responsed_li = []
    while jobs or wait:
        # 하드디스크가 비어있을 때 가장 먼저 요청이 들어온 작업을 찾는다.
        if not wait and jobs:
            job = jobs.pop()
            request_time, spend_time = job
            heapq.heappush(wait, (spend_time, request_time))
            # 요청이 여러개일 경우 wait에 누적시킨다.
        
            while jobs and (jobs[-1][0] <= time or jobs[-1][0] == job[0]):
                request_time, spend_time = jobs.pop()
                heapq.heappush(wait, (spend_time, request_time))
        
        # 하드디스크가 비어있지 않을 때 (9번 오류처리)
        elif wait and jobs:
            while jobs and (jobs[-1][0] <= time):
                request_time, spend_time = jobs.pop()
                heapq.heappush(wait, (spend_time, request_time))
        # wait중 가장 소요 시간이 짧은 것을 처리한다.
        spend_time, request_time = heapq.heappop(wait)
            # 시간을 맞춰주고
        if time < request_time:
            time = request_time
        time += spend_time
            # 평균을 내기 위해 총 응답시간을 넣어준다.
        responsed_li.append(time-request_time)
    answer = sum(responsed_li) // len(responsed_li)
    return answer

print(solution([[0, 3], [1, 9], [2, 6]]))


# 테스트 1 〉	통과 (0.44ms, 9.98MB)
# 테스트 2 〉	통과 (0.37ms, 10.4MB)
# 테스트 3 〉	통과 (0.45ms, 10.2MB)
# 테스트 4 〉	통과 (0.32ms, 10.4MB)
# 테스트 5 〉	통과 (0.41ms, 10.1MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.29ms, 10.2MB)
# 테스트 8 〉	통과 (0.25ms, 10.3MB)
# 테스트 9 〉	통과 (0.16ms, 10.2MB)
# 테스트 10 〉	통과 (0.46ms, 10.3MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
# 테스트 12 〉	통과 (0.01ms, 10.3MB)
# 테스트 13 〉	통과 (0.02ms, 9.98MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.2MB)
# 테스트 16 〉	통과 (0.01ms, 10.3MB)
# 테스트 17 〉	통과 (0.01ms, 10.2MB)
# 테스트 18 〉	통과 (0.01ms, 10.3MB)
# 테스트 19 〉	통과 (0.01ms, 10.1MB)
# 테스트 20 〉	통과 (0.01ms, 10.1MB)