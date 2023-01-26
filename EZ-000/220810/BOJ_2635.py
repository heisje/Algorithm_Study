import sys
N = int(sys.stdin.readline())
longest = []

for n in range(1, N + 1):
    seq = [N, n]
    while True:
        if seq[-2] - seq[-1] < 0:
            break
        else:
            seq.append(seq[-2] - seq[-1])
    if len(seq) > len(longest):
        longest = seq[:]

print(len(longest))
print(*longest)
