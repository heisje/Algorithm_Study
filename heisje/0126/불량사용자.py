import re

def solution(user_id, banned_id):
    # 정규 표현식으로 변환
    banneds = [] # 정규
    banneds_len = [] # 길이
    for user in banned_id:
        banneds.append(re.compile(user.replace('*', '\w')))
        banneds_len.append(len(user))

    # check에다가 banned_id가 몇 개 들어가는지 체크
    check = []
    for jdx in range(len(banneds)):
        tmp = []
        for idx, user in enumerate(user_id):
            if len(user) == banneds_len[jdx] and banneds[jdx].match(user):
                tmp.append(idx)
        check.append(tmp)

    # dfs로 check_set에 결과저장
    check_set = set()
    def deep(N, n, visited, li):
        if n == N:
            # 결과를 텍스트로 바꿔서 set에 저장
            check_set.add(' '.join(sorted(map(str, list(li)))))
            return
        for c in check[n]:
            if c not in visited:
                visited.add(c)
                li.add(c)
                deep(N, n+1, visited, li)
                visited.discard(c)
                li.discard(c)
    
    deep(len(check),0,set(),set())
    for c in check:
        pass
    return len(check_set)

a = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b = ["fr*d*", "abc1**"]
print(solution(a,b))
a = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b = ["*rodo", "*rodo", "******"]
print(solution(a,b))
a = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b = ["fr*d*", "*rodo", "******", "******"]
print(solution(a,b))

# 테스트 1 〉	통과 (0.04ms, 10.1MB)
# 테스트 2 〉	통과 (0.15ms, 10.3MB)
# 테스트 3 〉	통과 (0.24ms, 10.2MB)
# 테스트 4 〉	통과 (0.29ms, 10.3MB)
# 테스트 5 〉	통과 (128.13ms, 10.3MB)
# 테스트 6 〉	통과 (1.34ms, 10.2MB)
# 테스트 7 〉	통과 (0.14ms, 10.2MB)
# 테스트 8 〉	통과 (0.20ms, 10.4MB)
# 테스트 9 〉	통과 (0.19ms, 10.2MB)
# 테스트 10 〉	통과 (0.33ms, 10.3MB)
# 테스트 11 〉	통과 (0.22ms, 10.3MB)