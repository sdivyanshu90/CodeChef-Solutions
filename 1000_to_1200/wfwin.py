# cook your dish here
for _ in range(int(input())):
    m, p = map(int, input().split())
    
    k1 = (1000 - p - m) // 21
    k2 = 299 - m
    
    ans = min(k1, k2)
    print(max(0, ans))