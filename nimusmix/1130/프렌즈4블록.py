def solution(m, n, board):
    new = [list(i) for i in board]
    ans = 0

    while True:
        pop_list = []
        
        for i in range(m-1):
            for j in range(n-1):
                if new[i][j] and new[i][j] == new[i+1][j] == new[i][j+1] == new[i+1][j+1]:
                    pop_list.append((i, j))
                    pop_list.append((i+1, j))
                    pop_list.append((i, j+1))
                    pop_list.append((i+1, j+1))

        if pop_list:
            pop_list = set(pop_list)
            ans += len(pop_list)
        else:
            return ans
        
        for i, j in pop_list:
            new[i][j] = ''
        
        for i in range(m-1, 0, -1):
            for j in range(n-1, -1, -1):
                if new[i][j] == '':
                    for num in range(1, i+1):
                        if new[i-num][j] != '':
                            new[i][j] = new[i-num][j]
                            new[i-num][j] = ''
                            break


# 테스트 1 〉	통과 (0.03ms, 10.5MB)
# 테스트 2 〉	통과 (0.06ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (1.90ms, 10.4MB)
# 테스트 5 〉	통과 (149.05ms, 10.2MB)
# 테스트 6 〉	통과 (9.41ms, 10.3MB)
# 테스트 7 〉	통과 (0.90ms, 10.3MB)
# 테스트 8 〉	통과 (3.61ms, 10.2MB)
# 테스트 9 〉	통과 (0.03ms, 10.3MB)
# 테스트 10 〉	통과 (1.22ms, 10.3MB)
# 테스트 11 〉	통과 (4.47ms, 10.5MB)