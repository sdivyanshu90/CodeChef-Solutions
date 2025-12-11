# Question Link: https://www.codechef.com/problems/BULLET

# cook your dish here
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    a = y // x
    diff = z - a
    if diff < 0:
        print(0)
    else:
        print(diff)