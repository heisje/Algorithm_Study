import heapq

def solution(lines):
    answer = 1
    log_list = []

    for line in lines:
        date, s, t = line.split()
        h, m, s = map(float, s.split(':'))

        end_date = int(h * 3600 * 1000) + int(m * 60 * 1000) + int(s * 1000)
        start_date = end_date - int(float(t.replace('s', '')) * 1000) + 1

        log_list.append([start_date, end_date])

    log_list.sort(key=lambda x: x[0])

    arr = []

    # 시작 시간이 앞 로그의 종료 시간보다 작거나 같을 때 겹침
    for log in log_list:
        std = log[0]

        while arr:
            if std - 1000 >= arr[0][1][1]:
                heapq.heappop(arr)
            else:
                break
        heapq.heappush(arr, (log[1], log))
        answer = max(answer, len(arr))

    return answer

print(solution( [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))

'''
테스트 1 〉	통과 (0.04ms, 10.1MB)
테스트 2 〉	통과 (2.71ms, 10.2MB)
테스트 3 〉	통과 (2.84ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.42ms, 10.3MB)
테스트 6 〉	통과 (0.23ms, 10.3MB)
테스트 7 〉	통과 (4.15ms, 10.2MB)
테스트 8 〉	통과 (2.41ms, 10.2MB)
테스트 9 〉	통과 (0.22ms, 9.99MB)
테스트 10 〉	통과 (0.05ms, 10MB)
테스트 11 〉	통과 (0.04ms, 10.3MB)
테스트 12 〉	통과 (2.25ms, 10.5MB)
테스트 13 〉	통과 (0.22ms, 10.3MB)
테스트 14 〉	통과 (0.02ms, 10.1MB)
테스트 15 〉	통과 (0.02ms, 10MB)
테스트 16 〉	통과 (0.02ms, 10.3MB)
테스트 17 〉	통과 (0.02ms, 10.2MB)
테스트 18 〉	통과 (5.10ms, 10.5MB)
테스트 19 〉	통과 (4.54ms, 10.3MB)
테스트 20 〉	통과 (4.68ms, 10.4MB)
테스트 21 〉	통과 (0.02ms, 10MB)
테스트 22 〉	통과 (0.01ms, 10MB)
'''