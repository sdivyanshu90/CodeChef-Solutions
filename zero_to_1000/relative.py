# Question Link: https://www.codechef.com/problems/RELATIVE

# cook your dish here
for _ in range(int(input())):
    g, c = map(int, input().split())
    print((c ** 2) // (2*g))