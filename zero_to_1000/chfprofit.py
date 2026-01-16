# cook your dish here
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    buy = x * y
    sell = x * z
    print(sell - buy)