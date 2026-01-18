# cook your dish here
for _ in range(int(input())):
    n = int(input())
    res = 0
    while n != 50:
        if n > 50:
            n -= 3
        else:
            n += 2
        res += 1
    print(res)