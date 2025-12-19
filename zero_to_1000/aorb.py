# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    resa, resb = 0, 0
    p1 = x * 2
    p2 = (x + y) * 4
    p3 = y * 4
    p4 = (x + y) * 2
    resa = (500 - p1) + (1000 - p2)
    resb = (1000 - p4) + (500 - p3)
    print(max(resa, resb))