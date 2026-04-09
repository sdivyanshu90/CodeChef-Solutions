# Question Link: https://www.codechef.com/problems/SPLITN

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    p = bin(n).count('1')
    print(p - 1)