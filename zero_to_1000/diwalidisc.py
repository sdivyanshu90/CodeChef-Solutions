# Question Link: https://www.codechef.com/problems/DIWALIDISC

# cook your dish here
a, b = map(int, input().split())
if a > b:
    print(a - b)
else:
    print(0)