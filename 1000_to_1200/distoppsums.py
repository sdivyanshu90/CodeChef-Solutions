# cook your dish here
for _ in range(int(input())):
    n = int(input())
    
    res = []
    l, r = 1, n
    
    while l < r:
        res.append(l)
        res.append(r)
        l += 1
        r -= 1
        
    print(*res)