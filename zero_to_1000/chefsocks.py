# Question Link: https://www.codechef.com/problems/CHEFSOCKS

# cook your dish here
a, x, y = map(int, input().split())
if x + y >= a:
    print("YES")
else:
    print("NO")