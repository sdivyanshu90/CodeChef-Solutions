# Question Link: https://www.codechef.com/problems/EVENODDDIV

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    f, g = 0, 0
    # print(f"n: {n}")
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:
            # print(f"Even i: {i}")
            f += 1
        elif n % i == 0 and i % 2 != 0:
            # print(f"Odd i: {i}")
            g += 1
            
    if f > g:
        print(1)
    elif f < g:
        print(-1)
    else:
        print(0)