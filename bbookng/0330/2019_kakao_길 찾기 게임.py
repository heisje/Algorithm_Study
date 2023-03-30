import sys
sys.setrecursionlimit(10**6)

def pre_order(node, ll, rr, ans):  # 전위 순회
    if node != 0:
        ans.append(node)
        pre_order(ll[node], ll, rr, ans)
        pre_order(rr[node], ll, rr, ans)


def post_order(node, ll, rr, ans):  # 후위 순회
    if node != 0:
        post_order(ll[node], ll, rr, ans)
        post_order(rr[node], ll, rr, ans)
        ans.append(node)

def solution(nodeinfo):
    ans1 = []
    ans2 = []

    N = len(nodeinfo)
    left_node = [0] * (N + 1)
    right_node = [0] * (N + 1)

    # nodeinfo에 node 번호 추가
    for i in range(N):
        nodeinfo[i] += [i+1]

    # nodeinfo를 위에서부터 아래로 왼쪽에서부터 오른쪽으로 정렬
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))

    # 트리 저장용 dict
    d = {}

    # 위에서부터 하나씩 노드를 놓는 작업을 수행
    for x, y, idx in nodeinfo:
        # [x좌표, y좌표, left 자식 노드, right 자식노드]
        d[idx] = [x, y, None, None]
        now = nodeinfo[0][2]
        # for문에서 주어진 노드를 놓을 때 까지 while문을 돈다
        while True:
            # 만약 놓을 노드(for 문에서 주어지는 노드)가 현재 노드(now)x값(d[now][0])보다 보다 크면 오른쪽에 두어야함
            if x > d[now][0]:
                # 이 때, 현재 노드의 오른쪽 자식노드가 비어있다면
                if not (d[now][3]):
                    # 해당 노드의 자식노드로 놓을 노드(for 문에서 주어지는 노드)를 놓고
                    d[now][3] = idx
                    # right_node 리스트 갱신후 끝
                    right_node[now] = idx
                    break
                # 만약 오른쪽 노드가 있다면 현재 노드를 오른쪽 노드로 변경하고 다시 while문 수행
                now = d[now][3]

            # 왼쪽도 동일한 방식으로 진행
            elif x < d[now][0]:
                if not (d[now][2]):
                    d[now][2] = idx
                    left_node[now] = idx
                    break
                now = d[now][2]

            # 첫 노드는 그냥 넣음
            else:
                break


    pre_order(nodeinfo[0][2], left_node, right_node, ans1)
    post_order(nodeinfo[0][2], left_node, right_node, ans2)
    answer = [ans1, ans2]
    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))

'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.06ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (85.47ms, 11.1MB)
테스트 7 〉	통과 (60.40ms, 11.2MB)
테스트 8 〉	통과 (49.72ms, 11.6MB)
테스트 9 〉	통과 (274.18ms, 14.5MB)
테스트 10 〉	통과 (23.40ms, 10.8MB)
테스트 11 〉	통과 (208.28ms, 14.3MB)
테스트 12 〉	통과 (245.86ms, 14.4MB)
테스트 13 〉	통과 (0.36ms, 10.4MB)
테스트 14 〉	통과 (3.34ms, 10.5MB)
테스트 15 〉	통과 (17.96ms, 12MB)
테스트 16 〉	통과 (35.32ms, 14.4MB)
테스트 17 〉	통과 (6.19ms, 10.6MB)
테스트 18 〉	통과 (43.23ms, 14MB)
테스트 19 〉	통과 (12.62ms, 10.9MB)
테스트 20 〉	통과 (15.61ms, 11.8MB)
테스트 21 〉	통과 (41.10ms, 12.6MB)
테스트 22 〉	통과 (39.15ms, 14.1MB)
테스트 23 〉	통과 (42.80ms, 14.5MB)
테스트 24 〉	통과 (0.02ms, 10.2MB)
테스트 25 〉	통과 (0.02ms, 10.1MB)
테스트 26 〉	통과 (117.13ms, 11.5MB)
테스트 27 〉	통과 (0.02ms, 10.4MB)
테스트 28 〉	통과 (0.06ms, 10.3MB)
테스트 29 〉	통과 (0.01ms, 10.2MB)
'''