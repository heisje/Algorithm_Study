# Lv2
def solution(m, musicinfos):
    # musicinfos : "시작한 시각, 끝난 시각, 음악 제목, 악보 정보"
    answer = '(None)'
    musicinfo_list = []
    for i in musicinfos:
        lst = list(i.split(","))
        musicinfo_list.append(lst)              # 곡 정보 리스트화
    
    def getTime(st, et):                        # 재생 시간 구하는 함수
        st_h, st_m = map(int, st.split(":"))
        et_h, et_m = map(int, et.split(":"))
        minute = (et_h-st_h) * 60
        if et_h - st_h >= 0:                    # 이 부분 실수 때문에 2시간 날림ㅠㅠ
            minute += et_m - st_m
        else:
            minute -= et_m - st_m
        return minute

    def changeStr(s):                           # 플랫을 소문자로
        result = ""
        i = 1
        while i < len(s):
            if s[i] == "#":
                result += s[i-1].lower()
                i += 2
            else:
                result += s[i-1]
                i += 1
        if s[-1] != "#":
            result += s[-1]
        return result
    
    m = changeStr(m)
    result = []
    for info in musicinfo_list:
        title = changeStr(info[2])
        song = changeStr(info[3])
        time = getTime(info[0], info[1])
        # print(time, m, title, song)
        if len(song) > time:                    # 재생시간 < 곡 시간
            if time - len(m) < 0:
                continue
            for i in range(time-len(m)+1):      # 브루트포스
                for j in range(len(m)):
                    if song[(i+j)%len(song)] != m[j]:
                        break
                else:
                    if not result:
                        result = [title, time]
                    elif result[1] < time:
                        result = [title, time]
                    break
        else:                                   # 재생새긴 >= 곡 시간
            if time+(len(song)-(time%len(song)))-len(m) < 0:
                continue
            for i in range(time+(len(song)-(time%len(song)))-len(m)+1):
                for j in range(len(m)):
                    if song[(i+j)%len(song)] != m[j]:
                        break
                else:
                    if not result:
                        result = [title, time]
                    elif result[1] < time:
                        result = [title, time]
                    break

    if result:
        answer = result[0]
    return answer

'''
테스트 1 〉통과 (0.04ms, 10.5MB)
테스트 2 〉통과 (0.06ms, 10.4MB)
테스트 3 〉통과 (0.04ms, 10.5MB)
테스트 4 〉통과 (0.04ms, 10.4MB)
테스트 5 〉통과 (0.04ms, 10.4MB)
테스트 6 〉통과 (0.05ms, 10.4MB)
테스트 7 〉통과 (0.99ms, 10.5MB)
테스트 8 〉통과 (1.12ms, 10.4MB)
테스트 9 〉통과 (1.06ms, 10.4MB)
테스트 10 〉통과 (0.41ms, 10.4MB)
테스트 11 〉통과 (1.03ms, 10.5MB)
테스트 12 〉통과 (1.06ms, 10.4MB)
테스트 13 〉통과 (1.07ms, 10.4MB)
테스트 14 〉통과 (1.25ms, 10.4MB)
테스트 15 〉통과 (1.12ms, 10.4MB)
테스트 16 〉통과 (0.71ms, 10.4MB)
테스트 17 〉통과 (1.12ms, 10.4MB)
테스트 18 〉통과 (1.07ms, 10.4MB)
테스트 19 〉통과 (0.67ms, 10.5MB)
테스트 20 〉통과 (0.55ms, 10.4MB)
테스트 21 〉통과 (1.08ms, 10.4MB)
테스트 22 〉통과 (1.02ms, 10.4MB)
테스트 23 〉통과 (1.14ms, 10.5MB)
테스트 24 〉통과 (1.02ms, 10.4MB)
테스트 25 〉통과 (0.06ms, 10.4MB)
테스트 26 〉통과 (0.08ms, 10.4MB)
테스트 27 〉통과 (0.06ms, 10.4MB)
테스트 28 〉통과 (0.07ms, 10.4MB)
테스트 29 〉통과 (11.89ms, 10.5MB)  #
테스트 30 〉통과 (11.31ms, 10.4MB)
'''