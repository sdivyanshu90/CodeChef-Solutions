# Question Link: https://www.codechef.com/problems/TCG

# cook your dish here
x, y = map(int, input().split())
if x - y == 0:
    print("SAME")
elif x > y:
    print("DECREASED")
else:
    print("INCREASED")