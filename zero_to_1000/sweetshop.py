# Question Link: https://www.codechef.com/problems/SWEETSHOP

# cook your dish here
n, x = map(int, input().split())
rem = n - 10*x
print(rem // 20)