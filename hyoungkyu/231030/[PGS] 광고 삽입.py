# Lv3
def solution(play_time, adv_time, logs):
    answer = ''
    play_length = time_to_second(play_time)+1
    adv_length = time_to_second(adv_time)
    DP = [0] * play_length
    
    # 이거 예전에 터렛 문제였나 풀었던 방식
    for log in logs:
        start, end = log.split("-")
        DP[time_to_second(start)] += 1
        DP[time_to_second(end)] -= 1
        
    for i in range(1, play_length):
        DP[i] = DP[i-1] + DP[i]
    
    answer = sliding_window(DP, play_length, adv_length)
    
    return answer

def sliding_window(DP, play_length, adv_length):
    # 처음 윈도우 내 총합 구하기
    watching_time = 0
    for i in range(adv_length):
        watching_time += DP[i]
        
    max_time = watching_time
    max_idx = 0
    # 윈도우 움직이면서 총합 바꾸기
    for i in range(1, play_length - adv_length):
        watching_time += DP[i+adv_length] - DP[i]
        if max_time < watching_time:    # 시간이 같은 경우 빠른걸 뽑으면 되니까 <= 대신 < 사용
            max_time = watching_time
            max_idx = i+1
            # ex) [0, 0, 1, 1, 1, 1, ...] -> i == 1인 경우 window가 2부터 시작이므로 +1 해줘야 됨!
            
    return second_to_time(max_idx)

def time_to_second(time):
    return int(time[:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:])

def second_to_time(second):
    s = ""
    if second // 3600 < 10:
        s += f'0{second // 3600}:'
    else:
        s += f'{second // 3600}:'
    second %= 3600
    if second // 60 < 10:
        s += f'0{second // 60}:'
    else:
        s += f'{second // 60}:'
    second %= 60
    if second < 10:
        s += f'0{second}'
    else:
        s += f'{second}'
    return s

'''
정확성  테스트
테스트 1 〉	통과 (1.63ms, 10.5MB)
테스트 2 〉	통과 (7.64ms, 10.6MB)
테스트 3 〉	통과 (16.81ms, 10.9MB)
테스트 4 〉	통과 (173.07ms, 26.9MB)
테스트 5 〉	통과 (246.65ms, 21.5MB)
테스트 6 〉	통과 (92.02ms, 12.9MB)
테스트 7 〉	통과 (468.17ms, 41.2MB)
테스트 8 〉	통과 (473.06ms, 41.1MB)
테스트 9 〉	통과 (696.85ms, 49.5MB)
테스트 10 〉	통과 (704.23ms, 49.7MB)
테스트 11 〉	통과 (657.88ms, 49.7MB)
테스트 12 〉	통과 (606.20ms, 40.9MB)
테스트 13 〉	통과 (675.39ms, 49.6MB)
테스트 14 〉	통과 (477.87ms, 40.8MB)
테스트 15 〉	통과 (38.01ms, 11.1MB)
테스트 16 〉	통과 (544.04ms, 40.9MB)
테스트 17 〉	통과 (731.64ms, 49.6MB)
테스트 18 〉	통과 (555.44ms, 41MB)
테스트 19 〉	통과 (2.44ms, 10.4MB)
테스트 20 〉	통과 (1.02ms, 10.6MB)
테스트 21 〉	통과 (155.56ms, 20.3MB)
테스트 22 〉	통과 (148.38ms, 20.3MB)
테스트 23 〉	통과 (629.94ms, 44.6MB)
테스트 24 〉	통과 (587.19ms, 40.9MB)
테스트 25 〉	통과 (62.08ms, 12.4MB)
테스트 26 〉	통과 (41.75ms, 11.6MB)
테스트 27 〉	통과 (46.82ms, 11.9MB)
테스트 28 〉	통과 (43.68ms, 11.9MB)
테스트 29 〉	통과 (43.76ms, 11.8MB)
테스트 30 〉	통과 (35.08ms, 11.3MB)
테스트 31 〉	통과 (38.33ms, 11.6MB)
'''