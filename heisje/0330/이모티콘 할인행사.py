from copy import deepcopy

def solution(users, emoticons):
    answer = []
    # 이모티콘의 가격을 전부 10% 20% 30% 40%로 만든다
    sale_prices = [[y * (100 - x) / 100 for x in (10, 20, 30, 40) ]for y in emoticons]
    # (100 - x) / 100 * y // 오답 (13, 15, 18)
    # (100 - x) * y / 100 // 정답
    # y * (100 - x) / 100 // 정답
    # (100 - x) * 0.01 * y // 정답
    
    permutations = []
    def makePermutations(n, N, per):
        if n == N:
            permutations.append(per)
            return 
        for i in (0, 1, 2, 3):
            makePermutations(n+1, N, per+[i])
    makePermutations(0, len(emoticons), [])
    
    max_result = [0, 0]
    for pers in permutations:
        result = [0, 0]
        copy_users = deepcopy(users)
        copy_users_money = [0] * len(users)
        for emo_idx, p in enumerate(pers):
            for user_idx, _ in enumerate(copy_users):
                # 할인폭이 크면 산다
                if copy_users[user_idx][0] <= (p + 1) * 10:
                    # + 일 경우
                    if copy_users[user_idx][1] > 0:
                        copy_users[user_idx][1] -= sale_prices[emo_idx][p]
                        copy_users_money[user_idx] += sale_prices[emo_idx][p]
                        if copy_users[user_idx][1] <= 0: # 부호 주의
                            result[0] += 1
                            copy_users_money[user_idx] = 0
        
        result[1] = sum(copy_users_money)
        if max_result[0] < result[0]:
            max_result = result[:]
        elif max_result[0] == result[0]:
            if max_result[1] < result[1]:
                max_result = result[:]
                
    return max_result

#     테스트 1 〉	통과 (0.18ms, 10.2MB)
# 테스트 2 〉	통과 (0.44ms, 10.2MB)
# 테스트 3 〉	통과 (1.84ms, 10.4MB)
# 테스트 4 〉	통과 (8.10ms, 10.3MB)
# 테스트 5 〉	통과 (15.33ms, 10.3MB)
# 테스트 6 〉	통과 (7.29ms, 10.3MB)
# 테스트 7 〉	통과 (64.75ms, 10.2MB)
# 테스트 8 〉	통과 (32.32ms, 10.5MB)
# 테스트 9 〉	통과 (310.66ms, 10.4MB)
# 테스트 10 〉	통과 (136.15ms, 10.5MB)
# 테스트 11 〉	통과 (1295.84ms, 10.6MB)
# 테스트 12 〉	통과 (590.75ms, 12.3MB)
# 테스트 13 〉	통과 (5470.50ms, 12.3MB)
# 테스트 14 〉	통과 (4920.64ms, 12.2MB)
# 테스트 15 〉	통과 (322.78ms, 10.4MB)
# 테스트 16 〉	통과 (269.27ms, 10.4MB)
# 테스트 17 〉	통과 (3.52ms, 10.4MB)
# 테스트 18 〉	통과 (84.15ms, 10.5MB)
# 테스트 19 〉	통과 (0.26ms, 10.2MB)
# 테스트 20 〉	통과 (0.24ms, 10.5MB)