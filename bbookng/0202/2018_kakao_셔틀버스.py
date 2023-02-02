def solution(n, t, m, timetable):
    start = 540
    departs = []
    # 출발 시간 departs에 저장
    for i in range(n):
        departs.append(start + t * i)

    # timetable을 분단위로 바꾸어서 다시 저장
    timetable = sorted(list(map(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]), timetable)), reverse=True)

    # 출발 시간마다,
    for depart in departs:
        # 타는 사람 초기화
        num = 0

        # 아직 탈 사람이 남아있고, 사람이 m보다 적고, 승차시간보다 출발 시간이 크거나 같으면
        while timetable and num < m and timetable[-1] <= depart:
            # 그사람의 승차 시간이  마지막 승차 가능 시간
            last = timetable.pop()
            # 탑승자 한명 추가
            num += 1

    # 만약 버스 출발 시간 다 돌고 나서 사람 수가 m과 같다면
    if num == m:
        # 내가 마지막 사람보다는 1분 일찍 와야함
        result = last - 1
        return str(result//60).zfill(2)+':'+str(result%60).zfill(2)

    # 만약 탑승자 수가 m보다 작다면, 제일 마지막 출발 시간에 도착하면 된다.
    result = departs[-1]
    return str(result//60).zfill(2)+':'+str(result%60).zfill(2)


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))


'''
테스트 1 〉	통과 (0.04ms, 10.5MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.73ms, 10.4MB)
테스트 8 〉	통과 (0.03ms, 10.4MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.04ms, 10.4MB)
테스트 11 〉	통과 (0.05ms, 10.4MB)
테스트 12 〉	통과 (0.49ms, 10.4MB)
테스트 13 〉	통과 (0.66ms, 10.5MB)
테스트 14 〉	통과 (0.06ms, 10.2MB)
테스트 15 〉	통과 (0.10ms, 10.4MB)
테스트 16 〉	통과 (0.26ms, 10.3MB)
테스트 17 〉	통과 (0.32ms, 10.4MB)
테스트 18 〉	통과 (0.35ms, 10.4MB)
테스트 19 〉	통과 (0.53ms, 10.5MB)
테스트 20 〉	통과 (0.31ms, 10.2MB)
테스트 21 〉	통과 (1.83ms, 10.5MB)
테스트 22 〉	통과 (0.48ms, 10.5MB)
테스트 23 〉	통과 (0.30ms, 10.4MB)
테스트 24 〉	통과 (1.51ms, 10.4MB)
'''