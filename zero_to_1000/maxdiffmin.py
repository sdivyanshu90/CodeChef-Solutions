# Question Link: https://www.codechef.com/problems/MAXDIFFMIN

# cook your dish here
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a > b > c:
        print(a - c)
    elif b > a > c:
        print(b - c)
    else:
        print(c - a)