from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

def bfs():
    queue = deque()
    queue.append((fri, frj, fbi, fbj, 0))
    visited[fri][frj] = 0
    visited2[fbi][fbj] = 0
    
    while queue:
        ri, rj, bi, bj, c = queue.popleft()
        
        if c > 10:
            return -1
        
        for d in range(1, N):
            f1 = f2 = 1
            if f1: nri = ri - d
            if f2: nbi = bi - d
            
            if f1 and -1 < nri < N and visited[nri][rj] == -1 and board[nri][rj] != 'B':
                if board[nri][rj] == '#':
                    f1 = 0
                    ari, arj = nri+1, rj
                elif board[nri][rj] == '0':
                    return c+1
                else:
                    visited[nri][rj] == c+1
            
            if f2 and -1 < nbi < N and visited2[nbi][bj] == -1 and board[nbi][bj] != 'R':
                if board[nbi][bj] == '#':
                    f2 = 0
                    abi, abj = nbi+1, bj
                elif board[nbi][bj] == '0':
                    return -9
                else:
                    visited2[nbi][bj] == c+1
            
            if f1 == 0 and f2 == 0:
                break
            
        queue.append((ari, arj, abi, abj, c+1))
        
        for d in range(1, N):
            f1 = f2 = 1
            if f1: nri = ri + d
            if f2: nbi = bi + d
            
            if f1 and -1 < nri < N and visited[nri][rj] == -1 and board[nri][rj] != 'B':
                if board[nri][rj] == '#':
                    f1 = 0
                    ari, arj = nri-1, rj
                elif board[nri][rj] == '0':
                    return c+1
                else:
                    visited[nri][rj] == c+1
            if f2 and -1 < nbi < N and visited2[nbi][bj] == -1 and board[nbi][bj] != 'R':
                if board[nbi][bj] == '#':
                    f2 = 0
                    abi, abj = nbi-1, bj
                elif board[nbi][bj] == '0':
                    return -9
                else:
                    visited2[nbi][bj] == c+1
            
            if f1 == 0 and f2 == 0:
                break
            
        queue.append((ari, arj, abi, abj, c+1))
        
        for d in range(1, N):
            f1 = f2 = 1
            if f1: nrj = rj - d
            if f2: nbj = bj - d
            
            if f1 and -1 < nrj < N and visited[ri][nrj] == -1 and board[ri][nrj] != 'B':
                if board[ri][nrj] == '#':
                    f1 = 0
                    ari, arj = ri, nrj+1
                elif board[ri][nrj] == '0':
                    return c+1
                else:
                    visited[ri][nrj] == c+1
            if f2 and -1 < nbj < N and visited2[bi][nbj] == -1 and board[bi][nbj] != 'R':
                if board[bi][nbj] == '#':
                    f2 = 0
                    abi, abj = bi, nbj+1
                elif board[bi][nbj] == '0':
                    return -9
                else:
                    visited2[bi][nbj] == c+1
            
            if f1 == 0 and f2 == 0:
                break
            
        queue.append((ari, arj, abi, abj, c+1))
        
        for d in range(1, N):
            f1 = f2 = 1
            if f1: nrj = rj + d
            if f2: nbj = bj + d
            
            if f1 and -1 < nrj < N and visited[ri][nrj] == -1 and board[ri][nrj] != 'B':
                # print(ri, nrj, type(board[ri][nrj]), board[ri][nrj])
                if board[ri][nrj] == '#':
                    f1 = 0
                    ari, arj = ri, nrj-1
                elif board[ri][nrj] == '0':
                    return c+1
                else:
                    visited[ri][nrj] == c+1
            if f2 and -1 < nbj < N and visited2[bi][nbj] == -1 and board[bi][nbj] != 'R':
                if board[bi][nbj] == '#':
                    f2 = 0
                    abi, abj = bi, nbj-1
                elif board[bi][nbj] == '0':
                    return -9
                else:
                    visited2[bi][nbj] == c+1
            
            if f1 == 0 and f2 == 0:
                break
            
        queue.append((ari, arj, abi, abj, c+1))
    

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
visited2 = [[-1] * M for _ in range(N)]
f1 = f2 = 1

for i in range(N):
    for j in range(M):
        if f1 or f2:
            if board[i][j] == 'R':
                fri, frj = i, j
                f1 = 0
            elif board[i][j] == 'B':
                fbi, fbj = i, j
                f2 = 0
print(bfs())