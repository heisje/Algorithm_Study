def solution(nodeinfo):
    ans = [[], []]
    
    ys = sorted(set([x[1] for x in nodeinfo]), reverse=True)
    prev_y = ys[0]
    
    nodeinfo = [(idx+1, node) for idx, node in enumerate(nodeinfo)]
    nodeinfo.sort(reverse=True, key=lambda x: (x[1][1], -x[1][0]))
    
    ps = [x[0] for x in nodeinfo]
    prev_p = ps[0]

    c1 = [0] * (len(nodeinfo)+1)
    c2 = [0] * (len(nodeinfo)+1)

    
    def check_child(idx, p):
        nonlocal prev_y, prev_p, c1, c2
        
        for [c, [c_x, c_y]] in nodeinfo[idx+1:]:
            if c_y == prev_y:
                if c1[prev_p] and c2[prev_p]:
                    prev_p = ps[ps.index(prev_p)+1]
                elif not c1[prev_p]:
                    c1[prev_p] = c
                elif not c2[prev_p]:
                    c2[prev_p] = c
            else:
                prev_y = ys[ys.index(prev_y)+1]

    for idx, node in enumerate(nodeinfo):
        check_child(idx, ps[0])
        
    def preorder(p):
        if p:
            ans[0].append(p)
            preorder(c1[p][0])
            preorder(c2[p][0])
    
    def postorder(p):
        if p:
            postorder(c1[p][0])
            postorder(c2[p][0])
            ans[1].append(p)
            
    preorder(nodeinfo[0][0])
    postorder(nodeinfo[0][0])
    
    return ans