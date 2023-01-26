def solution(user_id, banned_id):
    candidate = [[] for _ in range(len(banned_id))]
    contained, possible = [], []
    
    for idx, banned in enumerate(banned_id):
        for user in user_id:
            if len(banned) != len(user):
                continue
            for al in range(len(banned)):
                if banned[al] != '*' and banned[al] != user[al]:
                    break
            else:
                candidate[idx].append(user)

    for c in candidate[0]:
        contained.append(([c], 0))

    while contained:
        arr, cnt = contained.pop()
        if cnt == len(banned_id) - 1:
            arr.sort()
            possible.append(tuple(arr))
            continue
        
        for e in candidate[cnt + 1]:
            if e not in arr:
                contained.append((arr[:] + [e], cnt+1))
        
    return len(set(possible))


# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.04ms, 10.1MB)
# 테스트 4 〉	통과 (0.03ms, 10.2MB)
# 테스트 5 〉	통과 (111.93ms, 14.9MB)
# 테스트 6 〉	통과 (0.98ms, 10.3MB)
# 테스트 7 〉	통과 (0.04ms, 10.4MB)
# 테스트 8 〉	통과 (0.07ms, 10.4MB)
# 테스트 9 〉	통과 (0.04ms, 10.2MB)
# 테스트 10 〉	통과 (0.04ms, 10.4MB)
# 테스트 11 〉	통과 (0.04ms, 10.3MB)