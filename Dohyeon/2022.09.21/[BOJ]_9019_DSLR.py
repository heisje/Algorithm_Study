from collections import deque
import sys

test_case = int(input())
input = sys.stdin.readline
route = {0: [[0, "D"], [9999, "S"]]}              # 가능한 경로를 저장할 딕셔너리


def calc_l(n):
    temp = n * 10
    a = temp % 10000
    b = temp // 10000
    return a + b


def calc_r(n):
    a = n % 10
    b = n // 10
    return 1000*a + b


for i in range(1, 5000):
    route[i] = [[i - 1, "S"], [i * 2, "D"], [calc_l(i), "L"], [calc_r(i), "R"]]
for i in range(5000, 10000):
    route[i] = [[i - 1, "S"], [i * 2 % 10000, "D"], [calc_l(i), "L"], [calc_r(i), "R"]]


for tc in range(1, test_case + 1):

    A, B = map(int, input().split())
    visited = [[] for i in range(10000)]          # 지나온 길을 저장할 것

    queue = deque([A])

    while queue:
        n = queue.popleft()
        if n == B:
            for i in visited[B]:
                print(i, end="")
            print()
            break

        for i in route[n]:
            if not (visited[i[0]]):
                queue.append(i[0])
                visited[i[0]].extend(visited[n] + [i[1]]) # 이전 단계 루트를 더한다.
                #visited[i[0]].append(i[1])





