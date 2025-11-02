# Question Link: https://www.codechef.com/problems/CHEFONDATE

# Chef also went on a date with his girlfriend. Le me solving his problem. Very Sed Life!!
# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x >= y:
        print("YES")
    else:
        print("NO")