# Question Link: https://www.codechef.com/problems/HOWMANY

# cook your dish here
n = int(input())
res = 0
while n != 0:
    n //= 10
    res += 1
# print(res)
if res > 3:
    print("More than 3 digits")
else:
    print(res)