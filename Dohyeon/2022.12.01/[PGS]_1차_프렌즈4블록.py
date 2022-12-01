
def solution(m, n, board):
    answer = 0
    removed = 0
    matrix = []
    for i in range(m):
        temp = list(board[i])
        matrix.append(temp)
    check_matrix = [[1 for _ in range(n)] for __ in range(m)]
    while True:

        did_have_same = 0
        for i in range(m - 1):
            for j in range(n -1):
                initial = matrix[i][j]
                if initial == 0:
                    continue
                isSame = True
                #print(i, j)
                for m_i in range(2):
                    for m_j in range(2):
                        if matrix[i + m_i][j + m_j] != initial:
                            isSame = False
                #print(isSame)
                if isSame:
                    did_have_same = 1
                    removed += 4
                    for m_i in range(2):
                        for m_j in range(2):
                            if check_matrix[i + m_i][j + m_j] == 0:
                                removed -= 1
                            else:
                                check_matrix[i + m_i][j + m_j] = 0
                                #matrix[i + m_i][j + m_j] = 0

        for i in range(m):
            for j in range(n):
                if check_matrix[i][j] == 0:
                    matrix[i][j] = 0

        for j in range(n):
            for i in range(m - 1, 0, -1):
                if check_matrix[i][j] == 0:
                    for k in range(i - 1, -1, -1):
                        if check_matrix[k][j] == 0:
                            continue
                        else:
                            check_matrix[i][j] = check_matrix[k][j]
                            check_matrix[k][j] = 0
                            matrix[i][j] = matrix[k][j]
                            matrix[k][j] = 0
                            break
                    else:
                        break

        if did_have_same == 0:
            break
    return removed

sol = solution(6, 6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
print(sol)

"""
테스트 1 〉	통과 (0.06ms, 10.2MB)
테스트 2 〉	통과 (0.10ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (1.95ms, 10.2MB)
테스트 5 〉	통과 (123.97ms, 10.3MB)
테스트 6 〉	통과 (10.31ms, 10.2MB)
테스트 7 〉	통과 (1.12ms, 10.2MB)
테스트 8 〉	통과 (1.98ms, 10.3MB)
테스트 9 〉	통과 (0.08ms, 10.2MB)
테스트 10 〉	통과 (1.14ms, 10.2MB)
테스트 11 〉	통과 (2.37ms, 10.2MB)
"""