K = int(input())
order = list(map(int, input().split()))
tree = [[] for _ in range(K)]

def visit(lv, order):
    m = len(order) // 2
    tree[lv].append(order[m])
    
    if len(order) == 1:
        return
    
    visit(lv + 1, order[:m])
    visit(lv + 1, order[m+1:])
    
visit(0, order)

for i in tree:
    print(*i)