# Question Link: https://www.codechef.com/problems/BORROWBOOK

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    occ = {}

    for i, value in enumerate(a, start=1):
        occ[value] = max(occ.get(value, 0), i)

    print(sum(occ.values()))