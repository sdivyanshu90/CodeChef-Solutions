# Question Link: https://www.codechef.com/problems/CCISLAND

# cook your dish here
for _ in range(int(input())):
    x, y, xr, yr, d = map(int, input().split())
    food = x / xr
    water = y / yr
    mini = min(food, water)
    if mini >= d:
        print("YES")
    else:
        print("NO")