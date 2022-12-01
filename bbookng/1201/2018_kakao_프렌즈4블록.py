def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board]

    while True:

        tmp = set()

        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != '':
                    tmp.update({(i, j), (i, j+1), (i+1, j), (i+1, j+1)})

        if tmp:
            answer += len(tmp)
            for i in tmp:
                x, y = i
                board[x][y] = ''
        else:
            return answer

        while True:
            flag = False
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and not board[i+1][j]:
                        board[i+1][j] = board[i][j]
                        board[i][j] = ''
                        flag = True

            if not flag:
                break

'''
테스트 1 〉	통과 (0.05ms, 10.3MB)
테스트 2 〉	통과 (0.07ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (1.45ms, 10.2MB)
테스트 5 〉	통과 (232.69ms, 10.3MB)
테스트 6 〉	통과 (15.25ms, 10.3MB)
테스트 7 〉	통과 (0.96ms, 10.2MB)
테스트 8 〉	통과 (1.06ms, 10.3MB)
테스트 9 〉	통과 (0.07ms, 10.2MB)
테스트 10 〉	통과 (1.61ms, 10.3MB)
테스트 11 〉	통과 (1.80ms, 10.4MB)
'''
