# Question Link: https://www.codechef.com/problems/PALL01

# cook your dish here
for _ in range(int(input())):
    n = (input())
    if n == n[::-1]:
        print("wins")
    else:
        print("loses")