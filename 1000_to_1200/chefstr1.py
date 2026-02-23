# Question: https://www.codechef.com/problems/CHEFSTR1

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    res = 0
    for i in range(1, n):
        res += abs(s[i] - s[i - 1]) - 1
    print(res)