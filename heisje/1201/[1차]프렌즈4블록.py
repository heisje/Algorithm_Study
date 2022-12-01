from collections import deque

def solution(m, n, board):
    answer = 0
    trig = True
    board = list(map(list, board))

    while trig:
        # 못찾으면 반복 안할거야!
        trig = False

        # 네모네모를 찾는다.
        visited = [[0 for _ in range(n)] for _ in range(m) ]
        for y in range(m-1):
            for x in range(n-1):
                pin = board[y][x]
                if pin != 0 and pin == board[y+1][x] and pin == board[y][x+1] and pin == board[y+1][x+1]:
                    visited[y][x] = visited[y+1][x] = visited[y][x+1] = visited[y+1][x+1] = 1
                    trig = True

        # 새로운 리스트를 만들어서, 삭제 안된 것을 고른다.
        new_list = deque(deque() for _ in range(n))
        for x in range(n):
            for y in range(m):
                # 삭제될건 패스하고~
                if visited[y][x] == 1:
                    pass
                # 삭제 안될거는 추가해!
                else:
                    new_list[x].append(board[y][x])
            # 남은 공간을 채워채워!!
            for _ in range(m-len(new_list[x])):
                new_list[x].appendleft(0)

        # 찾은 new_list를 돌려돌려
        for y in range(m):
            for x in range(n):
                board[y][x] = new_list[x][y]

    # 0개수 찾을거야!
    for y in range(m):
        for x in range(n):
            if board[y][x] == 0:
                answer += 1
    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))