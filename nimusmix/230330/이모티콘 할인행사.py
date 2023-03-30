from itertools import product

def solution(users, emoticons):
    ans = []
    
    for discount in product([10, 20, 30, 40], repeat=len(emoticons)):
        total_join, total_price = 0, 0
        
        for [s_ratio, s_price] in users:
            user_price = 0

            for idx, dc in enumerate(discount):
                if dc >= s_ratio:
                    user_price += emoticons[idx] * (100 - dc) // 100
                    
            if user_price >= s_price:
                total_join += 1
            else:
                total_price += user_price
        
        ans.append((total_join, total_price))
    ans.sort(reverse=True)

    return ans[0]


# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.07ms, 10.1MB)
# 테스트 3 〉	통과 (0.33ms, 10.3MB)
# 테스트 4 〉	통과 (1.62ms, 10.2MB)
# 테스트 5 〉	통과 (3.03ms, 10.2MB)
# 테스트 6 〉	통과 (1.55ms, 10.2MB)
# 테스트 7 〉	통과 (14.99ms, 10.2MB)
# 테스트 8 〉	통과 (7.82ms, 10.3MB)
# 테스트 9 〉	통과 (81.80ms, 10.4MB)
# 테스트 10 〉	통과 (33.25ms, 10.5MB)
# 테스트 11 〉	통과 (447.88ms, 10.4MB)
# 테스트 12 〉	통과 (184.34ms, 11.6MB)
# 테스트 13 〉	통과 (1755.99ms, 11.7MB)
# 테스트 14 〉	통과 (1577.97ms, 11.6MB)
# 테스트 15 〉	통과 (67.54ms, 10.3MB)
# 테스트 16 〉	통과 (68.94ms, 10.3MB)
# 테스트 17 〉	통과 (0.55ms, 10.3MB)
# 테스트 18 〉	통과 (24.08ms, 10.2MB)
# 테스트 19 〉	통과 (0.04ms, 10.2MB)
# 테스트 20 〉	통과 (0.04ms, 10.2MB)