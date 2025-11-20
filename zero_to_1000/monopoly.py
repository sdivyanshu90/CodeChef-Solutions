# Question Link: https://www.codechef.com/problems/MONOPOLY

# cook your dish here
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    if (x + y) < z or (y + z) < x or (x + z) < y:
        print("Yes")
    else:
        print("No")