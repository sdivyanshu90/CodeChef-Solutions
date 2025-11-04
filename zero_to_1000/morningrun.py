# Question Link: https://www.codechef.com/problems/MORNINGRUN

# cook your dish here
x, y = map(int, input().split())
if 2 * (x + y) >= 1000:
    print("YES")
else:
    print("NO")