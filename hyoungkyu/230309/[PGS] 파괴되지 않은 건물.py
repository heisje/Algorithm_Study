def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    tmp_board = [[0] * m for _ in range(n)]
    for type, r1, c1, r2, c2, degree in skill:
        tmp_board[r1][c1] += degree if type==2 else -degree
        if c2+1 < m:
            tmp_board[r1][c2+1] += -degree if type==2 else degree
        if r2+1 < n:
            tmp_board[r2+1][c1] += -degree if type==2 else degree
        if r2+1 < n and c2+1 < m:
            tmp_board[r2+1][c2+1] += degree if type==2 else -degree

    for i in range(n):
        for j in range(1, m):
            tmp_board[i][j] += tmp_board[i][j-1]
            
    for j in range(m):
        for i in range(1, n):
            tmp_board[i][j] += tmp_board[i-1][j]
            
    for i in range(n):
        for j in range(m):
            answer += 1 if board[i][j] + tmp_board[i][j] > 0 else 0
            
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.10ms, 10.1MB)
테스트 3 〉	통과 (0.32ms, 10.3MB)
테스트 4 〉	통과 (0.39ms, 10.2MB)
테스트 5 〉	통과 (0.69ms, 10.4MB)
테스트 6 〉	통과 (0.96ms, 10.1MB)
테스트 7 〉	통과 (1.68ms, 10.2MB)
테스트 8 〉	통과 (3.77ms, 10.2MB)
테스트 9 〉	통과 (4.84ms, 10.2MB)
테스트 10 〉	통과 (3.96ms, 10.3MB)

효율성  테스트
테스트 1 〉	통과 (881.81ms, 135MB)
테스트 2 〉	통과 (883.79ms, 135MB)
테스트 3 〉	통과 (812.97ms, 135MB)
    테스트 4 〉	통과 (902.21ms, 135MB)
테스트 5 〉	통과 (642.11ms, 101MB)
테스트 6 〉	통과 (568.65ms, 101MB)
테스트 7 〉	통과 (616.83ms, 101MB)
'''