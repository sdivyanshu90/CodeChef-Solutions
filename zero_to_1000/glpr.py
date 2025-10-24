# Question Link: https://www.codechef.com/problems/GLPR

# cook your dish here
x, y = map(int, input().split())
if 2 * x < y:
    print("PLASTIC")
else:
    print("METAL")