from collections import deque

def check(place):
    # 참가자들 좌표 담기
    partitions = [(i, j, 0) for i in range(5) for j in range(5) if place[i][j] == 'P']

    # 참가자 마다 반복
    for partition in partitions:
        q = deque([partition])
        visited = [[0] * 5 for _ in range(5)]

        while q:
            x, y, d = q.popleft()
            visited[x][y] = 1

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny, nd = x + dx, y + dy, d + 1

                # 범위 내에 있고 방문하지 않았을 때,
                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                    # 참가자인데 맨해튼거리 2이하라면 0을 return
                    if place[nx][ny] == 'P' and nd <= 2:
                        return 0
                    # 빈 공간이고 거리가 1일 때 더 탐색 / 파티션이면 막히고, 1이상이면 거리두기 조건 충족했기 때문에.
                    elif place[nx][ny] == 'O' and nd == 1:
                        q.append((nx, ny, nd))
                        visited[nx][ny] = 1
    return 1

def solution(places):
    answer = []

    for place in places:
        answer.append(check(place))

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

'''
테스트 1 〉	통과 (0.11ms, 10.3MB)
테스트 2 〉	통과 (0.06ms, 10.1MB)
테스트 3 〉	통과 (0.06ms, 10.1MB)
테스트 4 〉	통과 (0.09ms, 10.3MB)
테스트 5 〉	통과 (0.08ms, 10.2MB)
테스트 6 〉	통과 (0.12ms, 10.1MB)
테스트 7 〉	통과 (0.06ms, 10.2MB)
테스트 8 〉	통과 (0.07ms, 10.3MB)
테스트 9 〉	통과 (0.07ms, 10.2MB)
테스트 10 〉	통과 (0.08ms, 10.3MB)
테스트 11 〉	통과 (0.06ms, 10.1MB)
테스트 12 〉	통과 (0.10ms, 10.2MB)
테스트 13 〉	통과 (0.06ms, 10.3MB)
테스트 14 〉	통과 (0.08ms, 10.1MB)
테스트 15 〉	통과 (0.07ms, 10.2MB)
테스트 16 〉	통과 (0.06ms, 10.1MB)
테스트 17 〉	통과 (0.06ms, 10.4MB)
테스트 18 〉	통과 (0.09ms, 10.3MB)
테스트 19 〉	통과 (0.08ms, 10.3MB)
테스트 20 〉	통과 (0.07ms, 10.1MB)
테스트 21 〉	통과 (0.05ms, 10.1MB)
테스트 22 〉	통과 (0.06ms, 10.3MB)
테스트 23 〉	통과 (0.02ms, 10.4MB)
테스트 24 〉	통과 (0.04ms, 10.3MB)
테스트 25 〉	통과 (0.02ms, 10.1MB)
테스트 26 〉	통과 (0.02ms, 10.3MB)
테스트 27 〉	통과 (0.05ms, 10MB)
테스트 28 〉	통과 (0.05ms, 10.2MB)
테스트 29 〉	통과 (0.09ms, 10.3MB)
테스트 30 〉	통과 (0.04ms, 10.2MB)
테스트 31 〉	통과 (0.07ms, 10.3MB)
'''