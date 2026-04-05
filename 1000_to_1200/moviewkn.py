# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    r = list(map(int,input().split()))
    res = []
    
    for i in range(n):
        res.append((i, r[i], l[i] * r[i]))
    
    res.sort(key= lambda x: (-x[2], -x[1], x[0]))

    # print(res)
    print(res[0][0] + 1)