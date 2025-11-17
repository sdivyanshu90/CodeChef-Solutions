# Question Link: https://www.codechef.com/problems/EXPIRY

# cook your dish here
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a <= b * c:
        print("Yes")
    else:
        print("No")