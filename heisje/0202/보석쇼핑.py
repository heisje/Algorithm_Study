from collections import deque

def solution(gems):
    # 모든 보석 찾기
    # 한 개를 지날 때 마다 visited에 인덱스를 추가함
    #
    # 시작점 끝점 구하는 법
    # 시작점을 저장하고, 
    #   다른것이 들어오면 
    #   일단 추가
    #   만약 중복을 찾을 시
    #   맨 앞에 중복이 위치한다면 맨앞을 한 칸뒤로
    #   맨앞이 중복이 없어질 떄 까지 추가
    #
    # 결과 찾기
    # visited가 전부 다 차면 
    #   최대 길이를 체크하고 
    #   시작점 끝 점을 넣는다
    jewelrys = dict()
    for gem in gems:
        jewelrys[gem] = deque()
    N = len(list(jewelrys))
    n = 0
    start = 0 # 시작점
    save = (len(gems), 0, 0) # 결과
    for idx, gem in enumerate(gems):
        jewelrys[gem].append(idx)
        # 중복이면
        if len(jewelrys[gem]) > 1:
            # start가 중복이면 start를 하나씩 미룬다.
            while len(jewelrys[gems[start]]) > 1:
                jewelrys[gems[start]].popleft()
                start += 1
        # 중복한 게 아니면 n + 1
        else:
            n += 1

        # 결과 체크
        if n == N and save[0] > idx-start:
            save = (idx-start, start+1, idx+1)
        
    return [save[1], save[2]]

a = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(a))
a = ["AA", "AB", "AC", "AA", "AC"]
a = ["XYZ", "XYZ", "XYZ"]
a = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.06ms, 10.3MB)
# 테스트 3 〉	통과 (0.19ms, 10.2MB)
# 테스트 4 〉	통과 (0.34ms, 10.5MB)
# 테스트 5 〉	통과 (0.57ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.3MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.41ms, 10.2MB)
# 테스트 9 〉	통과 (1.04ms, 10.4MB)
# 테스트 10 〉	통과 (1.01ms, 10.7MB)
# 테스트 11 〉	통과 (0.84ms, 10.6MB)
# 테스트 12 〉	통과 (0.92ms, 10.3MB)
# 테스트 13 〉	통과 (1.22ms, 10.3MB)
# 테스트 14 〉	통과 (2.69ms, 10.5MB)
# 테스트 15 〉	통과 (4.88ms, 10.4MB)
# 효율성  테스트
# 테스트 1 〉	통과 (3.22ms, 10.5MB)
# 테스트 2 〉	통과 (5.81ms, 11.4MB)
# 테스트 3 〉	통과 (9.56ms, 11MB)
# 테스트 4 〉	통과 (12.19ms, 15MB)
# 테스트 5 〉	통과 (17.01ms, 12.2MB)
# 테스트 6 〉	통과 (19.56ms, 12.2MB)
# 테스트 7 〉	통과 (22.30ms, 13.1MB)
# 테스트 8 〉	통과 (26.44ms, 13.3MB)
# 테스트 9 〉	통과 (30.48ms, 13.4MB)
# 테스트 10 〉	통과 (34.56ms, 13.7MB)
# 테스트 11 〉	통과 (42.72ms, 15.7MB)
# 테스트 12 〉	통과 (43.06ms, 22.1MB)
# 테스트 13 〉	통과 (53.30ms, 22.7MB)
# 테스트 14 〉	통과 (63.90ms, 17.3MB)
# 테스트 15 〉	통과 (72.38ms, 20.7MB)