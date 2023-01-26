l = [-1] * 17
r = [-1] * 17
n = 0
val = []
answer = 1
vis = [0] * (1 << 17)


def sheep(s):
    global answer
    if vis[s]:
        return None
    vis[s] = 1
    wolf, vertex = 0, 0
    for i in range(n):
        if s & (1 << i):
            vertex += 1
            wolf += val[i]
    if vertex <= wolf * 2:
        return None
    answer = max(answer, vertex - wolf)

    for i in range(n):
        if not s & (1 << i):
            continue
        if l[i] != -1:
            sheep(s | (1 << l[i]))
        if r[i] != -1:
            sheep(s | 1 << r[i])


def solution(info, edges):
    global n, val
    n = len(info)
    val = info[:]
    for u, v in edges:
        if l[u] == -1:
            l[u] = v
        else:
            r[u] = v
    sheep(1)
    return answer

# 참고: https://blog.encrypted.gg/1029

# 테스트 1 〉	통과 (0.01ms, 10.9MB)
# 테스트 2 〉	통과 (0.28ms, 10.8MB)
# 테스트 3 〉	통과 (0.02ms, 10.8MB)
# 테스트 4 〉	통과 (0.01ms, 10.6MB)
# 테스트 5 〉	통과 (0.20ms, 11MB)
# 테스트 6 〉	통과 (0.19ms, 11MB)
# 테스트 7 〉	통과 (0.16ms, 10.9MB)
# 테스트 8 〉	통과 (0.22ms, 10.8MB)
# 테스트 9 〉	통과 (0.45ms, 10.7MB)
# 테스트 10 〉 통과 (0.84ms, 10.9MB)
# 테스트 11 〉 통과 (0.62ms, 10.9MB)
# 테스트 12 〉 통과 (1.12ms, 10.9MB)
# 테스트 13 〉 통과 (0.15ms, 10.8MB)
# 테스트 14 〉 통과 (0.35ms, 10.8MB)
# 테스트 15 〉 통과 (0.63ms, 10.9MB)
# 테스트 16 〉 통과 (0.53ms, 10.9MB)
# 테스트 17 〉 통과 (1.30ms, 10.7MB)
# 테스트 18 〉 통과 (0.21ms, 11MB)
