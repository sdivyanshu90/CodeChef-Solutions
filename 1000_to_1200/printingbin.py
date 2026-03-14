# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    res = []
    for num in arr:
        if num == 1:
            res.append(0)
        else:
            res.append(1)
            
    print(*res)