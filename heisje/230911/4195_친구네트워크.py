# 276ms
import sys
input = sys.stdin.readline
# 유니온 파인드
def solution():

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a = find(a)
        b = find(b)

        if a != b:
            parent[b] = a
            number[a] += number[b]
        print(number[a])

    parent = dict()
    number = dict()
    for _ in range(int(input())):
        f1, f2 = input().split()
        if f1 not in parent:
            parent[f1] = f1
            number[f1] = 1
        if f2 not in parent:
            parent[f2] = f2
            number[f2] = 1
        union(f1, f2)

for _ in range(int(input())):
    solution()
    

'''
from collections import defaultdict
TC = int(input())
answer = ''
for _ in range(TC):
    F = int(input())
    friends = defaultdict(int)
    groups = [set()]
    
    for _ in range(F):
        f1, f2 = input().split()
        
        if friends[f1] == 0 and friends[f2] == 0:   # 둘다 그룹이 없을때
            # 그룹 생성 후 넣기
            groups.append(set())
            groups[-1].add(f1)
            groups[-1].add(f2)
            friends[f1] = len(groups) - 1
            friends[f2] = len(groups) - 1

        elif friends[f1] == 0 and friends[f2] > 0:   # f2만 그룹이 있을때
            # f1을 f2그룹에 넣기
            groups[friends[f2]].add(f1)
            friends[f1] = friends[f2]

        elif friends[f1] > 0 and friends[f2] == 0:  # f1만 그룹이 있을때
            # f2를 f1그룹에 넣기
            groups[friends[f1]].add(f2)
            friends[f2] = friends[f1]

        else:
            # f1과 f2그룹 합하기
            groups[friends[f1]].update(groups[friends[f2]])
            for name in groups[friends[f2]]:
                friends[name] = friends[f1]
        
        answer += str(len(groups[friends[f1]])) + "\n"
        
print(answer.strip())
'''