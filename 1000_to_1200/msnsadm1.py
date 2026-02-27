# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    for i in range(n):
        a[i] = 20 * a[i]
        b[i] = 10 * b[i]
        
    temp = []
    for i in range(n):
        temp.append(a[i] - b[i])
    
    res = max(temp)
    if res > 0:
        print(res)
    else:
        print(0)