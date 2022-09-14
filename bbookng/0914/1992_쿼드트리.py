import sys
input = lambda: sys.stdin.readline().strip()

def solution(arr):
    K = len(arr)
    if K == 1:
        return arr[0][0]

    arr1 = [arr[i][:K//2] for i in range(K//2)]
    arr2 = [arr[i][K//2:] for i in range(K//2)]
    arr3 = [arr[i][:K//2] for i in range(K//2,K)]
    arr4 = [arr[i][K//2:] for i in range(K//2,K)]

    s1 = solution(arr1)
    s2 = solution(arr2)
    s3 = solution(arr3)
    s4 = solution(arr4)

    if s1 == s2 == s3 == s4 and s1.isnumeric():
        return s1

    else:
        return f'({s1}{s2}{s3}{s4})'


n = int(input())
arr = [list(input()) for _ in range(n)]
print(solution(arr))

