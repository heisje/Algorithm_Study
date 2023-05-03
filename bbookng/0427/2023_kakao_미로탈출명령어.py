from collections import deque
def solution(n, m, x, y, r, c, k):
    direction = ['d', 'l', 'r', 'u']
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]

    q = deque([(x, y, 0, '')])

    while q:
        cx, cy, cnt, route = q.popleft()
        if cx == r and cy == c and cnt == k:
            return route

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 < nx < n + 1 and 0 < ny < m + 1:
                # 남은 거리가 k보다 많으면 안봐도 됨
                if abs(nx - r) + abs(ny - c) + cnt >= k:
                    continue
                else:
                    q.append((nx, ny, cnt + 1, route + direction[i]))
                    break
    return "impossible"

'''
테스트 1 〉	통과 (0.17ms, 10.3MB)
테스트 2 〉	통과 (0.21ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.04ms, 10.1MB)
테스트 9 〉	통과 (4.44ms, 10.2MB)
테스트 10 〉	통과 (4.28ms, 10.3MB)
테스트 11 〉	통과 (4.62ms, 10.3MB)
테스트 12 〉	통과 (3.87ms, 10.4MB)
테스트 13 〉	통과 (4.32ms, 10.3MB)
테스트 14 〉	통과 (4.56ms, 10.2MB)
테스트 15 〉	통과 (4.51ms, 10.3MB)
테스트 16 〉	통과 (8.36ms, 10.3MB)
테스트 17 〉	통과 (4.59ms, 10.3MB)
테스트 18 〉	통과 (4.46ms, 10.2MB)
테스트 19 〉	통과 (8.68ms, 10.4MB)
테스트 20 〉	통과 (4.52ms, 10.5MB)
테스트 21 〉	통과 (7.12ms, 10.4MB)
테스트 22 〉	통과 (4.60ms, 10.3MB)
테스트 23 〉	통과 (4.54ms, 10.3MB)
테스트 24 〉	통과 (4.29ms, 10.3MB)
테스트 25 〉	통과 (4.93ms, 10.2MB)
테스트 26 〉	통과 (7.11ms, 10.4MB)
테스트 27 〉	통과 (3.99ms, 10.3MB)
테스트 28 〉	통과 (4.50ms, 10.3MB)
테스트 29 〉	통과 (4.08ms, 10.4MB)
테스트 30 〉	통과 (5.02ms, 10.5MB)
테스트 31 〉	통과 (3.74ms, 10.3MB)
'''
