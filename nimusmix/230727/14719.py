H, W = map(int, input().split())
blocks = list(map(int, input().split()))

ans = 0
for idx in range(1, W-1):
    left_max = max(blocks[:idx])
    right_max = max(blocks[idx+1:])
    lower = min(left_max, right_max)
    
    if blocks[idx] < lower:
        ans += lower - blocks[idx]
        
print(ans)