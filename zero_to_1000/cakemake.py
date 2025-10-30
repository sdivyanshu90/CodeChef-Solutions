# Question Link: https://www.codechef.com/problems/CAKEMAKE

# cook your dish here
res = set()
a, b = map(int, input().split())

for i in range(1, max(a, b) + 1):
    for j in range(1, max(a, b) + 1):
        if i == j or i > a or j > b:
            continue
        else:
            res.add((i, j))
            
print(len(res))