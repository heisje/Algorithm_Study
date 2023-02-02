def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()

    bus_time = {}
    for i in range(n):
        bus_time[9*60 + t*i] = []

    key_list = list(bus_time.keys())

    for i in range(len(timetable)):


        if len(bus_time[key_list[-1]]) == m:
            break

        temp = timetable[i]
        hour = int(temp[:2]) * 60
        minute = int(temp[3:])
        time = hour + minute

        if key_list[-1] < time:
            break

        for j in range(len(key_list)):
            if key_list[j] < time:
                continue
            else:
                if len(bus_time[key_list[j]]) < m :
                    bus_time[key_list[j]].append(time)
                    break
                else:
                    continue

    if len(bus_time[key_list[-1]]) < m:
        hourstring = str(key_list[-1] // 60)
        minutestring = str(key_list[-1] % 60)
        if len(hourstring) == 1:
            hourstring = "0" + hourstring
        if len(minutestring) == 1:
            minutestring = "0" + minutestring
        answer = hourstring + ":" + minutestring
    else:
        hourstring = str((bus_time[key_list[-1]][-1] - 1) // 60)
        minutestring = str((bus_time[key_list[-1]][-1] - 1) % 60)
        if len(hourstring) == 1:
            hourstring = "0" + hourstring
        if len(minutestring) == 1:
            minutestring = "0" + minutestring
        answer = hourstring + ":" + minutestring
    print(bus_time)
    return answer


"""
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.5MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.05ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.70ms, 10.5MB)
테스트 8 〉	통과 (0.03ms, 10.5MB)
테스트 9 〉	통과 (0.02ms, 10.4MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
테스트 11 〉	통과 (0.03ms, 10.4MB)
테스트 12 〉	통과 (1.34ms, 10.4MB)
테스트 13 〉	통과 (0.67ms, 10.5MB)
테스트 14 〉	통과 (0.09ms, 10.4MB)
테스트 15 〉	통과 (0.27ms, 10.4MB)
테스트 16 〉	통과 (0.24ms, 10.4MB)
테스트 17 〉	통과 (1.20ms, 10.5MB)
테스트 18 〉	통과 (0.46ms, 10.3MB)
테스트 19 〉	통과 (0.47ms, 10.4MB)
테스트 20 〉	통과 (0.46ms, 10.4MB)
테스트 21 〉	통과 (0.92ms, 10.5MB)
테스트 22 〉	통과 (0.53ms, 10.3MB)
테스트 23 〉	통과 (0.56ms, 10.3MB)
테스트 24 〉	통과 (0.89ms, 10.3MB)
"""