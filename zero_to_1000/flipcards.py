# Question Link: https://www.codechef.com/problems/FLIPCARD

# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    if n == x or x == 0:
        print(0)
    else:
        print(min(n - x, x))