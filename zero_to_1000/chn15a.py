# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    res = 0
    
    for num in a:
        if (num + k) % 7 == 0:
            res += 1
            
    print(res)