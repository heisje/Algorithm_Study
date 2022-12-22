import heapq

def solution(jobs):
    answer = 0

    request = -1    # 요청이 들어오는 기준시간
    now = 0         # 현재 시간
    cnt = 0         # 완료된 작업의 수

    controller = []

    # 모든 작업이 끝나기 전 까지 (cnt가 jobs의 갯수만큼 되기 전까지)
    # 한 작업이 끝날 때 마다 시간은 소요되고, 새로운 작업이 요청이 되므로 한 작업이 끝날 때 마다 반복.
    while cnt != len(jobs):
        for job in jobs:
            if request < job[0] <= now:     # 이천 요청시간 부터 현재시간까지 (요청이 들어온 작업들)
                heapq.heappush(controller, (job[1], job[0])) # 최소힙을 이용하기 위해 작업소요시간을 앞에 두고 컨트롤러에 넣어준다.

        if controller:  # 현재 요청이 들어온 작업이 있다면
            job = heapq.heappop(controller) # 작업소요시간이 가장 작은 작업을 꺼낸다.

            request = now                   # 다음 요청 시간이 될 시간을 저장해둔다.
            now += job[0]                   # 꺼낸 작업이 끝난 후 현재 시간을 저장해둔다.
            answer += now - job[1]          # answer에 해당 작업의 요청부터 종료까지 걸린시간을 더해준다.

            cnt += 1                        # 완료된 작업 수 + 1

        else:                               # 요청된 작업이 없다면
            now += 1                        # 현재 시간을 + 1 해서 작업이 요청되길 기다린다.


    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))


'''
테스트 1 〉	통과 (13.49ms, 10.4MB)
테스트 2 〉	통과 (14.31ms, 9.98MB)
테스트 3 〉	통과 (12.80ms, 10.2MB)
테스트 4 〉	통과 (10.00ms, 10.4MB)
테스트 5 〉	통과 (14.39ms, 10.4MB)
테스트 6 〉	통과 (0.13ms, 10.3MB)
테스트 7 〉	통과 (5.68ms, 10.1MB)
테스트 8 〉	통과 (5.31ms, 10.1MB)
테스트 9 〉	통과 (1.14ms, 10.1MB)
테스트 10 〉	통과 (20.86ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.4MB)
테스트 12 〉	통과 (0.02ms, 10MB)
테스트 13 〉	통과 (0.03ms, 10MB)
테스트 14 〉	통과 (0.03ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.1MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)
테스트 17 〉	통과 (0.01ms, 10.1MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
'''