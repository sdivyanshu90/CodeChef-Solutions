# cook your dish here
for _ in range(int(input())):
    l, r = map(int, input().split())
    
    res = 0
    for i in range(l, r + 1):
        unit = i % 10
        if unit == 2 or unit == 3 or unit == 9:
            res += 1
            
    print(res)