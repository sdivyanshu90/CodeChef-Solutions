# Question Link: https://www.codechef.com/problems/DATATYPE

# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    print(m % (n + 1))