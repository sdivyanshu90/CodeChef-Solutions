# cook your dish here
for _ in range(int(input())):
    n = int(input())
    res = []
    for i in range(n):
        a = list(map(int, input().split()))
        res.append(a)
        
    for i in range(n-2, -1, -1):
        for j in range(len(res[i])):
            res[i][j] = res[i][j] + max(res[i+1][j], res[i+1][j+1])
    print(res[0][0])