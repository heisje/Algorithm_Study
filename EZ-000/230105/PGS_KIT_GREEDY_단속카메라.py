def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[1], x[0]))
    L = len(routes)
    i = 0
    while i < L:
        if i < L:
            pos = routes[i][1]
        i += 1
        while i < L and routes[i][0] <= pos <= routes[i][1]:
            i += 1
        answer += 1

    return answer
