# block인 부분 체크하기
def is_block(m, n, i, j, board, visited):
    tmp = 0
    if i+1 < m and j+1 < n:
        if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
            if not visited[i][j]:
                visited[i][j] = 1
                tmp += 1
            if not visited[i+1][j]:
                visited[i+1][j] = 1
                tmp += 1
            if not visited[i][j+1]:
                visited[i][j+1] = 1
                tmp += 1
            if not visited[i+1][j+1]:
                visited[i+1][j+1] = 1
                tmp += 1
    return tmp

# 폭파시킨 후 요소들 내리기 --> 쭉 내려야됨
def down(m, n, board):
    for j in range(n):
        for i in range(m-1, -1, -1):
            if board[i][j] == 0:
                k = 0
                while 0<i-k:
                    k += 1
                    if board[i-k][j]:
                        board[i][j] = board[i-k][j]
                        board[i-k][j] = 0
                        break
            
def solution(m, n, board):
    answer = 0
    board = [list(s) for s in board]
    while True:
        visited = [[0] * n for _ in range(m)]   # 폭파시킬 요소들 체크할 배열
        check = answer                          # 폭파시킨 요소가 있는지 체크할 변수
        for i in range(m):                      # 전체 돌면서 블록 있는지 확인할거임
            for j in range(n):
                if board[i][j]:                 # 요소가 있으면
                    num = is_block(m, n, i, j, board, visited)  # 블록인지 확인
                    answer += num                               # 블록이 있으면 더하기 (디폴트 0)
        if check == answer:                     # 블록이 없으면 break
            break
        else:                                   # 블록이 있으면 폭파시키고 요소들 밑으로 내리기
            for i in range(m):
                for j in range(n):
                    if visited[i][j]:
                        board[i][j] = 0
            down(m, n, board)

    return answer

'''
테스트 1 〉통과 (0.05ms, 10.4MB)
테스트 2 〉통과 (0.10ms, 10.3MB)
테스트 3 〉통과 (0.01ms, 10.2MB)
테스트 4 〉통과 (1.93ms, 10.5MB)
테스트 5 〉통과 (206.83ms, 10.2MB)
테스트 6 〉통과 (12.53ms, 10.3MB)
테스트 7 〉통과 (2.05ms, 10.3MB)
테스트 8 〉통과 (4.04ms, 10.4MB)
테스트 9 〉통과 (0.05ms, 10.4MB)
테스트 10 〉통과 (0.80ms, 10.2MB)
테스트 11 〉통과 (9.47ms, 10.3MB)
'''