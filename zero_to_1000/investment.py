# Question Link: https://www.codechef.com/problems/INVESTMENT

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x >= 2 * y:
        print("YES")
    else:
        print("NO")