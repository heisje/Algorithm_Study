from collections import deque

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))
    
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        a, b, c = queue.popleft()
        
        if a == N - 1 and b == M - 1:
            return visited[a][b][c]
        
        for dx, dy in d:
            nx = a + dx
            ny = b + dy
            
            if 0 <= nx < N and 0 <= ny < M:
                # 다음에 이동할 곳이 벽이고, 벽 파괴 기회를 사용하지 않은 경우
                if graph[nx][ny] == 1 and c == 0:
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    queue.append((nx, ny, 1))
                # 다음에 이동할 곳이 벽이 아니고, 아직 방문하지 않은 경우
                elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    queue.append((nx, ny, c))
    return -1


N, M = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(N)]
print(bfs(0, 0, 0))