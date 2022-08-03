N, M = map(int, input().split())
a = []

def func():
    if len(a) == M:
        print(' '.join(map(str,a)))
        return
    else:
        for i in range(1,N+1):
            if i not in a:
                a.append(i)
                func()
                a.pop()
func()