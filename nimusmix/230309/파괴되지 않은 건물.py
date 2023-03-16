def solution(board, skill):
    ans = 0

    for [t, r1, c1, r2, c2, d] in skill:
        if t == 1:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    board[i][j] -= d
        else:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    board[i][j] += d
                    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                ans += 1

    return ans


# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.15ms, 10.4MB)
# 테스트 4 〉	통과 (0.79ms, 10.2MB)
# 테스트 5 〉	통과 (0.86ms, 10.1MB)
# 테스트 6 〉	통과 (1.66ms, 10.2MB)
# 테스트 7 〉	통과 (2.65ms, 10.3MB)
# 테스트 8 〉	통과 (5.47ms, 10.2MB)
# 테스트 9 〉	통과 (5.36ms, 10.2MB)
# 테스트 10 〉	통과 (19.62ms, 10.5MB)

# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	실패 (시간 초과)
# 테스트 7 〉	실패 (시간 초과)