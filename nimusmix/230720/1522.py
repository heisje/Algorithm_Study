def sol(S):
    ans = 1e9
    a_cnt = S.count('a')
    S += S[:a_cnt - 1]
    
    for i in range(len(S) - (a_cnt - 1)):
        ans = min(ans, S[i:i+a_cnt].count('b'))
    return ans

print(sol(input()))