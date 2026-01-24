# Question Link: https://www.codechef.com/problems/MINDAYSRET

# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    print((n + k - 1) // k)