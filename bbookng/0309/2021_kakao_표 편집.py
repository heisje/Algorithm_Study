def solution(n, k, cmd):
    nums = [[i, i-1, i+1] for i in range(n)]
    nums[-1][2] = -1

    deleted = []

    for command in cmd:
        # 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
        if 'U' in command:
            cmd, cnt = command.split()
            for i in range(int(cnt)):
                k = nums[k][1]
        # 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
        elif 'D' in command:
            cmd, cnt = command.split()
            for i in range(int(cnt)):
                k = nums[k][2]
        # 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다.
        # 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
        elif command == 'C':
            deleted.append(nums[k])
            nums[nums[k][1]][2] = nums[k][2]
            nums[nums[k][2]][1] = nums[k][1]
            if k == n-1:
                k = nums[k][1]
            else:
                k = nums[k][2]
        # 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
        elif command == 'Z':
            tmp = deleted.pop()
            nums[tmp[1]][2] = tmp[0]
            nums[tmp[2]][1] = tmp[0]

    answer = ['O'] * n
    for delete in deleted:
        answer[delete[0]] = 'X'
    answer = ''.join(answer)

    return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))

'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.5MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.13ms, 10.3MB)
테스트 6 〉	통과 (0.08ms, 10.3MB)
테스트 7 〉	통과 (0.12ms, 10.4MB)
테스트 8 〉	통과 (0.13ms, 10.4MB)
테스트 9 〉	통과 (0.08ms, 10.3MB)
테스트 10 〉	통과 (0.07ms, 10.3MB)
테스트 11 〉	통과 (0.40ms, 10.3MB)
테스트 12 〉	통과 (0.43ms, 10.5MB)
테스트 13 〉	통과 (0.48ms, 10.4MB)
테스트 14 〉	통과 (0.87ms, 10.4MB)
테스트 15 〉	통과 (0.89ms, 10.4MB)
테스트 16 〉	통과 (0.92ms, 10.3MB)
테스트 17 〉	통과 (3.46ms, 10.4MB)
테스트 18 〉	통과 (3.42ms, 10.4MB)
테스트 19 〉	통과 (3.19ms, 10.3MB)
테스트 20 〉	통과 (1.82ms, 10.4MB)
테스트 21 〉	통과 (1.93ms, 10.5MB)
테스트 22 〉	통과 (1.64ms, 10.5MB)
테스트 23 〉	통과 (0.04ms, 10.4MB)
테스트 24 〉	통과 (0.03ms, 10.4MB)
테스트 25 〉	통과 (0.03ms, 10.4MB)
테스트 26 〉	통과 (0.03ms, 10.3MB)
테스트 27 〉	통과 (0.04ms, 10.3MB)
테스트 28 〉	통과 (0.04ms, 10.4MB)
테스트 29 〉	통과 (0.04ms, 10.5MB)
테스트 30 〉	통과 (0.04ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (745.07ms, 214MB)
테스트 2 〉	통과 (743.22ms, 214MB)
테스트 3 〉	통과 (734.58ms, 214MB)
테스트 4 〉	통과 (722.18ms, 220MB)
테스트 5 〉	통과 (663.33ms, 220MB)
테스트 6 〉	통과 (651.34ms, 220MB)
테스트 7 〉	통과 (172.82ms, 57MB)
테스트 8 〉	통과 (190.53ms, 70.1MB)
테스트 9 〉	통과 (722.42ms, 221MB)
테스트 10 〉	통과 (712.92ms, 221MB)
'''