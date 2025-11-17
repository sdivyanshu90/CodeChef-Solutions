# Question Link: https://www.codechef.com/problems/MERRYXMAS

# cook your dish here
n = int(input())
if n >= 7:
    print(3)
elif n == 2 or n == 1:
    print(1)
elif 3 <= n <= 6:
    print(2)