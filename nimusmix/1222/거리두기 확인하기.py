from itertools import combinations

def check(place):
    person = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                person.append((i, j))

    for combi in combinations(person, 2):
        si, sj = combi[0]
        vi, vj = combi[1]

        # 맨해튼 거리가 2 이하이면
        if abs(si - vi) + abs(sj - vj) <= 2:
            tmp = [i[min(sj, vj):max(sj, vj) + 1] for i in place[min(si, vi):max(si, vi) + 1]]
            for i in range(len(tmp)):
                for j in range(len(tmp[0])):
                    if tmp[i][j] == 'P':
                        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            mi, mj = i + di, j + dj
                            if 0 <= mi < len(tmp) and 0 <= mj < len(tmp[0]) and tmp[mi][mj] != 'X':
                                return 0
    return 1

def solution(places):
    ans = [0] * 5
    for i in range(5):
        ans[i] = check(places[i])
    return ans


# 테스트 1 〉	통과 (0.20ms, 10.3MB)
# 테스트 2 〉	통과 (0.10ms, 10.2MB)
# 테스트 3 〉	통과 (0.06ms, 10.2MB)
# 테스트 4 〉	통과 (0.06ms, 10.2MB)
# 테스트 5 〉	통과 (0.04ms, 10.2MB)
# 테스트 6 〉	통과 (0.04ms, 10.2MB)
# 테스트 7 〉	통과 (0.04ms, 10.2MB)
# 테스트 8 〉	통과 (0.06ms, 10.2MB)
# 테스트 9 〉	통과 (0.08ms, 10.3MB)
# 테스트 10 〉	통과 (0.05ms, 10.3MB)
# 테스트 11 〉	통과 (0.09ms, 10.1MB)
# 테스트 12 〉	통과 (0.04ms, 10.3MB)
# 테스트 13 〉	통과 (0.05ms, 10.2MB)
# 테스트 14 〉	통과 (0.04ms, 10.4MB)
# 테스트 15 〉	통과 (0.06ms, 10.2MB)
# 테스트 16 〉	통과 (0.06ms, 10.2MB)
# 테스트 17 〉	통과 (0.05ms, 10.4MB)
# 테스트 18 〉	통과 (0.05ms, 10.3MB)
# 테스트 19 〉	통과 (0.04ms, 10.3MB)
# 테스트 20 〉	통과 (0.07ms, 10.3MB)
# 테스트 21 〉	통과 (0.05ms, 10.1MB)
# 테스트 22 〉	통과 (0.05ms, 10.3MB)
# 테스트 23 〉	통과 (0.03ms, 10.2MB)
# 테스트 24 〉	통과 (0.04ms, 10.2MB)
# 테스트 25 〉	통과 (0.02ms, 10.2MB)
# 테스트 26 〉	통과 (0.02ms, 10.1MB)
# 테스트 27 〉	통과 (0.05ms, 10.2MB)
# 테스트 28 〉	통과 (0.03ms, 10.3MB)
# 테스트 29 〉	통과 (0.03ms, 10.3MB)
# 테스트 30 〉	통과 (0.03ms, 10.3MB)
# 테스트 31 〉	통과 (0.05ms, 10.2MB)