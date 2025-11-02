# Question Link: https://www.codechef.com/problems/P1149

# cook your dish here
x, y, k = map(int, input().split())
if abs(x - y) <= k:
    print("YES")
else:
    print("NO")