# Lv3 / Heap
def solution(jobs):
    jobs.sort()
    answer = 0
    length = len(jobs)
    
    # 매번 기다리는 큐에서 소요시간이 젤 적을걸 빼는 방식
    current_time = jobs[0][0]+jobs[0][1]
    tot_time = jobs[0][1]
    jobs.pop(0)
    while jobs:
        waiting = []
        for idx in range(len(jobs)):
            if jobs[idx][0] <= current_time:
                waiting.append([jobs[idx][1], idx])
            else:
                break
        if not waiting:
            current_time += (jobs[0][0]-current_time)+jobs[0][1]
            tot_time += jobs[0][1]
            jobs.pop(0)
        else:
            waiting.sort()
            idx = waiting[0][1]
            current_time += jobs[idx][1]
            tot_time += current_time-jobs[idx][0]
            jobs.pop(idx)
            
    answer = tot_time//length
    return answer

'''
테스트 1 〉통과 (38.77ms, 10.4MB)
테스트 2 〉통과 (29.63ms, 10.3MB)
테스트 3 〉통과 (19.97ms, 10.4MB)
테스트 4 〉통과 (20.53ms, 10.2MB)
테스트 5 〉통과 (33.68ms, 10.4MB)
테스트 6 〉통과 (0.08ms, 10.2MB)
테스트 7 〉통과 (16.23ms, 10.2MB)
테스트 8 〉통과 (9.82ms, 10.4MB)
테스트 9 〉통과 (1.42ms, 10.2MB)
테스트 10 〉통과 (44.28ms, 10.3MB)
테스트 11 〉통과 (0.03ms, 10.2MB)
테스트 12 〉통과 (0.04ms, 10.2MB)
테스트 13 〉통과 (0.04ms, 10.2MB)
테스트 14 〉통과 (0.02ms, 10.3MB)
테스트 15 〉통과 (0.02ms, 10.2MB)
테스트 16 〉통과 (0.02ms, 10.3MB)
테스트 17 〉통과 (0.02ms, 10.2MB)
테스트 18 〉통과 (0.02ms, 10.2MB)
테스트 19 〉통과 (0.02ms, 10.2MB)
테스트 20 〉통과 (0.01ms, 10.2MB)
'''