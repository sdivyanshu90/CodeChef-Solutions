# Question Link: https://www.codechef.com/problems/MONEYDOUBLE

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x < 1000:
        x += 1000
        print((2 ** (y - 1))* x)
    else:
        print((2 ** y) * x)