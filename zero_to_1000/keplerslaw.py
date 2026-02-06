# Question Link: https://www.codechef.com/problems/KEPLERSLAW

# cook your dish here
for _ in range(int(input())):
    t1, t2, r1, r2 = map(int, input().split())
    first = t1 ** 2 / r1 ** 3
    second = t2 ** 2 / r2 ** 3
    if first == second:
        print("Yes")
    else:
        print("No")