from pprint import pprint

def convert_time(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s
def solution(play_time, adv_time, logs):
    answer = ''
    play_time = convert_time(play_time)
    adv_time = convert_time(adv_time)

    total = [0] * (play_time + 1)

    # 구간합 이용
    for log in logs:
        start, end = log.split('-')
        start, end = convert_time(start), convert_time(end)
        total[start] += 1
        total[end] -= 1

    for i in range(1, play_time):
        total[i] += total[i - 1]

    # 누적
    for i in range(1, play_time):
        total[i] += total[i - 1]

    max_view = 0
    std_time = 0

    for i in range(adv_time-1, play_time):
        if total[i] - total[i - adv_time] > max_view:
            max_view = total[i] - total[i - adv_time]
            std_time = i - adv_time + 1

    h = str(std_time // 3600).zfill(2)
    m = str(std_time % 3600 // 60).zfill(2)
    s = str(std_time % 60).zfill(2)

    return h + ':' + m + ':' + s

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))

'''
테스트 1 〉	통과 (3.24ms, 10.5MB)
테스트 2 〉	통과 (7.88ms, 10.7MB)
테스트 3 〉	통과 (16.39ms, 11.2MB)
테스트 4 〉	통과 (185.71ms, 27MB)
테스트 5 〉	통과 (332.63ms, 32.5MB)
테스트 6 〉	통과 (119.12ms, 21.4MB)
테스트 7 〉	통과 (428.09ms, 41.1MB)
테스트 8 〉	통과 (468.40ms, 45.9MB)
테스트 9 〉	통과 (572.56ms, 54.1MB)
테스트 10 〉	통과 (679.67ms, 54.5MB)
테스트 11 〉	통과 (627.94ms, 52MB)
테스트 12 〉	통과 (634.52ms, 49.5MB)
테스트 13 〉	통과 (613.61ms, 54.5MB)
테스트 14 〉	통과 (489.04ms, 40.7MB)
테스트 15 〉	통과 (41.91ms, 15MB)
테스트 16 〉	통과 (553.36ms, 40.7MB)
테스트 17 〉	통과 (749.52ms, 54.8MB)
테스트 18 〉	통과 (556.97ms, 42.2MB)
테스트 19 〉	통과 (2.68ms, 10.5MB)
테스트 20 〉	통과 (1.38ms, 10.3MB)
테스트 21 〉	통과 (158.14ms, 20.1MB)
테스트 22 〉	통과 (0.03ms, 20.2MB)
테스트 23 〉	통과 (609.57ms, 47.1MB)
테스트 24 〉	통과 (606.55ms, 40.9MB)
테스트 25 〉	통과 (101.85ms, 19.4MB)
테스트 26 〉	통과 (55.61ms, 14.6MB)
테스트 27 〉	통과 (113.03ms, 17.2MB)
테스트 28 〉	통과 (79.17ms, 16.6MB)
테스트 29 〉	통과 (61.50ms, 16.7MB)
테스트 30 〉	통과 (39.44ms, 14.2MB)
테스트 31 〉	통과 (42.99ms, 14.6MB)
'''