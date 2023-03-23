# a = 0: 기둥 / 1: 보
# b = 0: 삭제 / 1: 설치

def check(ans):
    for x, y, a in ans:
        # case 기둥
        if a == 0:
            if y == 0 or [x-1, y, 1] in ans or [x, y, 1] in ans or [x, y-1, 0] in ans:
                continue
            return False
        # case 보
        else:
            if [x, y-1, 0] in ans or [x+1, y-1, 0] in ans or ([x-1, y, 1] in ans and [x+1, y, 1] in ans):
                continue
            return False
    return True


def solution(n, build_frame):
    ans = []
    for [x, y, a, b] in build_frame:
        # case 설치
        if b == 1:
            ans.append([x, y, a])
            if not check(ans):
                ans.pop()
        # case 삭제
        else:
            ans.remove([x, y, a])
            if not check(ans):
                ans.append([x, y, a])
                
    ans.sort()
    return ans


# 정확성  테스트
# 테스트 1 〉	통과 (0.05ms, 10.3MB)
# 테스트 2 〉	통과 (0.08ms, 10.1MB)
# 테스트 3 〉	통과 (0.11ms, 10.2MB)
# 테스트 4 〉	통과 (0.34ms, 10.3MB)
# 테스트 5 〉	통과 (0.27ms, 10.3MB)
# 테스트 6 〉	통과 (1.44ms, 10.3MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.12ms, 10.1MB)
# 테스트 9 〉	통과 (0.06ms, 10.1MB)
# 테스트 10 〉	통과 (357.40ms, 10.3MB)
# 테스트 11 〉	통과 (2264.99ms, 10.5MB)
# 테스트 12 〉	통과 (290.85ms, 10.3MB)
# 테스트 13 〉	통과 (2366.82ms, 10.6MB)
# 테스트 14 〉	통과 (266.23ms, 10.5MB)
# 테스트 15 〉	통과 (2277.22ms, 10.6MB)
# 테스트 16 〉	통과 (273.18ms, 10.3MB)
# 테스트 17 〉	통과 (2172.16ms, 10.5MB)
# 테스트 18 〉	통과 (1348.33ms, 10.4MB)
# 테스트 19 〉	통과 (1530.89ms, 10.5MB)
# 테스트 20 〉	통과 (1373.10ms, 10.4MB)
# 테스트 21 〉	통과 (1914.05ms, 10.3MB)
# 테스트 22 〉	통과 (1501.41ms, 10.3MB)
# 테스트 23 〉	통과 (1544.48ms, 10.4MB)