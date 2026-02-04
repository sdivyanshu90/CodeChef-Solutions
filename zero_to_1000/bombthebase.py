# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    res = 0
    for i in range(n):
        if a[i] < x:
            res = i + 1

    print(res)