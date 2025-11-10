# Question Link: https://www.codechef.com/problems/SIXFRIENDS

# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    double = 3 * x
    triple = 2 * y
    if double > triple:
        print(triple)
    else:
        print(double)