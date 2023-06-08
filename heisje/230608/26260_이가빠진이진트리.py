# 236ms

class TreeClass:
    
    def __init__(self, N):
        self.tree = [0 for _ in range(N + 1)]
        self.lenTree = N

    def left(self, i):
        if i * 2 > self.lenTree:
            return False   
        return True
    
    def right(self, i):
        if i * 2 + 1 > self.lenTree:
            return False   
        return True

    # 순회
    def postOrder(self, i):
        if self.left(i):
            self.postOrder(i*2)
        if self.right(i):
            self.postOrder(i*2 + 1)
        print(self.tree[i], end=' ')
    
    # 값 넣기
    def push(self, idx, value):
        self.tree[idx] = value

    # 트리 만들기
    def makeTree(self, Tree, idx, li):
        # 중앙점을 잡는다.
        value = li[len(li) // 2]
        Tree.push(idx, value)

        # 갈래를 나눈다.
        if len(li) >= 3:
            # 왼쪽 리스트로 roof를 돈다.
            self.makeTree(Tree, idx * 2, li[:len(li) // 2])
            # 오른쪽 리스트로 roof를 돈다. 
            self.makeTree(Tree, idx * 2 + 1, li[len(li) // 2 + 1:])

def main(N, li, add):
    # -1의 값을 치환한다.
    li[li.index(-1)] = add
    li.sort()
    Tree = TreeClass(N)

    # 중심점누적해가면서 트리를 만든다.
    Tree.makeTree(Tree, 1, li)
    # 후위순회를 한다.
    Tree.postOrder(1)

N = int(input())
li = list(map(int, input().split()))
add = int(input())
main(N, li, add)