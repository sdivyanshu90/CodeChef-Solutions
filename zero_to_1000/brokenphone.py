# Question Link: https://www.codechef.com/problems/BROKENPHONE

# cook your dish here
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a < b:
        print("REPAIR")
    elif a > b:
        print("NEW PHONE")
    else:
        print("ANY")