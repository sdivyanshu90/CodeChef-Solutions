# Question Link: https://www.codechef.com/problems/FAIRSHARE

# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    share = n // (k + 1)
    # print(share)
    print(n - (k * share))