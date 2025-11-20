# Question Link: https://www.codechef.com/problems/MANGOES

# cook your dish here
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    res = (z - y) // x
    print(res)