from itertools import permutations 

def solution(info, edges):
    nodes = [[] for _ in range(len(info))]
    reverses = [-1 for _ in range(len(info))]
    # 출발점 기준으로 노드변환
    for s, e in edges:
        nodes[s].append(e)
        reverses[e] = s

    # 들린 곳
    visited = [0 for _ in range(len(info))]
    visited[0] = 1
    sheep = 0 # 양 갯수
    wolf = 0 # 늑대 갯수

    schedule = []
    schedule.append(0)
    while schedule:
        pre = schedule.pop()

        # 방문 후 양이나 늑대 추가
        visited[pre] = 1
        if info[pre] == 0: 
            sheep += 1
        else:
            wolf += 1

        # 2단계 까지 노드 탐색
        for n in nodes[pre]:
            # 현재위치에서 양이 있는 곳으로 이동 후 전부 취득함
            if info[n] == 0:
                schedule.append(n)
            # 현재위치에서 늑대가 있는 곳으로 이동 후 양이 하나라도 있으면 들어가봄
            else:
                for node in nodes[n]:
                    if info[node] == 0:
                        schedule.append(n)
                        break
    
    # 이제 무차별 대입 예정
    # 양의 위치를 전부 구한다.
    s_points = []
    for idx, value in enumerate(info):
        if value == 0 and visited[idx] == 0:
            s_points.append(idx)
    
    # 모든 순열대로 올라가본다.
    max_t_sheep = sheep
    for li in permutations(s_points):

        # 기본 값
        t_sheep = sheep
        t_wolf = wolf
        end_trg = False
        t_visited = visited[:]

        for pre in li:
            # 방문한 곳까지 올려보낸다.
            go_li = []
            while t_visited[pre] == 0:
                go_li.append(pre)
                pre = reverses[pre]
            
            # 다시 내려보낸다.
            while go_li:
                pre = go_li.pop()
                # 양, 늑대 상태추가
                if info[pre] == 0:
                    t_sheep += 1

                if info[pre] == 1: 
                    t_wolf += 1
                    if t_wolf >= t_sheep:
                        end_trg = True
                        break
                
                t_visited[pre] = 1
                
            if end_trg:
                break
            if max_t_sheep < t_sheep:
                max_t_sheep = t_sheep
    
    return max_t_sheep


a = [0,0,1,1,1,0,1,0,1,0,1,1]
b = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

print(solution(a,b))

a = [0,1,0,1,1,0,1,0,0,1,0]
b = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

print(solution(a,b))

# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (1.75ms, 10.4MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.06ms, 10.3MB)
# 테스트 6 〉	통과 (0.01ms, 10.3MB)
# 테스트 7 〉	통과 (0.02ms, 10.4MB)
# 테스트 8 〉	통과 (0.11ms, 10.2MB)
# 테스트 9 〉	통과 (0.24ms, 10.2MB)
# 테스트 10 〉	통과 (0.03ms, 10.3MB)
# 테스트 11 〉	통과 (0.39ms, 10.2MB)
# 테스트 12 〉	통과 (0.23ms, 10.3MB)
# 테스트 13 〉	통과 (4.69ms, 10.2MB)
# 테스트 14 〉	통과 (0.35ms, 10.3MB)
# 테스트 15 〉	통과 (0.22ms, 10.2MB)
# 테스트 16 〉	통과 (1.39ms, 10.3MB)
# 테스트 17 〉	통과 (0.03ms, 10.3MB)
# 테스트 18 〉	통과 (0.01ms, 10.2MB)