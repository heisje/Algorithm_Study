def matching(user, ban):
    for i in range(len(user)):
        if user[i] != ban[i] and ban[i] != "*":
            return False
    return True

def solution(user_id, banned_id):
    answer = 0
    visited = [0] * len(user_id)
    res = []
    
    def func(user_id, banned_id, idx):
        if idx == len(banned_id):
            if sum(visited) == len(banned_id) and visited not in res:
                res.append(visited[:])
            return
        for i in range(len(user_id)):
            if not visited[i] and len(user_id[i]) == len(banned_id[idx]) and matching(user_id[i], banned_id[idx]):
                visited[i] = 1
                func(user_id, banned_id, idx+1)
                visited[i] = 0

    func(user_id, banned_id, 0)
    # print(len(res), res)
    return len(res)

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.07ms, 10.2MB)
테스트 3 〉	통과 (0.10ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (168.59ms, 10.2MB)
테스트 6 〉	통과 (3.49ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.4MB)
테스트 8 〉	통과 (0.05ms, 10.2MB)
테스트 9 〉	통과 (0.09ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.13ms, 10.4MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''