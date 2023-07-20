from itertools import combinations

def get_triangle_area(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c
    
    step1 = ax * by + bx * cy + cx * ay
    step2 = bx * ay + cx * by + ax * cy
    triangle = abs(step1 - step2) * 0.5
    
    return triangle


def sol():
    N = int(input())
    dots = [list(map(int, input().split())) for _ in range(N)]
    triangles = []

    for a, b, c in combinations(dots, 3):
        triangles.append(get_triangle_area(a, b, c))
        
    return max(triangles)


print(sol())