# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(-1)
    else:
        if n % 2 == 0:
            res = [1] * (n // 2) + [-1] * (n // 2)
            print(*res)
        else:
            res = [1] * ((n + 1) // 2) + [-2]
            res += [-1] * (n - len(res))
            print(*res)