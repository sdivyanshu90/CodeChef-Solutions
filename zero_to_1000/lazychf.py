# Question Link: https://www.codechef.com/problems/LAZYCHF

# cook your dish here
for _ in range(int(input())):
    x, m, d = map(int, input().split())
    print(min(x * m, x + d))