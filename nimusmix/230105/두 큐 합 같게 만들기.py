from collections import deque


def solution(queue1, queue2):
    sum_all, sum_q1, sum_q2 = sum(queue1 + queue2), sum(queue1), sum(queue2)

    if (sum_all % 2 == 1):
        return -1

    cnt = 0
    q1, q2 = deque(queue1), deque(queue2)

    while q1 and q2 and cnt <= len(queue1) * 3:
        if sum_q1 > sum_q2:
            x = q1.popleft()
            q2.append(x)
            sum_q1 -= x
            sum_q2 += x
        elif sum_q1 < sum_q2:
            x = q2.popleft()
            q1.append(x)
            sum_q2 -= x
            sum_q1 += x
        else:
            return cnt
        cnt += 1
        if cnt >= len(queue1) * 3:
            return -1
    return -1


# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.05ms, 9.99MB)
# 테스트 6 〉	통과 (0.04ms, 10.2MB)
# 테스트 7 〉	통과 (0.06ms, 10.4MB)
# 테스트 8 〉	통과 (0.04ms, 10.2MB)
# 테스트 9 〉	통과 (0.13ms, 10.1MB)
# 테스트 10 〉	통과 (0.19ms, 10.3MB)
# 테스트 11 〉	통과 (60.97ms, 14.6MB)
# 테스트 12 〉	통과 (17.01ms, 14.7MB)
# 테스트 13 〉	통과 (5.69ms, 12.1MB)
# 테스트 14 〉	통과 (7.44ms, 12.4MB)
# 테스트 15 〉	통과 (8.76ms, 18.1MB)
# 테스트 16 〉	통과 (5.65ms, 18.5MB)
# 테스트 17 〉	통과 (5.58ms, 17.6MB)
# 테스트 18 〉	통과 (20.35ms, 33MB)
# 테스트 19 〉	통과 (26.33ms, 37.4MB)
# 테스트 20 〉	통과 (52.40ms, 37.6MB)
# 테스트 21 〉	통과 (32.43ms, 37.8MB)
# 테스트 22 〉	통과 (93.61ms, 37.7MB)
# 테스트 23 〉	통과 (73.69ms, 37.8MB)
# 테스트 24 〉	통과 (105.89ms, 37.7MB)
# 테스트 25 〉	통과 (0.07ms, 10.2MB)
# 테스트 26 〉	통과 (0.04ms, 10.3MB)
# 테스트 27 〉	통과 (0.05ms, 10.2MB)
# 테스트 28 〉	통과 (108.53ms, 19.2MB)
# 테스트 29 〉	통과 (0.51ms, 10.8MB)
# 테스트 30 〉	통과 (93.64ms, 19.2MB)
