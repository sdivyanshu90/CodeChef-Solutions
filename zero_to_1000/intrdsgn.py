# Question Link: https://www.codechef.com/problems/INTRDSGN

# cook your dish here
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    h1 = a + b
    h2 = c + d
    if h1 > h2:
        print(h2)
    else:
        print(h1)