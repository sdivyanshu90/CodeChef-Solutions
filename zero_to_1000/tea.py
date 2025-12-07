# cook your dish here
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    if x == y or y > x:
        print(z)
    else:
        frac = x // y
        if x % y == 0:
            print(frac * z)
        else:
            print((frac + 1) * z)