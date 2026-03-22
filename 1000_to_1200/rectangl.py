# cook your dish here
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if abs(a - b) == abs(c - d):
        print("YES")
    else:
        print("NO")