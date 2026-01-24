# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n % 5 != 0:
        print(-1)
    else:
        if n % 10 == 0:
            print(0)
        else:
            res = 0
            while n % 10:
                n *= 2
                res += 1
            print(res)