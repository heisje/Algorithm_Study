import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(list(set(nums)))
compress = {}       # dictionary 탐색 속도가 리스트보다 훨씬 빠르다!

for idx, num in enumerate(sorted_nums):
    compress[num] = idx

for num in nums:
    print(compress[num], end=' ')

'''참고
https://www.acmicpc.net/board/view/72041
'''
