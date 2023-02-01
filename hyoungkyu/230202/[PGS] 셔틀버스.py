def formatting(hour, minute):
    if 0 < int(minute) <= 10:
        if 0 < int(hour) < 10:
            return "0"+str(int(hour))+":0"+str(int(minute)-1)
        else:
            return hour+":0"+str(int(minute)-1)
    elif int(minute) == 0:
        if 0 < int(hour) <= 10:
            return "0"+str(int(hour)-1)+":59"
        else:
            return str(int(hour)-1)+":59"
    else:
        return hour+":"+str(int(minute)-1)

def solution(n, t, m, timetable):
    cnt_n = 1                           # 버스 지나간 수
    cnt_m = 0                           # 현재 버스 인원 수 체크
    end_time = 540+t*(n-1)              # 막차 시간
    
    timetable.sort()
    i = 0
    
    while i < len(timetable):
        hour, minute = timetable[i].split(":")
        minutes = int(hour)*60 + int(minute)    # 승객의 탑승 시간
        current_bus = 540+t*(cnt_n-1)           # 현재 버스 시간
        
        # 탑승 가능한 경우
        if current_bus >= minutes:
            
            # 남은 버스가 없고 인원수 다 찰 경우
            if cnt_m + 1 == m and cnt_n == n:                
                return formatting(hour, minute)
            
            # 막차를 타야만하는 경우1 : 남은 크루가 있지만 막차 시간보다 늦게 올 경우
            if minutes > end_time:
                return formatting(str(end_time//60), str(end_time%60+1))
            
            i += 1
            cnt_m += 1
            if cnt_m == m:
                cnt_m = 0
                cnt_n += 1
        
        # 해당 버스시간을 놓친 경우
        else:
            cnt_n += 1          # 다음 버스 ㄱ
            cnt_m = 0
        
        # 막차를 타야만하는 경우2 : 마지막 버스가 다 찰 경우
        if cnt_n > n:
            return formatting(str(end_time//60), str(end_time%60+1))
    
    # 막차를 타야만하는 경우3 : 모든 크루들이 다 탔을 경우
    return formatting(str(end_time//60), str(end_time%60+1))

'''
정확성  테스트
테스트 1 〉통과 (0.03ms, 10.3MB)
테스트 2 〉통과 (0.03ms, 10.3MB)
테스트 3 〉통과 (0.02ms, 10.5MB)
테스트 4 〉통과 (0.04ms, 10.4MB)
테스트 5 〉통과 (0.04ms, 10.5MB)
테스트 6 〉통과 (0.04ms, 10.3MB)
테스트 7 〉통과 (0.55ms, 10.5MB)
테스트 8 〉통과 (0.03ms, 10.4MB)
테스트 9 〉통과 (0.02ms, 10.5MB)
테스트 10 〉통과 (0.03ms, 10.3MB)
테스트 11 〉통과 (0.04ms, 10.5MB)
테스트 12 〉통과 (0.34ms, 10.5MB)
테스트 13 〉통과 (0.54ms, 10.4MB)
테스트 14 〉통과 (0.09ms, 10.4MB)
테스트 15 〉통과 (0.18ms, 10.5MB)
테스트 16 〉통과 (0.14ms, 10.4MB)
테스트 17 〉통과 (0.30ms, 10.5MB)
테스트 18 〉통과 (0.30ms, 10.5MB)
테스트 19 〉통과 (0.43ms, 10.5MB)
테스트 20 〉통과 (0.36ms, 10.6MB)
테스트 21 〉통과 (0.84ms, 10.4MB)       *
테스트 22 〉통과 (0.44ms, 10.4MB)
테스트 23 〉통과 (0.25ms, 10.5MB)
테스트 24 〉통과 (0.71ms, 10.4MB)
'''