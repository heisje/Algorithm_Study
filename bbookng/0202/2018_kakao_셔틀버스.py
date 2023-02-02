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