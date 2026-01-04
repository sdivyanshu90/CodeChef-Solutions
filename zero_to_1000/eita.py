# cook your dish here
for _ in range(int(input())):
    d, x, y, z = map(int, input().split())
    first = x * 7
    second = y * d + (z * (7 - d))
    print(max(first, second))