import sys;
input = sys.stdin.readline

def sol():
    # N = 접시의 수
    # d = 초밥의 가짓수
    # k = 연속해서 먹는 접시의 수
    # c = 쿠폰 번호
    N, d, k, c = list(map(int, input().split()))
    
    rail = [int(input().rstrip()) for _ in range(N)]
    rail += rail[0:k-1]
    
    ans_list = []
    for i in range(N):
        consecutive = rail[i:i+k]
        sushi = set(consecutive)
        
        if c in sushi:
            ans_list.append(len(sushi))
        else:
            ans_list.append(len(sushi)+1)
    
    print(max(ans_list))
       
sol()