# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    res = 0
    for num in a:
        if num >= x:
            res += 1
            
    print(res)