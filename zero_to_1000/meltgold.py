# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    res = 1
    
    for i in range(1, x - y + 1):
        y += i
        if y >= x:
            break
        res += 1
    print(res)