def find_root(cell, i, j):
    ni, nj = i, j
    while True:
        if type(cell[ni][nj]) != tuple:
            return (ni, nj)
        ni, nj = cell[ni][nj][0], cell[ni][nj][1]

def Update(cell, i, j, value):
    root_i, root_j = find_root(cell, i, j)
    cell[root_i][root_j] = value

def Merge(cell, i1, j1, i2, j2):
    root_i1, root_j1 = find_root(cell, i1, j1)
    root_i2, root_j2 = find_root(cell, i2, j2)
    # dictionary 쓰면 빠르긴 할텐데 귀찮아서 완전탐색 돌림..
    if cell[root_i1][root_j1]:
        for tmp_i in range(50):
            for tmp_j in range(50):
                if cell[tmp_i][tmp_j] == (root_i2, root_j2):
                    cell[tmp_i][tmp_j] = (root_i1, root_j1)
        cell[root_i2][root_j2] = (root_i1, root_j1)
    else:
        for tmp_i in range(50):
            for tmp_j in range(50):
                if cell[tmp_i][tmp_j] == (root_i1, root_j1):
                    cell[tmp_i][tmp_j] = (root_i2, root_j2)
        cell[root_i1][root_j1] = (root_i2, root_j2)

def Unmerge(cell, i, j):
    root_i, root_j = find_root(cell, i, j)
    val = cell[root_i][root_j]
    # dictionary 쓰면 빠르긴 할텐데 귀찮아서 완전탐색 돌림 22
    for tmp_i in range(50):
        for tmp_j in range(50):
            if cell[tmp_i][tmp_j] == (root_i, root_j):
                cell[tmp_i][tmp_j] = ''
    cell[root_i][root_j] = ''
    cell[i][j] = val

def func(lst, cell):
    if lst[0] == 'UPDATE':
        if len(lst) == 4:
            i, j = int(lst[1])-1, int(lst[2])-1
            Update(cell, i, j, lst[3])
        else:
            # dictionary 쓰면 빠르긴 할텐데 귀찮아서 완전탐색 돌림 333
            for i in range(50):
                for j in range(50):
                    if cell[i][j] == lst[1]:
                        cell[i][j] = lst[2]

    elif lst[0] == 'MERGE':
        i1, j1, i2, j2 = map(int, lst[1:])
        i1, j1, i2, j2 = i1-1, j1-1, i2-1, j2-1
        ci1, cj1 = find_root(cell, i1, j1)
        ci2, cj2 = find_root(cell, i2, j2)
        if ci1 == ci2 and cj1 == cj2:
            return
        Merge(cell, ci1, cj1, ci2, cj2)

    elif lst[0] == 'UNMERGE':
        i, j = int(lst[1])-1, int(lst[2])-1
        Unmerge(cell, i, j)

    elif lst[0] == 'PRINT':
        i, j = int(lst[1])-1, int(lst[2])-1
        i, j = find_root(cell, i, j)
        return cell[i][j] if cell[i][j] else "EMPTY"


def solution(commands):
    answer = []
    cell = [[''] * 50 for _ in range(50)]
    for command in commands:
        lst = list(command.split(' '))
        res = 0
        res = func(lst, cell)
        if res:
            answer.append(res)

    return answer

'''
테스트 1 〉	통과 (1.04ms, 10.4MB)
테스트 2 〉	통과 (0.84ms, 10.4MB)
테스트 3 〉	통과 (0.05ms, 10.5MB)
테스트 4 〉	통과 (0.06ms, 10.5MB)
테스트 5 〉	통과 (0.39ms, 10.5MB)
테스트 6 〉	통과 (1.20ms, 10.4MB)
테스트 7 〉	통과 (0.80ms, 10.4MB)
테스트 8 〉	통과 (1.13ms, 10.6MB)
테스트 9 〉	통과 (3.50ms, 10.4MB)
테스트 10 〉	통과 (4.42ms, 10.4MB)
테스트 11 〉	통과 (7.84ms, 10.4MB)
테스트 12 〉	통과 (9.82ms, 10.3MB)
테스트 13 〉	통과 (48.68ms, 10.4MB)
테스트 14 〉	통과 (51.30ms, 10.4MB)
테스트 15 〉	통과 (95.09ms, 10.4MB)
테스트 16 〉	통과 (73.11ms, 10.5MB)
테스트 17 〉	통과 (100.19ms, 10.4MB)
테스트 18 〉	통과 (77.87ms, 10.4MB)
테스트 19 〉	통과 (92.40ms, 10.3MB)
테스트 20 〉	통과 (139.81ms, 10.4MB)
    테스트 21 〉	통과 (197.51ms, 10.5MB)
테스트 22 〉	통과 (91.43ms, 10.3MB)
'''
