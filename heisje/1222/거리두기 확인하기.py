# https://school.programmers.co.kr/learn/courses/30/lessons/81302
from collections import deque

d_x = (0, 0, -1, 1)
d_y = (-1, 1, 0, 0)

def solution(places):
    answer = []
    # p위치 찾기
    
    for place in places:
        # p의 위치를 찾자
        p_points = []
        print(place)
        for y in range(5):
            for x in range(5):
                if place[y][x] == 'P':
                    p_points.append((x, y))
        
        flag = False # 틀린걸 찾았는지 확인
        visited = [[0 for _ in range(5)] for _ in range(5)]
        # p마다 bfs를 돌려보자
        for p_x, p_y in p_points:
            dq = deque()
            dq.append((p_x, p_y, 1))
            visited[p_y][p_x] = 1
            while dq:
                print(visited, dq)
                x, y, value = dq.popleft()
                for d_x, d_y in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                    go_x = x + d_x
                    go_y = y + d_y
                    # 바깥, 벽 예외처리
                    if 0 <= go_x < 5 and 0 <= go_y < 5 and place[go_y][go_x] != 'X':
                        # 빈공간일 때
                        if place[go_y][go_x] == "O" and visited[go_y][go_x] == 0:
                            if value <= 1:
                                dq.append((go_x, go_y, value + 1))
                                visited[go_y][go_x] = value + 1
                        # 사람일 때
                        if place[go_y][go_x] == "P" and visited[go_y][go_x] == 0:
                            print('찾았다!', go_x, go_y )
                            flag = True
                            break
                if flag:
                    break
            if flag:
                break
        # 찾으면 0, 없으면 1
        if flag:
            answer.append(0)
        else:
            answer.append(1)
    return answer


a = [
    ["POOOP", 
     "OXXOX", 
     "OPXPX", 
     "OOXOX", 
     "POXXP"], 

    ["POOPX", 
     "OXPXP", 
     "PXXXO", 
     "OXXXO", 
     "OOOPP"], 

    ["PXOPX", 
     "OXOXP", 
     "OXPOX", 
     "OXXOP", 
     "PXPOX"], 

    ["OOOXX", 
     "XOOOX", 
     "OOOXX", 
     "OXOOX", 
     "OOOOO"], 

    ["PXPXP", 
     "XPXPX", 
     "PXPXP", 
     "XPXPX", 
     "PXPXP"]
]
print(solution(a))


# 테스트 1 〉	통과 (0.25ms, 10.2MB)
# 테스트 2 〉	통과 (0.11ms, 10.2MB)
# 테스트 3 〉	통과 (0.22ms, 10.3MB)
# 테스트 4 〉	통과 (0.09ms, 10.3MB)
# 테스트 5 〉	통과 (0.10ms, 10.3MB)
# 테스트 6 〉	통과 (0.15ms, 10.4MB)
# 테스트 7 〉	통과 (0.18ms, 10.3MB)
# 테스트 8 〉	통과 (0.15ms, 10.3MB)
# 테스트 9 〉	통과 (0.14ms, 10.3MB)
# 테스트 10 〉	통과 (0.17ms, 10.2MB)
# 테스트 11 〉	통과 (0.12ms, 10.4MB)
# 테스트 12 〉	통과 (0.11ms, 10.4MB)
# 테스트 13 〉	통과 (0.14ms, 10.4MB)
# 테스트 14 〉	통과 (0.18ms, 10.3MB)
# 테스트 15 〉	통과 (0.08ms, 10.3MB)
# 테스트 16 〉	통과 (0.12ms, 10.3MB)
# 테스트 17 〉	통과 (0.12ms, 10.4MB)
# 테스트 18 〉	통과 (0.11ms, 10.3MB)
# 테스트 19 〉	통과 (0.14ms, 10.4MB)
# 테스트 20 〉	통과 (0.12ms, 10.2MB)
# 테스트 21 〉	통과 (0.09ms, 10.3MB)
# 테스트 22 〉	통과 (0.11ms, 10.3MB)
# 테스트 23 〉	통과 (0.04ms, 10.4MB)
# 테스트 24 〉	통과 (0.08ms, 10.3MB)
# 테스트 25 〉	통과 (0.04ms, 10.3MB)
# 테스트 26 〉	통과 (0.04ms, 10.3MB)
# 테스트 27 〉	통과 (0.19ms, 10.3MB)
# 테스트 28 〉	통과 (0.11ms, 10.3MB)
# 테스트 29 〉	통과 (0.14ms, 10.2MB)
# 테스트 30 〉	통과 (0.08ms, 10.3MB)
# 테스트 31 〉	통과 (0.15ms, 10.4MB)