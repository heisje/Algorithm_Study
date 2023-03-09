
# 1 : 적의 공격
# 2 : 아군의 회복 스킬
# [type, r1, c1, r2, c2, degree]
def solution(board, skill):
    answer = 0
    d = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            d[r1][c1] -= degree
            d[r1][c2 + 1] += degree
            d[r2 + 1][c1] += degree
            d[r2 + 1][c2 + 1] -= degree

        if type == 2:
            d[r1][c1] += degree
            d[r1][c2+1] -= degree
            d[r2+1][c1] -= degree
            d[r2+1][c2+1] += degree

    for i in range(len(d)-1):
        for j in range(len(d[0])-1):
            d[i][j + 1] += d[i][j]

    for j in range(len(d[0]) - 1):
        for i in range(len(d) - 1):
            d[i + 1][j] += d[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += d[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer


print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (0.19ms, 10.2MB)
테스트 4 〉	통과 (0.42ms, 10.2MB)
테스트 5 〉	통과 (0.72ms, 10.2MB)
테스트 6 〉	통과 (1.28ms, 10.2MB)
테스트 7 〉	통과 (1.79ms, 10.2MB)
테스트 8 〉	통과 (2.19ms, 10.5MB)
테스트 9 〉	통과 (2.81ms, 10.2MB)
테스트 10 〉	통과 (7.62ms, 10.3MB)

효율성  테스트
테스트 1 〉	통과 (849.85ms, 143MB)
테스트 2 〉	통과 (857.79ms, 143MB)
테스트 3 〉	통과 (852.09ms, 143MB)
테스트 4 〉	통과 (755.32ms, 143MB)
테스트 5 〉	통과 (583.97ms, 132MB)
테스트 6 〉	통과 (606.80ms, 132MB)
테스트 7 〉	통과 (675.45ms, 132MB)
'''