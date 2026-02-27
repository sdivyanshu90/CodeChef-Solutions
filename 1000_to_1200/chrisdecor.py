# cook your dish here
for _ in range(int(input())):
    n, x, y = map(int, input().split())
    
    if x < n:
        print("NO")
        continue
    
    op1 = max(0, 2*n - x)
    op2 = min(n, y // 3)
    
    if op1 <= op2:
        print("YES")
    else:
        print("NO")