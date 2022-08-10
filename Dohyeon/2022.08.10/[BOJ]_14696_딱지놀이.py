import sys
input = lambda: sys.stdin.readline().strip()
N = int(input())

result=[]
a={ 1 : 0, 2 : 0 , 3 : 0, 4 : 0} # 입력받은 도형 종류별로 저장할 딕셔너리
b={ 1 : 0, 2 : 0 , 3 : 0, 4 : 0}
for i in range(N*2):
    if i % 2 == 0:
        list_A = list(map(int, input().split()))
        list_A[0] = 0 # 첫번째의 들어오는 값은 전체 도형 수 이므로 큰 의미가 없다. count 안되게 0으로 처리
        a[1] = list_A.count(1)
        a[2] = list_A.count(2)
        a[3] = list_A.count(3)
        a[4] = list_A.count(4)
    
    else:
        list_B = list(map(int, input().split()))
        list_B[0] = 0
        b[1] = list_B.count(1)
        b[2] = list_B.count(2)
        b[3] = list_B.count(3)
        b[4] = list_B.count(4)


        j = 4 # 별을 나타내는 4 부터 내려가면서 비교
        while(True):
            if a[j] > b[j]:
                result.append('A')
                break
            elif a[j] < b[j]:
                result.append('B')
                break
            else:
                if j == 1: # 1까지 갯수가 같으면 무승부
                    result.append('D')
                    break
                j = j - 1
for i in result:
    print(i)