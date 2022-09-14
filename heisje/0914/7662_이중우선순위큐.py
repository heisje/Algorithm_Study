
TC = int(input())
for _ in range(TC):
    N = int(input())
    d_tree = dict()

    # 루트 짜기
    i_or_d, n = input().split()
    n = int(n)
    d_tree[n] = [None, None, 1]
    root = n

    # input 반복
    for _ in range(N - 1):
        i_or_d, n = input().split()
        n = int(n)

        # 트리 인풋
        
        if i_or_d == 'I':
            if root == None:
                d_tree[n] = [None, None, 1]
                root = n
            else:
                go = root
                before = None # 이전 것도 찾아야해
                while True:
                    left, right, _ = d_tree.get(go)
                    if n == go:  # 같으면
                        d_tree[n][2] += 1 # left, right, 개수
                        break
                    elif n < go:  # 작으면
                        if left == None: # 비어있으면 채워준다.
                            d_tree[go][0] = n 
                            d_tree[n] = [None, None, 1] # left, right, 개수
                            break
                        else:
                            go = left # 왼쪽으로 가본다.
                    elif go < n: # 크면
                        if right == None: # 비어있으면 채워준다.
                            d_tree[go][1] = n 
                            d_tree[n] = [None, None, 1]
                            break
                        else:
                            go = right

        #트리 삭제
        elif i_or_d == 'D':
            if root == None:
                pass
            else:
                go = root
                before = root
                if n == -1 : #최솟값 삭제
                    while True:
                        left, right, num = d_tree.get(go)
                        if left == None: # 비어있으면 삭제한다.
                            if num >= 2:
                                d_tree[go][2] -= 1
                            elif right != None: # 삭제방법: 삭제할 곳의 right가 존재하면 before와 연결시켜준다.
                                d_tree[before][0] = right
                            else:
                                d_tree[before][0] = None
                                if go == root and before == root:
                                    if d_tree[root][1] != None: #루트에 뭐가 들어있으면
                                        root = d_tree[root][1] 
                                    else: 
                                        root = None
                            break
                        else:         # 비어있지 않으면
                            before = go
                            go = left # 왼쪽으로 가본다.
                if n == 1 : #최댓값 삭제
                    while True:
                        left, right, num = d_tree.get(go)
                        if right == None: # 비어있으면 삭제한다.
                            if num >= 2:
                                d_tree[go][2] -= 1
                            elif left != None: # 삭제방법: 삭제할 곳의 right가 존재하면 before와 연결시켜준다.
                                d_tree[before][1] = left
                            else:
                                d_tree[before][1] = None
                                if go == root and before == root:
                                    if d_tree[root][0] != None: #루트에 뭐가 들어있으면
                                        root = d_tree[root][0] 
                                    else: 
                                        root = None
                            break
                        else:         # 비어있지 않으면
                            before = go
                            go = right # 왼쪽으로 가본다.

    #왼쪽 프린트
    if root == None:
        print('EMPTY')
    else:
        
        go = root        
        while True:
            left, right, _ = d_tree.get(go)
            if right == None: # 비어있으면 삭제한다.
                print(go, end=' ')
                break
            else:         # 비어있지 않으면
                go = right # 왼쪽으로 가본다.
        go = root
        while True:
            left, right, _ = d_tree.get(go)
            if left == None: # 비어있으면 print
                print(go)
                break
            else:         # 비어있지 않으면
                go = left # 왼쪽으로 가본다.

#print(d_tree)

            
