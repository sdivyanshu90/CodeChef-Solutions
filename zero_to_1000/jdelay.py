# cook your dish here
for _ in range(int(input())):
    n = int(input())
    time = []
    for _ in range(n):
        a, b = map(int, input().split())
        time.append(b - a)
    
    res = 0
    for t in time:
        if t > 5:
            res += 1
    print(res)