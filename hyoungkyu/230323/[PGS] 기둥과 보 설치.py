def check(answer):
    for x, y, a in answer:
        if a == 0: #기둥 체크
            #'바닥 위' or '보의 한쪽 끝 위' or '또 다른 기둥 위' 
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif a == 1: #보 체크
            #'한쪽 끝 부분이 기둥 위' or '양쪽 끝 부분이 다른 보와 동시 연결'
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, a, b = build
        if b == 1: # 설치
            answer.append([x, y, a])
            if not check(answer): 
                answer.remove([x, y, a])
        elif b == 0: # 삭제
            answer.remove([x, y, a])
            if not check(answer): 
                answer.append([x, y, a])
    
    return sorted(answer)

'''
테스트 1 〉	통과 (0.05ms, 10.1MB)
테스트 2 〉	통과 (0.09ms, 10.1MB)
테스트 3 〉	통과 (0.07ms, 10.2MB)
테스트 4 〉	통과 (0.22ms, 10.3MB)
테스트 5 〉	통과 (0.23ms, 10.3MB)
테스트 6 〉	통과 (1.43ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.07ms, 10.2MB)
테스트 9 〉	통과 (0.06ms, 10.2MB)
테스트 10 〉	통과 (342.05ms, 10.3MB)
테스트 11 〉	통과 (2331.18ms, 10.5MB)
테스트 12 〉	통과 (265.33ms, 10.4MB)
    테스트 13 〉	통과 (2488.30ms, 10.6MB)
테스트 14 〉	통과 (236.75ms, 10.4MB)
테스트 15 〉	통과 (2552.36ms, 10.6MB)
테스트 16 〉	통과 (247.90ms, 10.4MB)
테스트 17 〉	통과 (2375.90ms, 10.4MB)
테스트 18 〉	통과 (1538.98ms, 10.4MB)
테스트 19 〉	통과 (1567.34ms, 10.4MB)
테스트 20 〉	통과 (1795.97ms, 10.5MB)
테스트 21 〉	통과 (1994.62ms, 10.3MB)
테스트 22 〉	통과 (1571.39ms, 10.5MB)
테스트 23 〉	통과 (2001.44ms, 10.5MB)
'''


# def beam_check(x, y, b, arr):
#     # 보 설치 체크
#     if b == 1:
#         if arr[x][y] // 10 or arr[x][y+1] // 10:
#             return True
#         elif arr[x][y] % 10 and arr[x][y+1] % 10:
#             return True
#         return False
        
#     # 보 삭제 체크
#     else:
#         # 보의 한쪽 위에 기둥이 있는 경우
#         if 0 < x and ((not arr[x][y] // 10 and arr[x-1][y] // 10) or (not arr[x][y+1] // 10 and arr[x-1][y+1] // 10)):
#             return False
#         # 보 사이에 꼈을 때
#         elif arr[x][y] == 4 and arr[x][y+1] == 4 and (not arr[x][y-1] // 10 or not arr[x][y+2] // 10):
#             return False
#         # 왼쪽에만 기둥이 있을 때
#         elif arr[x][y] // 10 and arr[x][y+1] == 4 and not arr[x][y+2] // 10:
#             return False
#         # 오른쪽에만 기둥이 있을 때
#         elif arr[x][y+1] // 10 and arr[x][y] == 4 and not arr[x][y-1] // 10:
#             return False
#         return True
        
# def column_check(x, y, b, n, arr):
#     # 기둥 설치 체크
#     if b == 1:
#         if x == n:
#             return True
#         elif arr[x][y] // 10 or arr[x][y] % 2:
#             return True
#         return False
    
#     # 기둥 삭제 체크
#     else:
#         # 기둥만 연속으로 붙은 경우
#         if arr[x-1][y] == 10 and 2 <= x and arr[x-2][y] // 10:
#             return False
#         # 기둥 위에 보가 있는 경우
#         elif arr[x-1][y] % 10:
#             # 보가 오른쪽으로 하나인 경우
#             if arr[x-1][y] % 10 == 1 and not arr[x-1][y+1] // 10:
#                 return False
#             # 보가 왼쪽으로 하나인 경우
#             elif arr[x-1][y] % 10 == 3 and not arr[x-1][y-1] // 10:
#                 return False
#             # 보가 양쪽으로 있는 경우
#             elif arr[x-1][y] % 10 == 4:
#                 if arr[x-1][y-1] != 4 and not arr[x-1][y-1] // 10:
#                     return False
#                 elif arr[x-1][y+1] != 4 and not arr[x-1][y+1] // 10:
#                     return False
#         return True
                

# def beam(x, y, a, b, n, arr):
#     if b == 1 and beam_check(x, y, b, arr):
#         arr[x][y] += 1
#         arr[x][y+1] += 3
#         return [y, n-x, a]
#     elif b == 0 and beam_check(x, y, b, arr):
#         arr[x][y] -= 1
#         arr[x][y+1] -= 3
#         return [y, n-x, a]
#     return []

# def column(x, y, a, b, n, arr):
#     if b == 1 and column_check(x, y, b, n, arr):
#         arr[x-1][y] += 10
#         return [y, n-x, a]
#     elif b == 0 and column_check(x, y, b, n, arr):
#         arr[x-1][y] -= 10
#         return [y, n-x, a]
#     return []

# def solution(n, build_frame):
#     # a : 0 - 기둥, 1 - 보
#     # b : 0 - 삭제, 1 - 설치
#     answer = []
#     arr = [[0] * (n+1) for _ in range(n+1)]
#     for frame in build_frame:
#         x, y, a, b = frame
#         y = n - y
#         if a == 1:
#             tmp = beam(y, x, a, b, n, arr)
#             if tmp:
#                 if b == 1:
#                     answer.append(tmp) 
#                 elif b == 0 and tmp in answer: 
#                     answer.pop(answer.index(tmp))
#         else:
#             tmp = column(y, x, a, b, n, arr)
#             if tmp:
#                 if b == 1:
#                     answer.append(tmp) 
#                 elif b == 0 and tmp in answer: 
#                     answer.pop(answer.index(tmp))

#     return sorted(answer)