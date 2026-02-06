# Question Link: https://www.codechef.com/problems/KTTABLE

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    res = 0
    if b[0] <= a[0]:
        res += 1
    for i in range(1, n):
        if b[i] <= a[i] - a[i-1]:
            res += 1
    
    print(res)