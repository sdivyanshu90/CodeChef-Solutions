# Question Link: https://www.codechef.com/problems/CANDYDIST

# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    distrib = n /  m
    if distrib % 2 == 0:
        print("Yes")
    else:
        print("No")