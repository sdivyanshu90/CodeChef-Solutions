# Question Link: https://www.codechef.com/problems/FOOTCUP

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == y and x != 0 and y != 0:
        print("YES")
    else:
        print("NO")