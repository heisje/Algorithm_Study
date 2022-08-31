def cal_kevin_bacon (V_list, E_dict):
    min_val = len(V_list) * len(E_dict)
    In_SSA = V_list[0]                            # 일단 가장 첫번째 사람이 가장 인싸라고 생각하자
    for guy in V_list:
        visited = [0] * (len(V_list) + 1)         # 인덱스 에러 방지용 하나 추가

        q = []
        visited[guy] = 1
        q.append(guy)
        while(q):                                 # BFS를 돌면서 각각의 사람에게 몇번만에 도달하는지 확인하여 저장한다.
            v = q.pop(0)
            for w in E_dict[v]:
                if visited[w] == 0:
                    q.append(w)
                    visited[w] = visited[v] + 1
                else:
                    continue
        local_sum = sum(visited)                  # 거리가 저장된 값을 모두 합친다
        if local_sum < min_val:
            min_val = local_sum                   # 케빈 베이컨의 최솟값을 갱신함
            In_SSA = guy                          # 새로운 인싸 결정
    return In_SSA

V, E = map(int, input().split())

people = [i + 1 for i in range(V)]                # 사람들을 저장한 리스트
edge_dict = {i + 1: [] for i in range(V)}         # 사람들 사이의 간선을 저장한 딕셔너리

for i in range(E):
    a, b = map(int, input().split())
    edge_dict[a].append(b)                        # 양방향으로 추가해줘야 한다.
    edge_dict[b].append(a)

print(cal_kevin_bacon(people, edge_dict))

