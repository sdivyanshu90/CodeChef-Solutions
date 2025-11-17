# Question Link: https://www.codechef.com/problems/TVDISC

# cook your dish here
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    tvone = a - c
    tvtwo = b - d
    if tvone > tvtwo:
        print("Second")
    elif tvtwo > tvone:
        print("First")
    else:
        print("Any")