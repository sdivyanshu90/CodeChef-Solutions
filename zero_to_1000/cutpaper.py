# Question Link: https://www.codechef.com/problems/CUTPAPER

# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    res = n // k
    print(res ** 2)