# Question Link: https://www.codechef.com/problems/IED

# cook your dish here
a, b, c = map(int, input().split())
if a * c > b * c:
    print(a * c)
else:
    print(b * c)