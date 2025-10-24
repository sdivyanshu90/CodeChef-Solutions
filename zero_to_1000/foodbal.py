# Question Link: https://www.codechef.com/problems/FOODBAL

# cook your dish here
a, b, c, d = map(int, input().split())
first = abs(a - b)
second = abs(c - d)
if first > second:
    print("Second")
elif first == second:
    print("Both")
else:
    print("First")