def sol():
    N = int(input())
    arr = list(map(int, input().split()))
    memory = [0]
         
    for i in arr:
        if memory[-1] < i:
            memory.append(i)
        else:
            l = 0
            r = len(memory)
            
            while l < r:
                m = (l + r) // 2
                if memory[m] < i:
                    l = m + 1
                else:
                    r = m
            memory[r] = i      
    return len(memory) - 1
       
print(sol())