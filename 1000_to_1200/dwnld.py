# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    res = 0
    for _ in range(n):
        t, d = map(int, input().split())
        if k > 0:
            k -= t
            if k < 0:
                res += (d * (-k))
        else:
            res += (d * t)
    print(res)