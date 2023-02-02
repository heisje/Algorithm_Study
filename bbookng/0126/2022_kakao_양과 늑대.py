def solution(info, edges):
    visited = [0] * len(info)
    answer = []

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for parent, child in edges:

            if visited[parent] and not visited[child]:
                visited[child] = 1
                if info[child] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[child] = 0

    visited[0] = 1
    dfs(1, 0)

    return max(answer)

'''
테스트 1 〉	통과 (0.00ms, 7.67MB)
테스트 2 〉	통과 (0.21ms, 7.63MB)
테스트 3 〉	통과 (0.01ms, 7.71MB)
테스트 4 〉	통과 (0.01ms, 7.73MB)
테스트 5 〉	통과 (0.32ms, 7.68MB)
테스트 6 〉	통과 (0.17ms, 7.59MB)
테스트 7 〉	통과 (0.05ms, 7.63MB)
테스트 8 〉	통과 (0.03ms, 7.69MB)
테스트 9 〉	통과 (0.33ms, 7.67MB)
테스트 10 〉	통과 (9.13ms, 7.6MB)
테스트 11 〉	통과 (0.12ms, 7.75MB)
테스트 12 〉	통과 (0.88ms, 7.81MB)
테스트 13 〉	통과 (0.03ms, 7.67MB)
테스트 14 〉	통과 (0.10ms, 7.77MB)
테스트 15 〉	통과 (0.36ms, 7.64MB)
테스트 16 〉	통과 (0.65ms, 7.62MB)
테스트 17 〉	통과 (21.62ms, 7.72MB)
테스트 18 〉	통과 (0.56ms, 7.67MB)
'''