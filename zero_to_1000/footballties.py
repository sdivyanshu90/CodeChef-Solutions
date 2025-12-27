# Question Link: https://www.codechef.com/problems/FOOTBALLTIES

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    print(min(x % 3, y % 3))