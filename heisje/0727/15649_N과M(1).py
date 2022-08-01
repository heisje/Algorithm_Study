#https://www.acmicpc.net/problem/15649 
#핵심은 O(n!)인가..? 재귀 반복문을 내가 쓸 수 있을까

#DFS랑 BFS가 뭔데!

#재귀 함수 (N = 최대크기, m = 순열개수, check_box = 숫자가 사용되었는지, result_li = 결과, max_len = 최대길이)
def foring(N, m, check_box, result_li, max_len):
    if m == 0:
        print(*result_li)
        return
    for i in range(1, N + 1):
        if check_box[i] == False:
            result_li[max_len - m] = i
            check_box[i] = True
            foring(N,m - 1,check_box, result_li, max_len)
            result_li[max_len - m] = None
            check_box[i] = False
    return

#N은 숫자 최대크기, M은 길이
N, M = map(int,input().split()) 

check_box = {i:False for i in range(1, N + 1)} #숫자가 들어있는지 확인
result_li = [None for _ in range(M)] #결과값
max_len = M #최대길이
foring(N, M, check_box, result_li, max_len)

#print(result_li)

#  n n-1 4 3 2 1
#  1 2 3 4 5 n


'''
import copy
def sohard(li, count):
    sub_li = copy.deepcopy(li)
    for key in sub_li:
        if count == 0:
            return ' '
        else:
            sub_li.remove(key)
            return str(key) + ' ' + str(sohard(sub_li, count-1))
# M = maxi, N = N(num)
maxi, N = map(int,input().split())

result_li = [[] for _ in range(N)] #결과를 넣을 리스트

count = N
li = [i for i in range(1, maxi)] #숫자로 이루어진 list 생성
print(sohard(li, N))

'''
'''
maxi, N = map(int,input().split()) 
real_result_li = []

for i in range(1, maxi):# 맨 앞자리 구하고
    li = [i for i in range(1, maxi)]
    result_li = [i]
    li.remove(i)
    for i in li:#맨 앞자리에서 쓴거 빼고 구하고
        result_li += i
        li.remove(i)
        for i in li:#빼고 빼고 구하고
            result_li += i
            li.remove(i)
            real_result_li.append(result_li)
print(real_result_li)
'''
    
'''
def foring(M, N):
    for i in range(1, M + 1):
        if N == 1:
            return str(i)
        else:
            return str(i) + " " + str(foring(M,N - 1)) #마지막 자리까지 

M, N = map(int,input().split()) #M은 숫자 최대크기, N은 길이
result_li = []
print(foring(M, N))
#print(result_li)
'''
