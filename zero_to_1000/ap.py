# cook your dish here
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    if y - x == z - y:
        print(0)
    else:
        print(1)