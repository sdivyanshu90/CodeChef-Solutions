# Question Link: https://www.codechef.com/problems/HWFIN

# cook your dish here
x, y = map(int, input().split())
if x + y * 10 >= 100:
    print("Yes")
else:
    print("No")