import sys
w, h = map(int, sys.stdin.readline().split())
lines = int(sys.stdin.readline())

vcut = [0]
hcut = [0]
for _ in range(lines):
    d, n = map(int, sys.stdin.readline().split())
    if d:
        vcut.append(n)
    else:
        hcut.append(n)
vcut.sort()
hcut.sort()
vcut.append(w)
hcut.append(h)

ws = []
hs = []
for idx in range(len(vcut) - 1):
    ws.append(vcut[idx + 1] - vcut[idx])
for idx in range(len(hcut) - 1):
    hs.append(hcut[idx + 1] - hcut[idx])


print(max(ws) * max(hs))
