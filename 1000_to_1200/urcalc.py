# Question Link: https://www.codechef.com/problems/URCALC

# cook your dish here
a = int(input())
b = int(input())
s = input()
if s == "+":
    print(a + b)
elif s == "-":
    print(a - b)
elif s == "*":
    print(a * b)
else:
    print(a / b)