# Question Link: https://www.codechef.com/problems/DIFFSUM

# cook your dish here
n1, n2 = map(int, input().split())
if n1 > n2:
    print(n1 - n2)
else:
    print(n1 + n2)