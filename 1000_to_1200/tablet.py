# Question Link: https://www.codechef.com/problems/TABLET

# cook your dish here
for _ in range(int(input())):
    n, budget = map(int, input().split())
    temp = []
    for _ in range(n):
        w, h, p = map(int, input().split())
        temp.append((w*h, p))
        
    res = 0
    for area, price in temp:
        if price <= budget:
            res = max(res, area)
    if res:
        print(res)
    else:
        print("no tablet")