# Question Link: https://www.codechef.com/problems/ONEFULPAIRS

# cook your dish here
a, b = map(int, input().split())
op = a + b + (a * b)
if op == 111:
    print("Yes")
else:
    print("No")