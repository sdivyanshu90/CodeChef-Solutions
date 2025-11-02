# Question Link: https://www.codechef.com/problems/MULT3

# cook your dish here
n = int(input())
if (n + 1) % 3 == 0:
    print(n + 1)
elif (n - 1) % 3 == 0:
    print(n - 1)
else:
    print(n)