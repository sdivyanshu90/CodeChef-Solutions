# cook your dish here
for _ in range(int(input())):
    z, y, a, b, c = map(int, input().split())
    remaining = z - y
    if remaining >= (a + b + c):
        print("YES")
    else:
        print("NO")