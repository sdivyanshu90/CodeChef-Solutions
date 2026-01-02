# Question Link: https://www.codechef.com/problems/GENE01

# cook your dish here
a, b = map(str, input().split())
if a == "R" or b == "R":
    print("R")
elif a == "B" or b == "B":
    print("B")
else:
    print("G")