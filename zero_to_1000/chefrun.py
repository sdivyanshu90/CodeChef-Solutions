# Question Link: https://www.codechef.com/problems/CHEFRUN

# cook your dish here
for _ in range(int(input())):
    x1, x2, x3, v1, v2 = map(int, input().split())
    kefa = (x2 - x3) / v2
    chef = (x3 - x1) / v1
    if chef > kefa:
        print("Kefa")
    elif chef < kefa:
        print("Chef")
    else:
        print("Draw")