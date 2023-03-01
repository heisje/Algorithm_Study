def dfs(i, j, board, answer, D):
    visited = [[float('INF')] * len(board) for _ in range(len(board))]
    visited[i][j] = 0
    check = [[[] for _ in range(len(board))] for _ in range(len(board))]
    dir = (0, 0)
    stack = []
    while True:
        for di, dj in D:
            ni, nj = i+di, j+dj
            if 0<=ni<len(board) and 0<=nj<len(board) and board[ni][nj] != 1:
                if dir == (0, 0) and visited[ni][nj] > visited[i][j] + 100:
                    visited[ni][nj] = visited[i][j] + 100
                    stack.append((i, j, dir))
                    dir = (di, dj)
                    check[ni][nj] = [dir]
                    i, j = ni, nj
                    break
                elif dir == (di, dj) and visited[ni][nj] > visited[i][j] + 100:
                    visited[ni][nj] = visited[i][j] + 100
                    stack.append((i, j, dir))
                    check[ni][nj] = [dir]
                    i, j = ni, nj
                    break
                elif dir != (di, dj) and visited[ni][nj] > visited[i][j] + 600:
                    visited[ni][nj] = visited[i][j] + 600
                    stack.append((i, j, dir))
                    dir = (di, dj)
                    check[ni][nj] = [dir]
                    i, j = ni, nj
                    break
                elif dir != (di, dj) and visited[ni][nj] == visited[i][j] + 600 and (di, dj) not in check[ni][nj]:
                    stack.append((i, j, dir))
                    dir = (di, dj)
                    check[ni][nj].append(dir)
                    i, j = ni, nj
                    break
                elif dir == (di, dj) and visited[ni][nj] == visited[i][j] + 100 and (di, dj) not in check[ni][nj]:
                    stack.append((i, j, dir))
                    dir = (di, dj)
                    check[ni][nj].append(dir)
                    i, j = ni, nj
                    break
        else:
            if stack:
                i, j, dir = stack.pop()
            else:
                # for k in check:
                #     print(*k)
                answer.append(visited[-1][-1])
                return

def solution(board):
    answer = []
    dfs(0, 0, board, answer, ((0, 1), (1, 0), (-1, 0), (0, -1)))
    dfs(0, 0, board, answer, ((1, 0), (0, 1), (-1, 0), (0, -1)))
    # for i in arr:
    #     print(*i)
    return min(answer)

'''
테스트 1 〉	통과 (0.19ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 10.1MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.18ms, 10.3MB)
테스트 5 〉	통과 (0.16ms, 10.3MB)
테스트 6 〉	통과 (12.21ms, 10.2MB)
테스트 7 〉	통과 (14.08ms, 10.4MB)
테스트 8 〉	통과 (13.38ms, 10.5MB)
테스트 9 〉	통과 (11.78ms, 10.3MB)
테스트 10 〉	통과 (50.84ms, 10.4MB)
테스트 11 〉	통과 (144.78ms, 10.4MB)
    테스트 12 〉	통과 (921.43ms, 10.3MB)
테스트 13 〉	통과 (1.71ms, 10.2MB)
테스트 14 〉	통과 (2.10ms, 10.3MB)
테스트 15 〉	통과 (39.82ms, 10.3MB)
테스트 16 〉	통과 (134.17ms, 10.3MB)
테스트 17 〉	통과 (94.37ms, 10.4MB)
테스트 18 〉	통과 (387.74ms, 10.3MB)
테스트 19 〉	통과 (364.13ms, 10.3MB)
테스트 20 〉	통과 (7.33ms, 10.3MB)
테스트 21 〉	통과 (12.04ms, 10.2MB)
테스트 22 〉	통과 (0.38ms, 10.3MB)
테스트 23 〉	통과 (0.32ms, 10.3MB)
테스트 24 〉	통과 (0.29ms, 10.3MB)
테스트 25 〉	통과 (0.18ms, 10.4MB)
'''