def solution(user_id, banned_id):
    candidate = [0] * len(banned_id)
    contained = [[] for _ in range(len(banned_id))]
    
    for idx, banned in enumerate(banned_id):
        for user in user_id:
            if len(banned) != len(user):
                continue
            for al in range(len(banned)):
                if banned[al] != '*' and banned[al] != user[al]:
                    break
            else:
                if user not in contained:
                    contained[idx] += user
                    candidate[idx] += 1
                
    ans = 0 if sum(candidate) == 0 else 1
    for i in candidate:
        ans *= i
    
    return ans


# 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))

# 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))

# 3
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))