from collections import deque

def solution(board):
    n = len(board)
    cost = [[[1e9] * n for _ in range(n)] for _ in range(4)]
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque()
    
    for i in range(4):
        cost[i][0][0] = 0
    
    if board[0][1] == 0:
        queue.append([0, 1, 0, 100])
        cost[0][0][1] = 100
        
    if board[1][0] == 0:
        queue.append([1, 0, 1, 100])
        cost[1][1][0] = 100
        
    while queue:
        x, y, d, c = queue.popleft()            # x 좌표, y 좌표, 방향, 비용
        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                new_cost = c + 100 if d == i else c + 600
                if cost[i][nx][ny] > new_cost:
                    cost[i][nx][ny] = new_cost
                    queue.append([nx, ny, i, new_cost])
    
    return min([cost[i][-1][-1] for i in range(4)])


# 테스트 1 〉	통과 (0.05ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.04ms, 10.1MB)
# 테스트 4 〉	통과 (0.10ms, 10.2MB)
# 테스트 5 〉	통과 (0.11ms, 10.3MB)
# 테스트 6 〉	통과 (1.87ms, 10.2MB)
# 테스트 7 〉	통과 (2.87ms, 10.2MB)
# 테스트 8 〉	통과 (1.43ms, 10.2MB)
# 테스트 9 〉	통과 (0.73ms, 10.2MB)
# 테스트 10 〉	통과 (1.80ms, 10.2MB)
# 테스트 11 〉	통과 (29.73ms, 10.1MB)
# 테스트 12 〉	통과 (10.20ms, 10.2MB)
# 테스트 13 〉	통과 (0.65ms, 10.2MB)
# 테스트 14 〉	통과 (0.99ms, 10.1MB)
# 테스트 15 〉	통과 (4.17ms, 10.1MB)
# 테스트 16 〉	통과 (6.90ms, 10.2MB)
# 테스트 17 〉	통과 (11.08ms, 10.2MB)
# 테스트 18 〉	통과 (18.97ms, 10.1MB)
# 테스트 19 〉	통과 (25.50ms, 10.2MB)
# 테스트 20 〉	통과 (1.95ms, 10.1MB)
# 테스트 21 〉	통과 (1.31ms, 10.1MB)
# 테스트 22 〉	통과 (0.19ms, 10.1MB)
# 테스트 23 〉	통과 (0.12ms, 10.1MB)
# 테스트 24 〉	통과 (0.23ms, 10.2MB)
# 테스트 25 〉	통과 (0.12ms, 10.1MB)