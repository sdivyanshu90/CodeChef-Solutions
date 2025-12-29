# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = (n + 1) * 100
    c = (b * 50) // 100
    d = c - sum(a)
    if d > 100:
        print(-1)
    elif d <= 0:
        print(0)
    else:
        print(d)