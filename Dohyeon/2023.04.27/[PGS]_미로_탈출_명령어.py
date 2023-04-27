from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = ''
    # answer_list = []
    # dx = [-1, 0, 1, 0]
    # dy = [0, 1, 0, -1]
    #
    # if (abs(x - r) + abs(y - c)) % 2:
    #     if k % 2 == 0:
    #         return "impossible"
    # else:
    #     if k % 2:
    #         return "impossible"
    #
    #
    # que = deque([["", x - 1, y - 1]])
    #
    # while(que):
    #     current = que.popleft()
    #
    #     for i in range(4):
    #         if current[1] + dx[i] < 0 or current[1] + dx[i] >= n:
    #             continue
    #         if current[2] + dy[i] < 0 or current[2] + dy[i] >= m:
    #             continue
    #
    #         next = [current[0], current[1] + dx[i], current[2] + dy[i]]
    #
    #         if i == 0:
    #             next[0] = next[0] + "u"
    #         elif i == 1:
    #             next[0] = next[0] + "r"
    #         elif i == 2:
    #             next[0] = next[0] + "d"
    #         elif i == 3:
    #             next[0] = next[0] + "l"
    #
    #         ## 핵심 자르기
    #         if abs(next[1] - (r - 1)) + abs(next[2] - (c - 1)) > k - len(next[0]):
    #             continue
    #
    #
    #
    #
    #
    #         #####
    #         if len(next[0]) == k:
    #             if next[1] == r - 1 and next[2] == c - 1:
    #                 answer_list.append(next[0])
    #                 continue
    #
    #         elif len(next[0]) > k:
    #             continue
    #
    #         else:
    #             que.append(next)
    #
    # answer_list.sort()
    # if len(answer_list) == 0:
    #     return "impossible"
    # return answer_list[0]

    if (abs(x - r) + abs(y - c)) % 2:
        if k % 2 == 0:
            return "impossible"
    else:
        if k % 2:
            return "impossible"

    if (abs(x - r) + abs(y - c)) > k:
        return "impossible"

    elif (abs(x - r) + abs(y - c)) == k:

        if x - r > 0:           # 시작지점이 도착보다 낮음
            while(x != r):
                answer = answer + "u"
                x = x - 1
        elif x == r:
            pass
            #여유 없음
        else:
            while (x != r):
                answer = answer + "d"
                x = x + 1

        if y - c > 0:           # 시작지점이 도착점 오른쪽에 있음
            while (y != c):
                answer = answer + "l"
                y = y - 1

        elif y == c:
            pass
            #여유 없음

        else:                   # 시작지점이 도착점 왼쪽에 있음
            while (y != c):
                answer = answer + "r"
                y = y + 1

    else:                       # 다른곳을 들릴 여유가 있음. 여유는 짝수로 남게됨

        spare = (k - (abs(x - r) + abs(y - c))) // 2
        while(spare > 0):

            if x + 1 <= n:
                answer = answer + "d"

            elif y - 1 > 0:
                answer = answer + "l"

            elif y + 1 <= m:
                answer = answer + "r"

            else:
                answer = answer + "u"

            spare = (k - (abs(x - r) + abs(y - c))) // 2

        total = (abs(x - r) + abs(y - c))

        while(total):
            if x - r > 0:  # 시작지점이 도착보다 낮음
                answer = answer + "u"
                total = (abs(x - r) + abs(y - c))
                continue

            elif x == r:
                pass
                # 여유 없음
            else:
                answer = answer + "d"
                total = (abs(x - r) + abs(y - c))
                x = x + 1

            if y - c > 0:  # 시작지점이 도착점 오른쪽에 있음
                while (y != c):
                    answer = answer + "l"
                    y = y - 1

            elif y == c:
                pass
                # 여유 없음

            else:  # 시작지점이 도착점 왼쪽에 있음
                while (y != c):
                    answer = answer + "r"
                    y = y + 1








print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))