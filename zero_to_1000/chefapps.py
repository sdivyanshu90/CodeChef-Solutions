# cook your dish here
for _ in range(int(input())):
    s, x, y, z = map(int, input().split())
    count = 0
    tot = x + y + z
    maxi = max(x, y)
    while tot > s:
        if maxi == x:
            tot -= x
        else:
            tot -= y
        count += 1
    print(count)