# Question Link: https://www.codechef.com/problems/APPLORNG

# cook your dish here
n = int(input())
apple, orange = map(int, input().split())
if apple + orange <= n:
    print("Yes")
else:
    print("No")