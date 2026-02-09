# Question Link: https://www.codechef.com/problems/ZCOSCH

# cook your dish here
n = int(input())
if n >= 1 and n <= 50:
    print("100")
elif n >= 51 and n <= 100:
    print("50")
else:
    print("0")