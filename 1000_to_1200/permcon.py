# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    
    groups = [[] for _ in range(k)]
    
    for i in range(1, n + 1):
        groups[i % k].append(i)
    
    ans = [0] * (n + 1)
    possible = True
    
    for g in groups:
        if len(g) == 1:
            possible = False
            break
        
        for i in range(len(g)):
            ans[g[i]] = g[(i + 1) % len(g)]
    
    if not possible:
        print(-1)
    else:
        print(*ans[1:])