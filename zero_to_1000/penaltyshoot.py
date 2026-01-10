# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == y:
        print("YES")
    elif x > y:
        if (y + 1) < x:
            print("NO")
        else:
            print("YES")
    else:
        if (x + 2) < y:
            print("NO")
        else:
            print("YES")