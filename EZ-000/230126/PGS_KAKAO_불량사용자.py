import re
from itertools import permutations


def solution(user_id, banned_id):
    answer = []
    r = len(banned_id)
    perms = list(map(list, permutations(user_id, r)))
    banned_id = [re.sub('\*', '.', id) for id in banned_id]

    for perm in perms:
        for i in range(r):
            temp = re.match('^' + banned_id[i] + '$', perm[i])
            if not temp:
                break
        else:
            perm.sort()
            if perm not in answer:
                answer.append(perm)

    return len(answer)


# 테스트 1 〉	통과 (0.09ms, 10.3MB)
# 테스트 2 〉	통과 (1.24ms, 10.1MB)
# 테스트 3 〉	통과 (0.44ms, 10.3MB)
# 테스트 4 〉	통과 (0.33ms, 10.1MB)
# 테스트 5 〉	통과 (274.78ms, 15.4MB)
# 테스트 6 〉	통과 (38.59ms, 12.4MB)
# 테스트 7 〉	통과 (2.34ms, 10.4MB)
# 테스트 8 〉	통과 (1.34ms, 10.2MB)
# 테스트 9 〉	통과 (3.01ms, 10.3MB)
# 테스트 10 〉 통과 (51.71ms, 15.3MB)
# 테스트 11 〉 통과 (3.61ms, 10.3MB)
