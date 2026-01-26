# Question Link: https://www.codechef.com/problems/SPCP4

# cook your dish here
for _ in range(int(input())):
    n, k, x = map(int, input().split())
    print(abs((n - k) % x - k % x))