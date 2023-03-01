from collections import deque
def bfs(board):
    costs = [[[1e9] * len(board) for _ in range(len(board))] for _ in range(4)]

    for i in range(4):
        costs[i][0][0] = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append((0, 0, 0, 0))

    if board[0][1] == 0:
        costs[0][0][1] = 100
        q.append((0, 1, 0, 100))

    if board[1][0] == 0:
        costs[1][1][0] = 100
        q.append((1, 0, 1, 100))

    while q:
        x, y, direction, cost = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            new_cost = 100 if i == direction else 600

            if 0 <= nx < len(board) and 0 <= ny < len(board) and not board[nx][ny]:
                if new_cost + cost < costs[i][nx][ny]:
                    costs[i][nx][ny] = new_cost + cost
                    q.append((nx, ny, i, new_cost + cost))

    return min(costs[0][-1][-1], costs[1][-1][-1], costs[2][-1][-1], costs[3][-1][-1])
def solution(board):
    return bfs(board)


print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))

'''
테스트 1 〉	통과 (0.05ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 10MB)
테스트 3 〉	통과 (0.05ms, 10MB)
테스트 4 〉	통과 (0.06ms, 10.2MB)
테스트 5 〉	통과 (0.08ms, 10.2MB)
테스트 6 〉	통과 (1.66ms, 10.2MB)
테스트 7 〉	통과 (3.28ms, 10.3MB)
테스트 8 〉	통과 (2.96ms, 10.2MB)
테스트 9 〉	통과 (1.03ms, 10.1MB)
테스트 10 〉	통과 (2.78ms, 10.2MB)
테스트 11 〉	통과 (31.04ms, 10.2MB)
테스트 12 〉	통과 (5.72ms, 10MB)
테스트 13 〉	통과 (0.76ms, 10MB)
테스트 14 〉	통과 (0.59ms, 9.98MB)
테스트 15 〉	통과 (2.39ms, 10.2MB)
테스트 16 〉	통과 (7.85ms, 10.1MB)
테스트 17 〉	통과 (9.02ms, 10.2MB)
테스트 18 〉	통과 (14.17ms, 10.2MB)
테스트 19 〉	통과 (24.21ms, 10.2MB)
테스트 20 〉	통과 (2.50ms, 10.2MB)
테스트 21 〉	통과 (2.55ms, 10.2MB)
테스트 22 〉	통과 (0.14ms, 10.2MB)
테스트 23 〉	통과 (0.23ms, 10.1MB)
테스트 24 〉	통과 (0.14ms, 10.2MB)
테스트 25 〉	통과 (0.08ms, 10.2MB)
'''