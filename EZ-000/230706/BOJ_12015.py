import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

lis = [0]

for a in A:
    if lis[-1] < a:
        lis.append(a)
    else:
        start = 0
        end = len(lis)

        while start < end:
            mid = (start + end) // 2
            if lis[mid] < a:
                start = mid + 1
            else:
                end = mid
        lis[end] = a

print(len(lis) - 1)
