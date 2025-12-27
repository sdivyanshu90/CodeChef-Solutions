# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    d = list(map(int, input().split()))
    res = 0
    for i in range(n):
        if s[i] == d[i]:
            res += 1
            
    print(res)