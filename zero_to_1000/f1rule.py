# Question Link: https://www.codechef.com/problems/F1RULE

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    qualify = x * 1.07
    if y <= qualify:
        print("YES")
    else:
        print("NO")