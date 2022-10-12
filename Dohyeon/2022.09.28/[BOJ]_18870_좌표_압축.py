import sys

input = lambda: sys.stdin.readline().strip()

N = int(input())
arr = list(map(int, input().split()))
num_dict = {}
base = arr[0]
for i in range(len(arr)):               # base와의 차이를 키값, 밸류는 인덱스 값으로하는 딕셔너리 제작
    try:
        num_dict[arr[i] - base].append(i)
    except KeyError:
        num_dict[arr[i] - base] = [i]

gap_list = list(num_dict.keys())        # 키값에 대한 리스트를 만든 후 이를 정렬해 준다.
gap_list.sort()

now = 0
for i in gap_list:
    for j in num_dict[i]:               # 키를 넣어 거기에 해당하는 인덱스를 이용, 순서대로 값을 넣어준다.
        arr[j] = now
    now += 1
print(*arr)
