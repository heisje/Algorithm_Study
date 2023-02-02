import re

def solution(user_id, banned_id):
    global answered

    answered = []
    bans = []

    for ban in banned_id:
        l = len(ban)
        ban = ban.replace('*','.')
        p = re.compile\
            (ban)
        bans.append((l, p))

    def backtracking(i, visited):
        global answered

        if i == len(banned_id):
            if visited not in answered:
                answered.append(visited)
            return

        for j in range(len(user_id)):
            print(bans[j])
            if not (1 << j) & visited and bans[i][1].match(user_id[j]) and bans[i][0] == len(user_id[j]):
                visited += 2 ** j
                backtracking(i+1, visited)
                visited -= 2 ** j

    backtracking(0, 0)

    answer = len(answered)
    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))

'''
테스트 1 〉	통과 (0.08ms, 10.2MB)
테스트 2 〉	통과 (0.17ms, 10.2MB)
테스트 3 〉	통과 (0.14ms, 10.3MB)
테스트 4 〉	통과 (0.15ms, 10.2MB)
테스트 5 〉	통과 (138.19ms, 10.2MB)
테스트 6 〉	통과 (1.62ms, 10.2MB)
테스트 7 〉	통과 (0.17ms, 9.93MB)
테스트 8 〉	통과 (0.30ms, 10.2MB)
테스트 9 〉	통과 (0.32ms, 10.2MB)
테스트 10 〉	통과 (0.26ms, 10MB)
테스트 11 〉	통과 (0.24ms, 10.2MB)
'''