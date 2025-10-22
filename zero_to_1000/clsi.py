# Question Link: https://www.codechef.com/problems/CLSI

# cook your dish here
n, b = map(int, input().split())
required_iq = b * 10
if required_iq <= n:
    print("YES")
else:
    print("NO")