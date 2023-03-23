def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    delta = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for s in skill:
        type, r1, c1, r2, c2, degree = s
        if type == 1:
            delta[r1][c1] += -degree
            delta[r1][c2 + 1] += degree
            delta[r2 + 1][c1] += degree
            delta[r2 + 1][c2 + 1] += -degree
        elif type == 2:
            delta[r1][c1] += degree
            delta[r1][c2 + 1] += -degree
            delta[r2 + 1][c1] += -degree
            delta[r2 + 1][c2 + 1] += degree

    for r in range(N):
        for c in range(1, M):
            delta[r][c] += delta[r][c - 1]

    for c in range(M):
        for r in range(1, N):
            delta[r][c] += delta[r - 1][c]

    for r in range(N):
        for c in range(M):
            if 0 < board[r][c] + delta[r][c]:
                answer += 1

    return answer

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.06ms, 10.3MB)
테스트 3 〉	통과 (0.18ms, 10.1MB)
테스트 4 〉	통과 (0.39ms, 10.3MB)
테스트 5 〉	통과 (0.64ms, 10.3MB)
테스트 6 〉	통과 (1.26ms, 10.2MB)
테스트 7 〉	통과 (1.37ms, 10.3MB)
테스트 8 〉	통과 (2.13ms, 10.3MB)
테스트 9 〉	통과 (4.62ms, 10.4MB)
테스트 10 〉	통과 (3.83ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (814.35ms, 136MB)
테스트 2 〉	통과 (812.90ms, 136MB)
테스트 3 〉	통과 (711.81ms, 136MB)
테스트 4 〉	통과 (812.70ms, 136MB)
테스트 5 〉	통과 (533.30ms, 102MB)
테스트 6 〉	통과 (618.24ms, 102MB)
테스트 7 〉	통과 (625.39ms, 102MB)
"""
