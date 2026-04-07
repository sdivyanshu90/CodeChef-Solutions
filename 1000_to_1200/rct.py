# cook your dish here
for _ in range(int(input())):
    w, l = map(int, input().split())
    if (w * l) % 2 == 0:
        print("YES")
    else:
        print("NO")