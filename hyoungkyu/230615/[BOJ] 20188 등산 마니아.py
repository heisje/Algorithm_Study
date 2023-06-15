# https://goodsosbva.tistory.com/101

from collections import deque

N = int(input())
adjL = [[] for _ in range(N+1)]
for _ in range(N-1):
    i, j = map(int, input().split())
    adjL[i].append(j)
    adjL[j].append(i)

class Node(object):
    def __init__(self, parent, childs, distance):
        self.parent = parent
        self.childs = childs
        self.distance = distance

class Cal(object):
    def __init__(self, node1, node2, Tree):
        self.node1 = node1
        self.node2 = node2
        self.Tree = Tree

    def find_distance(self):
        return self.Tree[self.node1].distance + self.Tree[self.node2].distance - self.Tree[self.find_parent()].distance

    def find_parent(self):
        current1 = self.node1
        current2 = self.node2
        lst = [self.node1, self.node2]
        root = 1
        while True:
            if self.Tree[current1].parent != 0:
                if self.Tree[current1].parent in lst: 
                    root = self.Tree[current1].parent
                    break
                lst.append(self.Tree[current1].parent)
                current1 = self.Tree[current1].parent

            if self.Tree[current2].parent != 0:
                if self.Tree[current2].parent in lst: 
                    root = self.Tree[current2].parent
                    break
                lst.append(self.Tree[current2].parent)
                current2 = self.Tree[current2].parent

            if self.Tree[current1].parent == 0 and self.Tree[current2].parent == 0: 
                root = 1
                break
        return root

Tree = [[] for _ in range(N+1)]
Tree[1] = Node(0, adjL[1], 0)

que = deque()
que.append((1, adjL[1]))

# 트리 만들기
while que:
    parent, lst = que.popleft()
    for i in lst:
        adjL[i].pop(adjL[i].index(parent))
        Tree[i] = Node(parent, adjL[i], Tree[parent].distance+1)
        que.append((i, adjL[i]))

# 각 노드 출력
# for i in range(1, len(Tree)):
#     print(f'parent: {Tree[i].parent}, childs: {Tree[i].childs}, distance: {Tree[i].distance}')

answer = 0
for i in range(1, N):
    for j in range(i+1, N+1):
        tmp = Cal(i, j, Tree)
        answer += tmp.find_distance()
        # print(f'node1: {i}, node2: {j}, answer : {answer}\n')
print(answer)


'''
예제 2번 : 84

1-2 : 3
1-3 : 2
1-4 : 1
1-5 : 1
1-6 : 2
1-7 : 2
1-8 : 3
14

2-3 : 5
2-4 : 4
2-5 : 3
2-6 : 3
2-7 : 4
2-8 : 4
23

3-4 : 2
3-5 : 3
3-6 : 4
3-7 : 4
3-8 : 5
18

4-5 : 2
4-6 : 3
4-7 : 3
4-8 : 4
12

5-6 : 2
5-7 : 2
5-8 : 3
7

6-7 : 3
6-8 : 3
6

7-8 : 4
4
'''