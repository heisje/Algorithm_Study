# Lv2
def DFS(places, idx):
    D = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for i in range(5):
        for j in range(5):
            if places[idx][i][j] != "P":
                continue
            visited = list([0]*5 for _ in range(5))
            stack = []
            ci, cj = i, j
            visited[ci][cj] = 1
            cnt = 1
            while True:
                if cnt < 3:
                    for di, dj in D:
                        ni, nj = ci+di, cj+dj
                        if 0<=ni<5 and 0<=nj<5 and visited[ni][nj] == 0:
                            if places[idx][ni][nj] == "O":
                                cnt += 1
                                visited[ni][nj] = cnt
                                stack.append([ci, cj])
                                ci, cj = ni, nj
                                break
                            elif places[idx][ni][nj] == "P":
                                return 0
                    else:
                        if stack:
                            pos = stack.pop()
                            ci, cj = pos[0], pos[1]
                            cnt -= 1
                        else:
                            break
                else:
                    if stack:
                        pos = stack.pop()
                        ci, cj = pos[0], pos[1]
                        cnt -= 1
                    else:
                        break
    return 1

def solution(places):
    answer = []
    for i in range(5):
        answer.append(DFS(places, i))
    
    return answer

'''
테스트 1 〉통과 (0.13ms, 10.4MB)    #
테스트 2 〉통과 (0.05ms, 10.3MB)
테스트 3 〉통과 (0.05ms, 10.2MB)
테스트 4 〉통과 (0.05ms, 10.4MB)
테스트 5 〉통과 (0.06ms, 10.2MB)
테스트 6 〉통과 (0.10ms, 10.2MB)
테스트 7 〉통과 (0.07ms, 10.2MB)
테스트 8 〉통과 (0.08ms, 10.2MB)
테스트 9 〉통과 (0.06ms, 10.3MB)
테스트 10 〉통과 (0.03ms, 10.4MB)
테스트 11 〉통과 (0.07ms, 10.2MB)
테스트 12 〉통과 (0.05ms, 10.2MB)
테스트 13 〉통과 (0.06ms, 10.2MB)
테스트 14 〉통과 (0.10ms, 10.2MB)
테스트 15 〉통과 (0.03ms, 10.4MB)
테스트 16 〉통과 (0.06ms, 10.2MB)
테스트 17 〉통과 (0.07ms, 10.2MB)
테스트 18 〉통과 (0.05ms, 10.3MB)
테스트 19 〉통과 (0.10ms, 10.2MB)
테스트 20 〉통과 (0.06ms, 10.3MB)
테스트 21 〉통과 (0.03ms, 10.2MB)
테스트 22 〉통과 (0.05ms, 10.4MB)
테스트 23 〉통과 (0.02ms, 10.4MB)
테스트 24 〉통과 (0.02ms, 10.2MB)
테스트 25 〉통과 (0.02ms, 10.2MB)
테스트 26 〉통과 (0.02ms, 10.2MB)
테스트 27 〉통과 (0.09ms, 10.4MB)
테스트 28 〉통과 (0.06ms, 10.3MB)
테스트 29 〉통과 (0.06ms, 10.3MB)
테스트 30 〉통과 (0.04ms, 10.2MB)
테스트 31 〉통과 (0.07ms, 10.4MB)
'''