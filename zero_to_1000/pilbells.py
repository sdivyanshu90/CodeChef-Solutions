# cook your dish here
for _ in range(int(input())):
    n, x, k, p = map(int, input().split())
    if k == 0:
        print(p)
    elif k < n:
        if k > x:
            print(p + (x * 10) + ((k - x) * 5))
        else:
            print(p + (k * 10))
    else:
        print(p + (x * 10) + ((k - x) * 5) + 20)