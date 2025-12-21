# Question Link: https://www.codechef.com/problems/CHEFRACES

# cook your dish here
for _ in range(int(input())):
    x = set(map(int, input().split()))
    if len(x) == 4:
        print(2)
    elif len(x) == 3:
        print(1)
    else:
        print(0)