from collections import deque


def solution(queue1, queue2):
    answer = 0
    s1, s2 = sum(queue1), sum(queue2)
    if (s1 + s2) % 2:
        answer = -1
    else:
        L = len(queue1)
        queue1, queue2 = deque(queue1), deque(queue2)
        while True:
            if L * 3 < answer:
                answer = -1
                break
            if s1 == s2:
                break

            if s2 < s1:
                temp = queue1.popleft()
                queue2.append(temp)
                s1 -= temp
                s2 += temp
            else:
                temp = queue2.popleft()
                queue1.append(temp)
                s1 += temp
                s2 -= temp
            answer += 1

    return answer
