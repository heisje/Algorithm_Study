import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))                       # 중복 값 없애고 오름차순 정렬
dic = {arr2[i] : i for i in range(len(arr2))}       # 각 숫자를 key로 하고 arr2의 idx 를 value로 넣으면
print(dic)                                          # 크기 순서가 나옴 ( 크기 순서는 자신보다 작은 값의 갯수를 의미 )

for i in arr:                                       # 처음에 받은 array 의 각 요소들에 해당하는 값 출력
    print(dic[i], end = ' ')