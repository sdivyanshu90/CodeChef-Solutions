# Question Link: https://www.codechef.com/problems/CHEFCHOCO

# cook your dish here
for _ in range(int(input())):
    c, x, y = map(int, input().split())
    print((c - x) * y)