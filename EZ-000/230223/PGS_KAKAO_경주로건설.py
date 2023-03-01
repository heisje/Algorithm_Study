from heapq import heappop, heappush


def solution(board):
    N = len(board)
    visited = [[[-1] * 4 for _ in range(N)] for _ in range(N)]
    heap = [(-1, 0, 0, 0)]  # direction, cost, x, y

    answer = -1
    while heap:
        d, c, x, y = heappop(heap)
        if x == y == N - 1 and (answer == -1 or c < answer):
            answer = c

        new_pos = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for direction, (nx, ny) in enumerate(new_pos):
            if nx < 0 or ny < 0 or N - 1 < nx or N - 1 < ny:
                continue
            if board[nx][ny]:
                continue

            cost = c + (100 if d == direction or d == -1 else 600)
            if visited[nx][ny][direction] != -1 and visited[nx][ny][direction] < cost:
                continue

            heappush(heap, (direction, cost, nx, ny))
            visited[nx][ny][direction] = cost
    return answer

"""
테스트 1 〉	통과 (0.09ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.08ms, 10.2MB)
테스트 5 〉	통과 (0.08ms, 10.3MB)
테스트 6 〉	통과 (1.36ms, 10.3MB)
테스트 7 〉	통과 (2.60ms, 10.2MB)
테스트 8 〉	통과 (1.26ms, 10.1MB)
테스트 9 〉	통과 (1.55ms, 10.1MB)
테스트 10 〉	통과 (12.93ms, 10.4MB)
테스트 11 〉	통과 (93.97ms, 10.5MB)
테스트 12 〉	통과 (10.30ms, 10.2MB)
테스트 13 〉	통과 (0.87ms, 10.2MB)
테스트 14 〉	통과 (0.74ms, 10.2MB)
테스트 15 〉	통과 (2.27ms, 10.3MB)
테스트 16 〉	통과 (11.56ms, 10.1MB)
테스트 17 〉	통과 (77.95ms, 10.4MB)
테스트 18 〉	통과 (48.44ms, 10.2MB)
테스트 19 〉	통과 (124.59ms, 10.7MB)
테스트 20 〉	통과 (1.53ms, 10.2MB)
테스트 21 〉	통과 (1.49ms, 10.2MB)
테스트 22 〉	통과 (0.23ms, 10.2MB)
테스트 23 〉	통과 (0.10ms, 10.2MB)
테스트 24 〉	통과 (0.24ms, 10.2MB)
테스트 25 〉	통과 (0.14ms, 10.2MB)
"""