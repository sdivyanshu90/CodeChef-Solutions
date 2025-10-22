# Question Link: https://www.codechef.com/problems/SKONG

# cook your dish here
x, h = map(int, input().split())
date = abs(4 - x)
print(date * 24 + h)