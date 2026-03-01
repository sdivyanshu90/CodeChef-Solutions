# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    res = ""
    
    for num in d:
        if num % k == 0:
            res += "1"
        else:
            res += "0"
            
    print(res)