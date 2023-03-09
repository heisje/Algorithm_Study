# def move(idx, command, array, num, dic):
#     cnt = 0
#     if command == "U":
#         while True:
#             idx -= 1
#             if array[idx]:
#                 cnt += 1
#                 if cnt == num:
#                     return idx
#     elif command == "D":
#         while True:
#             idx += 1
#             if array[idx]:
#                 cnt += 1
#                 if cnt == num:
#                     return idx

# def solution(n, k, cmd):
#     answer = ''
#     array = [1] * n
#     idx = k
#     stack = []
#     dic = {}
#     for lst in cmd:
#         if len(lst) > 1:
#             order, num = lst.split(' ')
#             idx = move(idx, order, array, int(num), dic)
#         elif lst[0] == "C":
#             stack.append(idx)
#             array[idx] = 0
#             if idx == n-1:
#                 idx = move(idx, "U", array, 1, dic)
#             else:
#                 idx = move(idx, "D", array, 1, dic)
#         else:
#             tmp_idx = stack.pop()
#             array[tmp_idx] = 1
            
#     for num in array:
#         answer += "O" if num else "X"
        
#     return answer

def solution(n, k, cmd):
    answer = ''
    array = [[False, idx-1, idx+1] for idx in range(n)] # 삭제 유무, 위쪽, 아래쪽
    idx = k
    stack = []
    for command in cmd:
        lst = list(command.split(' '))
        # 이동시키는 경우
        if len(lst) > 1:
            if lst[0] == "U":
                for _ in range(int(lst[1])):
                    idx = array[idx][1]
            else:
                for _ in range(int(lst[1])):
                    idx = array[idx][2]

        else:
            # 삭제시키는 경우
            if lst[0] == "C":
                # 스택에 추가
                stack.append(idx)

                # 삭제 체크
                array[idx][0] = True

                # 양 옆 좌, 우 좌표 갱신 (삭제된 좌표 뛰어넘기게)
                if array[idx][1] >= 0:
                    array[array[idx][1]][2] = array[idx][2]
                if array[idx][2] <= n-1:
                    array[array[idx][2]][1] = array[idx][1]

                # 인덱스 이동
                if array[idx][2] <= n-1:
                    idx = array[idx][2]
                else:
                    idx = array[idx][1]

            # 복구시키는 경우
            else:
                # 스택에서 빼옴
                tmp_idx = stack.pop()

                # 복구 체크
                array[tmp_idx][0] = False

                # 양 옆 좌, 우 좌표 갱신 (복구시킨 인덱스로)
                if array[tmp_idx][1] >= 0:
                    array[array[tmp_idx][1]][2] = tmp_idx
                if array[tmp_idx][2] <= n-1:
                    array[array[tmp_idx][2]][1] = tmp_idx

    for i in range(n):
        answer += 'X' if array[i][0] else 'O'
    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
# "OOOOXOOO"
print()

print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
# "OOXOXOOO"
print()

print(solution(8, 0, ["C", "C", "C", "C", "D 2", "C", "C", "Z", "Z", "C"]))
# "XXXXXOOX"
print()

'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.5MB)
테스트 2 〉	통과 (0.04ms, 10.5MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.04ms, 10.5MB)
테스트 5 〉	통과 (0.10ms, 10.4MB)
테스트 6 〉	통과 (0.10ms, 10.4MB)
테스트 7 〉	통과 (0.17ms, 10.5MB)
테스트 8 〉	통과 (0.10ms, 10.4MB)
테스트 9 〉	통과 (0.19ms, 10.6MB)
테스트 10 〉	통과 (0.10ms, 10.5MB)
테스트 11 〉	통과 (0.82ms, 10.4MB)
테스트 12 〉	통과 (0.61ms, 10.5MB)
테스트 13 〉	통과 (0.61ms, 10.5MB)
테스트 14 〉	통과 (1.04ms, 10.6MB)
테스트 15 〉	통과 (1.11ms, 10.5MB)
테스트 16 〉	통과 (1.13ms, 10.4MB)
테스트 17 〉	통과 (3.72ms, 10.5MB)
테스트 18 〉	통과 (3.68ms, 10.5MB)
테스트 19 〉	통과 (3.44ms, 10.4MB)
테스트 20 〉	통과 (2.28ms, 10.6MB)
테스트 21 〉	통과 (2.09ms, 10.5MB)
테스트 22 〉	통과 (1.99ms, 10.5MB)
테스트 23 〉	통과 (0.04ms, 10.4MB)
테스트 24 〉	통과 (0.03ms, 10.5MB)
테스트 25 〉	통과 (0.03ms, 10.5MB)
테스트 26 〉	통과 (0.03ms, 10.4MB)
테스트 27 〉	통과 (0.04ms, 10.4MB)
테스트 28 〉	통과 (0.09ms, 10.5MB)
테스트 29 〉	통과 (0.05ms, 10.5MB)
테스트 30 〉	통과 (0.05ms, 10.5MB)
효율성  테스트
테스트 1 〉	통과 (862.77ms, 176MB)
테스트 2 〉	통과 (843.48ms, 176MB)
    테스트 3 〉	통과 (862.83ms, 176MB)
테스트 4 〉	통과 (811.63ms, 182MB)
테스트 5 〉	통과 (758.49ms, 182MB)
테스트 6 〉	통과 (802.60ms, 182MB)
테스트 7 〉	통과 (211.63ms, 49.3MB)
테스트 8 〉	통과 (244.59ms, 60MB)
테스트 9 〉	통과 (802.50ms, 183MB)
테스트 10 〉	통과 (738.45ms, 183MB)
'''