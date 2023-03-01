

def solution(board):
    # dfs
    # before X, before Y, x, y, visited, money
    def dfs(bx, by, x, y, money, LEN_X, LEN_Y):
        money += 100
        if min_money[0] != -1 and min_money[0] < money:
            return
        if min_money[0] != -1 and money + ((LEN_X - 1 - x) + (LEN_Y - 1 - y)) * 100 > min_money[0]:
            return

        for dx, dy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if dx == LEN_X-1 and dy == LEN_Y-1:
                if bx == x == dx or by == y == dy:
                    pass
                else:
                    money += 500
                if min_money[0] == -1 or money < min_money[0]:
                    min_money[0] = money
                return

            # board가 벽이면 패스
            if 0 <= dx < LEN_X and 0 <= dy < LEN_Y and board[dy][dx] == 0 and visited[dy][dx] == 0:
                visited[dy][dx] = 2
                if bx == x == dx or by == y == dy:
                    if min_visited[dy][dx] == 0 or money <= min_visited[dy][dx] + 400:
                        min_visited[dy][dx] = money
                        dfs(x, y, dx, dy, money ,LEN_X, LEN_Y)
                else:
                    if min_visited[dy][dx] == 0 or money <= min_visited[dy][dx] + 400:
                        min_visited[dy][dx] = money
                        dfs(x, y, dx, dy, money + 500, LEN_X, LEN_Y)
                visited[dy][dx] = 0
    # 칸마다 가장 빠른 시간을 업데이트 하면서 bfs로 진행한다.
    # 칸의 위쪽 왼쪽 만 체크하면서 진행한다.
    LEN_X = len(board[0])
    LEN_Y = len(board)
    visited = [[board[y][x] for x in range(LEN_X)] for y in range(LEN_Y)]
    min_visited = [[board[y][x] for x in range(LEN_X)] for y in range(LEN_Y)]
    min_money = [-1,[]]
    dfs(0,0,0,0,0, LEN_X, LEN_Y)
    return min_money[0]

a = [[0,0,0],[0,0,0],[0,0,0]]
print(solution(a))
a = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(a))
a = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
print(solution(a))
a = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
print(solution(a))

# 테스트 1 〉	통과 (0.03ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.5MB)
# 테스트 3 〉	통과 (0.01ms, 10.5MB)
# 테스트 4 〉	통과 (0.08ms, 10.5MB)
# 테스트 5 〉	통과 (0.12ms, 10.4MB)
# 테스트 6 〉	통과 (1.72ms, 10.4MB)
# 테스트 7 〉	통과 (4.70ms, 10.5MB)
# 테스트 8 〉	통과 (2.57ms, 10.5MB)
# 테스트 9 〉	통과 (0.54ms, 10.4MB)
# 테스트 10 〉	통과 (2.59ms, 10.4MB)
# 테스트 11 〉	통과 (767.40ms, 10.5MB)
# 테스트 12 〉	통과 (155.00ms, 10.9MB)
# 테스트 13 〉	통과 (0.34ms, 10.5MB)
# 테스트 14 〉	통과 (1.69ms, 10.4MB)
# 테스트 15 〉	통과 (5.23ms, 10.3MB)
# 테스트 16 〉	통과 (29.23ms, 10.4MB)
# 테스트 17 〉	통과 (48.76ms, 10.3MB)
# 테스트 18 〉	통과 (171.63ms, 10.5MB)
# 테스트 19 〉	통과 (142.86ms, 10.5MB)
# 테스트 20 〉	통과 (2.19ms, 10.6MB)
# 테스트 21 〉	통과 (1.72ms, 10.6MB)
# 테스트 22 〉	통과 (0.09ms, 10.3MB)
# 테스트 23 〉	통과 (0.19ms, 10.4MB)
# 테스트 24 〉	통과 (0.14ms, 10.4MB)
# 테스트 25 〉	통과 (0.06ms, 10.3MB)