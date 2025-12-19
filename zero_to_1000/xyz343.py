# cook your dish here
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    tot = x * y
    res = 0
    if tot <= z:
        print(0)
    else:
        while tot > z:
            tot -= y
            res += 1
        print(res)