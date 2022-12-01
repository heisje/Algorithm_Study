
def solution(m, n, board):
    answer = 0
    removed = 0
    matrix = []
    for i in range(m):
        temp = list(board[i])
        matrix.append(temp)
    check_matrix = [[1 for _ in range(n)] for __ in range(m)]
    while True:
        """
        for i in range(m):
            print(matrix[i])
        """
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
        """
        for i in range(m):
            print(check_matrix[i])
        """
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
                """
                if check_matrix[i][j] == 0:
                    check_matrix[i][j] = check_matrix[i - 1][j]
                    check_matrix[i - 1][j] = 0
                    matrix[i][j] = matrix[i - 1][j]
                    matrix[i - 1][j] = 0
                

        for i in range(m):
            print(matrix[i])
        print("---")
        """
        if did_have_same == 0:
            break
    return removed

sol = solution(6, 6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
print(sol)