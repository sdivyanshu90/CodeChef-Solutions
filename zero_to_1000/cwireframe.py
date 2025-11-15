# Question Link: https://www.codechef.com/problems/CWIREFRAME

# cook your dish here
for _ in range(int(input())):
    n, m, x = map(int, input().split())
    total_length = 2 * (n + m)
    print(x * total_length)