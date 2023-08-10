# 668ms
import sys
input = sys.stdin.readline
N, M = input().split()
defined = [input().rstrip() for _ in range(int(N))]
li = [input().rstrip() for _ in range(int(M))]

def main():
    answer=''
    setD = set()
    for d in defined:
        setD.add(d)

    for l in li:
        used = l.split(',')
        for u in used:
            setD.discard(u)
        answer += str(len(setD)) + '\n'

    print(answer.rstrip())

main()