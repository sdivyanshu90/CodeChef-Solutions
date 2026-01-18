# Question Link: https://www.codechef.com/problems/RUNCOMPARE

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    alice = list(map(int, input().split()))
    bob = list(map(int, input().split()))
    res = 0
    for i in range(n):
        if alice[i] > 2*bob[i] or bob[i] > 2*alice[i]:
            continue
        else:
            res += 1
    print(res)