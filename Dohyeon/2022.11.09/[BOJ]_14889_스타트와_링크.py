from itertools import combinations


def calc_taste(list_):
    global matrix

    result = 0

    a = list(combinations(list_, 2))
    for b in a:

        result = result + matrix[b[0]][b[1]] + matrix[b[1]][b[0]]

    return result


N = int(input())

matrix = [None] * N

ingredients = list(range(N))                         
full_set = set(ingredients)

min_gap = 20000 * 16 * 16                              

for i in range(N):
    matrix[i] = list(map(int, input().split()))

comb = list(combinations(ingredients, N // 2))        


for j in range(len(comb)//2):
    set1 = set(comb[j])                                
    set2 = full_set - set1                              

    list1 = list(set1)                                  
    list2 = list(set2)

    gap = abs(calc_taste(list2) - calc_taste(list1))

    if min_gap > gap:
        min_gap = gap

print(min_gap)