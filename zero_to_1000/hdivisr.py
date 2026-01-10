# Question Link: https://www.codechef.com/problems/HDIVISR

# cook your dish here
res = []
n = int(input())

for i in range(1, n + 1):
    if n % i == 0:
        if i >= 1 and i <= 10:
            res.append(i)
print(max(res))