# Question Link: https://www.codechef.com/problems/NONNEGPROD

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    prod = 1
    for num in a:
        prod *= num
    # print(prod)
    if prod >= 0:
        print(0)
    else:
        print(1)