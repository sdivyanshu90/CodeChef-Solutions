# Question Link: https://www.codechef.com/problems/ACTEMP

# cook your dish here
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a <= b and b >= c:
        print("Yes")
    else:
        print("No")