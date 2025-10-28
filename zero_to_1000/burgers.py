# Question Link: https://www.codechef.com/problems/BURGERS

# cook your dish here
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        print(b)
    else:
        print(a)