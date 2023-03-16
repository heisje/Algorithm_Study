def solution(board, skill):
    fure = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    for ty, r1, c1, r2, c2, degree in skill:
        if ty == 2:
            degree = -degree
        fure[r1][c1] -= degree 
        fure[r2+1][c1] += degree 
        fure[r1][c2+1] += degree 
        fure[r2+1][c2+1] -= degree 
    
    cnt = 0
    
    for r in range(0,len(fure)):
        for c in range(1,len(fure[0])):
            fure[r][c] += fure[r][c-1]
            
    for c in range(0,len(fure[0])):
        for r in range(1,len(fure)):
            fure[r][c] += fure[r-1][c]     
    cnt = 0
    for r in range(0,len(board)):
        for c in range(0,len(board[0])):
            board[r][c] += fure[r][c]
            if board[r][c] >= 1:
                cnt += 1
            
    return cnt

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.09ms, 10.3MB)
# 테스트 3 〉	통과 (0.42ms, 10.3MB)
# 테스트 4 〉	통과 (0.42ms, 10.2MB)
# 테스트 5 〉	통과 (0.73ms, 10.1MB)
# 테스트 6 〉	통과 (1.15ms, 10.4MB)
# 테스트 7 〉	통과 (2.21ms, 10.4MB)
# 테스트 8 〉	통과 (2.26ms, 10.2MB)
# 테스트 9 〉	통과 (2.96ms, 10.3MB)
# 테스트 10 〉	통과 (4.89ms, 10.4MB)
# 효율성  테스트
# 테스트 1 〉	통과 (878.49ms, 144MB)
# 테스트 2 〉	통과 (868.24ms, 144MB)
# 테스트 3 〉	통과 (873.08ms, 144MB)
# 테스트 4 〉	통과 (855.59ms, 144MB)
# 테스트 5 〉	통과 (661.82ms, 133MB)
# 테스트 6 〉	통과 (680.12ms, 133MB)
# 테스트 7 〉	통과 (683.16ms, 133MB)