from collections import deque

def BFS(n, m, x, y, r, c, k):
    D = [['d', 1, 0], ['l', 0, -1], ['r', 0, 1], ['u', -1, 0]]
    ci, cj = x, y
    que = deque()
    que.append(['', 0, ci, cj])
    res = []
    while que:
        cs, cnt, ci, cj = que.popleft()
        if ci == r and cj == c and cnt == k:
            res.append(cs)
            continue
        for ds, di, dj in D:
            ni, nj = ci+di, cj+dj
            # 이동한 곳에서 돌아갈 수 있으면 ㄱㄱ
            if 0<=ni<n and 0<=nj<m and abs(ni-r)+abs(nj-c)+cnt+1 <= k:
                que.append([cs+ds, cnt+1, ni, nj])
                break
    return res

def solution(n, m, x, y, r, c, k):
    answer = ''
    
    # 불가능 조건 : 거리차가 짝수거나 홀수일때 k도 짝수거나 홀수여야함, k 안에 들어와야됨
    if (abs(x-r)+abs(y-c)) % 2 != k % 2 or abs(x-r)+abs(y-c) > k: return 'impossible'
    answer = BFS(n, m, x-1, y-1, r-1, c-1, k)
    
    return answer[0]

print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))

'''
테스트 1 〉	통과 (0.08ms, 10.3MB)
테스트 2 〉	통과 (0.17ms, 10.4MB)
테스트 3 〉	통과 (0.00ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.4MB)
테스트 8 〉	통과 (0.03ms, 10.4MB)
테스트 9 〉	통과 (2.61ms, 10.4MB)
테스트 10 〉	통과 (3.49ms, 10.4MB)
    테스트 11 〉	통과 (3.55ms, 10.3MB)
테스트 12 〉	통과 (1.90ms, 10.2MB)
테스트 13 〉	통과 (1.91ms, 10.3MB)
테스트 14 〉	통과 (3.29ms, 10.4MB)
테스트 15 〉	통과 (1.85ms, 10.2MB)
테스트 16 〉	통과 (3.53ms, 10.2MB)
테스트 17 〉	통과 (2.29ms, 10.2MB)
테스트 18 〉	통과 (1.91ms, 10.2MB)
테스트 19 〉	통과 (1.92ms, 10.2MB)
테스트 20 〉	통과 (2.00ms, 10.4MB)
테스트 21 〉	통과 (1.92ms, 10.2MB)
테스트 22 〉	통과 (1.95ms, 10.2MB)
테스트 23 〉	통과 (1.91ms, 10.3MB)
테스트 24 〉	통과 (3.44ms, 10.3MB)
테스트 25 〉	통과 (2.12ms, 10.3MB)
테스트 26 〉	통과 (1.96ms, 10.3MB)
테스트 27 〉	통과 (1.83ms, 10.4MB)
테스트 28 〉	통과 (2.37ms, 10.2MB)
테스트 29 〉	통과 (2.11ms, 10.3MB)
테스트 30 〉	통과 (2.60ms, 10.2MB)
테스트 31 〉	통과 (0.00ms, 10.2MB)
'''