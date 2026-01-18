# cook your dish here
for _ in range(int(input())):
    a, b = map(int, input().split())
    diff = abs(a - b)
    if diff % 2 == 0:
        print("YES")
    else:
        print("NO")