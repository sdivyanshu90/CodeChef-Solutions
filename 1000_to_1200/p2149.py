# cook your dish here
for _ in range(int(input())):
    a, b, x = map(int, input().split())
    rec = a * b
    sq = x * x
    if rec <= sq:
        print(0)
    elif min(a, b) <= sq:
        print(1)
    else:
        print(2)