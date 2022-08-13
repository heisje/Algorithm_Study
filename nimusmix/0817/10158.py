W, H = map(int, input().split())
p, q = map(int, input().split())
T = int(input())

p_li = list(range(W+1)) + list(range(W-1, 0, -1))
q_li = list(range(H+1)) + list(range(H-1, 0, -1))

print(p_li[(p+T)%(len(p_li))], q_li[(q+T)%(len(q_li))])