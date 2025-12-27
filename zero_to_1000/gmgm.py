# cook your dish here
for _ in range(int(input())):
    n, d = map(int,input().split())
    a = list(map(int,input().split()))
    
    res = 0
    small = True
    for num in a:
        if num <= d and small == False:
            res += 1
            small = True
        elif num > d and small == True:
            res += 1
            small = False
            
    print(res)