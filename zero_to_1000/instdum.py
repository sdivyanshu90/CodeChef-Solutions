# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    run = 0
    for i in range(1, n + 1):
        run += a[i - 1]
        if ((run / i) * 100) == 100:
            res += 1
            
    print(res)