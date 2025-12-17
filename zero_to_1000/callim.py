# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    runsum = 0
    res = 0
    for num in a:
        runsum += num
        if runsum <= k:
            res += 1
            
    print(res)