# Question Link: https://www.codechef.com/problems/BUDGET_

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if 30 * y <= x:
        print("YES")
    else:
        print("NO")