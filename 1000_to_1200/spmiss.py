# cook your dish here
for _ in range(int(input())):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    s = input()
    
    normal_sum = 0
    special_sum = 0
    
    for i in range(n):
        if s[i] == '0':
            normal_sum += a[i]
        else:
            special_sum += a[i]
    
    ans = normal_sum
    
    if normal_sum >= c:
        ans = max(ans, normal_sum + special_sum - c)
    
    print(ans)